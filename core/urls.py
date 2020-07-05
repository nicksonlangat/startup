from django.urls import path 
from .import views 

urlpatterns = [
    path('' , views.index, name='home'),
    path('jobs/<int:opening_id>/', views.detail, name='detail'),
    path('upload/resume', views.resume, name='upload'),
    path("contact", views.contact, name="contact"),
]
