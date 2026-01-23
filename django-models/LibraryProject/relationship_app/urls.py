from django.urls import path
from .views import CustomLoginView, CustomRegisterView, index
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
   path('', index, name='index'),
   path('login/', CustomLoginView.as_view(), name='login'),
   path('register/', CustomRegisterView.as_view(), name='register'),
   path('books/', list_books, name='book_list'),
   path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]