from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article

@permission_required('accounts.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'accounts/view_articles.html', {'articles': articles})

@permission_required('accounts.can_create', raise_exception=True)
def create_article(request):
    # simplified logic
    return render(request, 'accounts/create_article.html')

