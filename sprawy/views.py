from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from .models import TypSprawy, Sprawa
from .forms import SprawaCreateForm




class SprawaListView(LoginRequiredMixin, ListView):
	model = Sprawa
	context_object_name = "sprawy"
	# combined_queryset = CustomUser.objects.exclude(admin='True').exclude(detektyw='True')
	# queryset = combined_queryset.order_by("nazwisko")
	template_name = 'sprawy/case_list.html'


	def get_queryset(self):
		queryset = super(SprawaListView, self).get_queryset()
		user = self.request.user
		if user.is_staff:
			filtered_queryset = queryset.order_by('-data_rozpoczecia')
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
		return reverse('sprawy:case_list_view')


	def test_func(self, *args, **kwargs):
		current_user = self.get_object()

		return self.request.user.is_staff == 1


