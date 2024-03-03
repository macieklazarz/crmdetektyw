from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from .models import TypSprawy, Sprawa




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

		return self.request.user.admin == 1 or current_case.detektyw == self.request.user

	# def post(self, request,  *args, **kwargs):
	# 	print('post1')
	# 	if request.method == 'POST' and 'button' in request.POST:
	# 		print('post2')
	# 		self.get_object().delete()

	# 	return redirect('home')