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
from django.contrib import admin
from django.urls import path
from runs.views import RunsListView, AddRunView, RunDetailsView, RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin-panel'),
    path('', RunsListView.as_view(), name="run_list"),
    path('add_run/', AddRunView.as_view(), name="add_run"),
    path('details/<int:run_id>/', RunDetailsView.as_view(), name = "run_details"),
    path('registration/<int:run_id>/', RegistrationView.as_view(), name = "registration"),
    # path('account/', UserPrivateDataView.as_view(), name='user_account'),

]
