"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('diary-list/',views.DiaryListView.as_view(),name="diary_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(),name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(),name="diary_create"),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/',views.DiaryDeletelView.as_view(), name="diary_delete"),
]
