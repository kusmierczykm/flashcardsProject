from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nazwa kategorii'
        }


def index(request):
    return render(request, 'flashcards/index.html')


def add_category(request):
    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('flashcards:show_all_categories')
    return render(request, 'flashcards/add_category.html', {'form': form})


def show_all_categories(request):
    all_categories = Category.objects.all().order_by('name').values()
    context = {
        'categories': all_categories
    }
    return render(request, 'flashcards/all_categories.html', context)


def edit_category(request, id, type):
    category = get_object_or_404(Category, pk=id)
    if type == 'edit':
        form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('flashcards:show_all_categories')
        return render(request, 'flashcards/add_category.html', context)

    elif type == 'delete':
        # category.removed = True
        # category.save()
        category.delete()
        return redirect('flashcards:show_all_categories')
