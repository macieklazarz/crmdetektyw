"""
URL configuration for aplikacja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, Homepage
from uzytkownicy.forms import UserLoginForm
from uzytkownicy.views import Register, SignUpView
from django.contrib.auth import views
from uzytkownicy.views import logout_view, CustomerListView, StaffListView,CustomerDetailView, CustomerUpdateView, StaffUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name="home"),
    path('', Homepage.as_view(), name="home"),
    path('login/',views.LoginView.as_view(template_name="uzytkownicy/login.html" ,authentication_form=UserLoginForm), name='login'),
    path('register/', SignUpView.as_view(), name="register"),
    path('logout/', logout_view, name="logout"),
    path('customer_list/', CustomerListView.as_view(), name="customer_list"),
    path('customer_detail/<uuid:pk>/', CustomerDetailView.as_view(), name="customer_detail"),
    path('customer_update/<uuid:pk>/', CustomerUpdateView.as_view(), name="customer_update"),
    path('staff_list/', StaffListView.as_view(), name="staff_list"),
    path('staff_update/<uuid:pk>/', StaffUpdateView.as_view(), name="staff_update"),
    path('case_list/', include('sprawy.urls', namespace='sprawy')),
]
