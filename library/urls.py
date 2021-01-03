from django.urls import path
from library import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('authors/', views.author_list),
    path('authors/<int:pk>/', views.author_detail),
]
