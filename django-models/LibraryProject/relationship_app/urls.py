from django.urls import path
from .views import login_view, logout_view, index, register_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
   path('', index, name='index'),
   # path('login/', login_view, name='login'),
   # path('logout/', logout_view, name='logout'),
   # path('register/', register_view, name='register'),
   path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('books/', list_books, name='book_list'),
   path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]