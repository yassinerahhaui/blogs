from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_article),
    path('<int:id>', views.article)
]