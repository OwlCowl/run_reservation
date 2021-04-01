"""Run_reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from runs.views import RunsListView, AddRunView, RunDetailsView, RegistrationView, ContactsView, UserPrivateDataView
from runs import views
app_name = "main"


urlpatterns = [
    path('admin_account/', admin.site.urls, name = 'admin-panel'),
    path('', RunsListView.as_view(), name="run_list"),
    path('add_run/', AddRunView.as_view(), name="add_run"),
    path('details/<int:run_id>/', RunDetailsView.as_view(), name = "run_details"),
    path('registration/<int:run_id>/', RegistrationView.as_view(), name = "registration"),
    path('contacts/', ContactsView.as_view(), name = 'contacts'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('account/<int:user_id>/', UserPrivateDataView.as_view(), name='user_account'),

]


