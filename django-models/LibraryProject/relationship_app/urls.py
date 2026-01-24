from django.urls import path
from .views import login_view, logout_view, index, register_view
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
   path('', index, name='index'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', register_view, name='register'),
   path('books/', list_books, name='book_list'),
   path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]