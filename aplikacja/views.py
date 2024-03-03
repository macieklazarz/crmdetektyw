from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	return render(request, 'aplikacja/home.html')



 
class Homepage(LoginRequiredMixin, View):                       #create a view 
    def get(self, request): 					             #'Get' is used to receive data from the server
        return render(request, 'aplikacja/home.html')


