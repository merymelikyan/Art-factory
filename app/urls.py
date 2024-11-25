from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('frequently_questions/', views.frequently_questions, name="frequently_questions"),
    path('drop_down/', views.drop_down, name="drop_down"),
 
    path('services/<int:seven_blocks_id>', 
          views.read_more, name="read_more"),
]