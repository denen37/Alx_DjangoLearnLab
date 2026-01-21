from django.urls import path
from .views import index, list_books
from .views import LibraryDetailView

urlpatterns = [
   path('', index, name='index'),
   path('books/', list_books, name='book_list'),
   path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]