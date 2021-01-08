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
from runs.views import RunsListView, AddRunView, RunDetailsView, RunEnrollView, UserDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('run/add/', AddRunView.as_view(), name="add_run"),
    path('', RunsListView.as_view(), name="run_list"),
    path('details/<int:run_id>/', RunDetailsView.as_view(), name = "run_details"),
    path('run/enroll/<int:run_id>/', RunEnrollView.as_view(), name = "run_enroll"),
    path('account/', UserDataView.as_view(), name='user_account'),

]
