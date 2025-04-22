from django.urls import path

from . import views


urlpatterns = [
    path('', views.ListBookView.as_view(), name='book_list'),
]