from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create.as_view()),
    path('delete/<int:id>', views.delete.as_view()),
]