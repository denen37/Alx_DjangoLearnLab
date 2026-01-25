from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test


def index(request):
    return HttpResponse("<h1 style='text-align: center;'>Welcome to the Library</h1>")

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    next_page = 'books/'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    next_page = 'login'


# class CustomRegisterView(CreateView):
#     template_name = 'relationship_app/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')  # use URL name, not path
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {
        'form': form
    })
    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page.
            return redirect('book_list')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'relationship_app/login.html', {'error': 'Invalid username or password'})
    return render(request, 'relationship_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context

@user_passes_test(lambda u: u.profile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: u.profile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.profile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')