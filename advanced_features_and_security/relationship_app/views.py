from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserForm()
    return render(request, 'relationship_app/register.html', {'form': form})
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_view', raise_exception=True)
def list_books(request):
    # View logic
    pass

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    pass

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic to delete a book
    pass
