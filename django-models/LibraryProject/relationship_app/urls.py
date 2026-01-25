from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
   # path('', index, name='index'),
   # path('login/', login_view, name='login'),
   # path('logout/', logout_view, name='logout'),
   path('admin/', views.admin_view, name='admin_view'),
   path('librarian/', views.librarian_view, name='librarian_view'),
   path('member/', views.member_view, name='member_view'),
   path('register/', views.register, name='register'),
   path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='relationship_app/login.html'), name='logout'),
   path('books/', list_books, name='book_list'),
   path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]