from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('load/<str:page>/', views.load_page, name='load_page'),
]