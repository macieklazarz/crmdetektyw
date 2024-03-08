from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from .models import TypSprawy, Sprawa
from .forms import SprawaCreateForm, SprawaCreateInlineForm, NotatkaForm, NotatkaFormset, BrudnopisUpdateForm




class SprawaListView(LoginRequiredMixin, ListView):
	model = Sprawa
	context_object_name = "sprawy"
	# combined_queryset = CustomUser.objects.exclude(admin='True').exclude(detektyw='True')
	# queryset = combined_queryset.order_by("nazwisko")
	template_name = 'sprawy/case_list.html'


	def get_queryset(self):
		queryset = super(SprawaListView, self).get_queryset()
		user = self.request.user
		if user.admin:
			filtered_queryset = queryset.order_by('-data_rozpoczecia')
		elif user.detektyw:
			filtered_queryset = queryset.filter(detektyw=user).order_by('-data_rozpoczecia')
		else:
			filtered_queryset = queryset.filter(klient=user).order_by('-data_rozpoczecia')

		return filtered_queryset



	# def get_context_data(self, *args, **kwargs):
	# 	context = super(CustomerListView, self).get_context_data(*args,**kwargs)
	# 	context['type'] = 'klientów'
	# 	return context

class SprawaDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Sprawa
	context_object_name = "sprawa"
	template_name = 'sprawy/case_detail.html'
	


	def test_func(self, *args, **kwargs):
		current_case = self.get_object()

		return self.request.user.admin == 1 or current_case.detektyw == self.request.user or current_case.klient == self.request.user



	def post(self, request,  *args, **kwargs):
		# print('post1')
		if request.method == 'POST' and 'button' in request.POST:
			# print('post2')
			self.get_object().delete()

		return redirect('sprawy:case_list_view')



class SprawaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Sprawa
	template_name = 'sprawy/case_new.html'
	form_class = SprawaCreateForm

	def test_func(self, *args, **kwargs):


		return self.request.user.admin == 1 
    # specify the fields to be displayed
 
    # fields = ['title', 'description']
	def get_success_url(self):
		return reverse('sprawy:case_list_view')

	def test_func(self, *args, **kwargs):

		return self.request.user.admin == 1




class CaseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Sprawa
	context_object_name = "case"
	form_class = SprawaCreateForm
	template_name = 'sprawy/case_new.html'


	# def get_form_kwargs(self, *args, **kwargs):
	# 	kwargs = super(CustomerUpdateView, self).get_form_kwargs()
	# 	uuid = self.kwargs['pk']
	# 	user = CustomUser.objects.get(id=uuid)
	# 	is_detektyw = user.detektyw

	# 	kwargs['is_detektyw'] = is_detektyw
	# 	kwargs['requestor_is_admin'] = self.request.user.admin

		# return kwargs


	def get_success_url(self):
		return reverse('sprawy:case_detail', kwargs={'pk':self.object.id})


	def test_func(self, *args, **kwargs):
		case = self.get_object()

		return self.request.user.admin == 1 or self.request.user == case.detektyw





class NotatkaInline():
	form_class = SprawaCreateInlineForm
	model = Sprawa
	template_name = "sprawy/note_update.html"


	def form_valid(self, form):
		named_formsets = self.get_named_formsets()
		if not all((x.is_valid() for x in named_formsets.values())):
			return self.render_to_response(self.get_context_data(form=form))

		self.object = form.save()

		for name, formset in named_formsets.items():
			formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
			if formset_save_func is not None:
				formset_save_func(formset)
			else:
				formset.save()
		return redirect('sprawy:case_detail', pk=self.object.id)
		# return reverse('sprawy:case_detail_view self.object.id')

	def formset_notatki_valid(self, formset):
		notatki = formset.save(commit=False)  # self.save_formset(formset, contact)

		for obj in formset.deleted_objects:
			obj.delete()
		for notatka in notatki:
			notatka.sprawa = self.object
			notatka.autor = self.request.user
			notatka.save()

	# def get_form_kwargs(self, *args, **kwargs):
	# 	kwargs = super(NotatkaInline, self).get_form_kwargs()

	# 	kwargs['user'] = self.request.user

	# 	print(f'views user:{kwargs["user"]}')
	# 	return kwargs


class NotakaCreate(LoginRequiredMixin, NotatkaInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(NotakaCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'notatki': NotatkaFormset(prefix='notatki'),
            }
        else:
            return {
                'notatki': NotatkaFormset(self.request.POST or None, self.request.FILES or None, prefix='notatki'),

            }

class NotatkaUpdateView(LoginRequiredMixin, UserPassesTestMixin, NotatkaInline, UpdateView):
	def get_context_data(self, **kwargs):
		ctx = super(NotatkaUpdateView, self).get_context_data(**kwargs)
		ctx['named_formsets'] = self.get_named_formsets()
		return ctx

	def get_named_formsets(self):
		return {'notatki': NotatkaFormset(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='notatki',),
		}

	# def test_func(self, *args, **kwargs):
	# 	current_user = self.get_object()

	# 	return self.request.user.admin == 1 

	def get_form_kwargs(self, *args, **kwargs):
		kwargs = super(NotatkaUpdateView, self).get_form_kwargs()

		# kwargs['user'] = self.request.user

		# print(f'views user:{kwargs["user"]}')
		return kwargs





	def test_func(self, *args, **kwargs):
		current_object = self.get_object()


		return self.request.user.admin == 1 or current_object.detektyw == self.request.user





class BrudnopisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Sprawa
	context_object_name = "case"
	form_class = BrudnopisUpdateForm
	template_name = 'sprawy/case_new.html'


	# def get_form_kwargs(self, *args, **kwargs):
	# 	kwargs = super(CustomerUpdateView, self).get_form_kwargs()
	# 	uuid = self.kwargs['pk']
	# 	user = CustomUser.objects.get(id=uuid)
	# 	is_detektyw = user.detektyw 

	# 	kwargs['is_detektyw'] = is_detektyw
	# 	kwargs['requestor_is_admin'] = self.request.user.admin

		# return kwargs


	def get_success_url(self):
		return reverse('sprawy:case_detail', kwargs={'pk':self.object.id})


	def test_func(self, *args, **kwargs):
		current_case = self.get_object()

		return self.request.user.admin == 1 or current_case.detektyw == self.request.user