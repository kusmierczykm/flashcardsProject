from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.forms import ModelForm
from .models import Category, Flashcard


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nazwa kategorii'
        }


class WordForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['eng_word', 'pl_word', 'category']
        labels = {
            'eng_word': 'Słówko angielskie',
            'pl_word': 'Tłumaczenie polskie',
            'category': 'Kategoria'
        }
        # category = forms.ModelChoiceField(queryset=Flashcard.objects.all().order_by('-pk'), empty_label='Wybierz',
        #                                  widget=forms.Select(attrs={'class': 'custom-class'}))


class PrepareTestForm(forms.Form):
    count = forms.IntegerField(label="Ilość słówek")
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'), empty_label='Wszystkie', label="Kategoria", required=False)
    print('test')



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


def show_all_words(request):
    all_words = Flashcard.objects.all()
    context = {
        'words': all_words
    }
    return render(request, 'flashcards/all_words.html', context)


def add_word(request):
    form = WordForm(request.POST or None, request.FILES or None)
    all_words = Flashcard.objects.all()
    if form.is_valid():
        for word in all_words:
            if word.eng_word == form.cleaned_data['eng_word'] and word.pl_word == form.cleaned_data['pl_word']:
                return redirect('flashcards:show_all_words')

        form.save()
        return redirect('flashcards:show_all_words')
    return render(request, 'flashcards/add_word.html', {'form': form})


def edit_word(request, id, type):
    word = get_object_or_404(Flashcard, pk=id)
    if type == 'edit':
        form = WordForm(request.POST or None, request.FILES or None, instance=word)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('flashcards:show_all_words')
        return render(request, 'flashcards/add_word.html', context)

    elif type == 'delete':
        # category.removed = True
        # category.save()
        word.delete()
        return redirect('flashcards:show_all_words')


def prepare_test(request):
    form = PrepareTestForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        return redirect('flashcards:make_test', form.cleaned_data['count'],form.cleaned_data['category'])
    return render(request, 'flashcards/prepare_test.html', {'form': form})


def make_test(request, count, category):
    if category == 'None':
        data = Flashcard.objects.all()
    else:
        cats = Category.objects.all()
        for cat in cats:
            if category == cat.name:
                cat_id = cat.id
                break
        data = Flashcard.objects.filter(category=cat_id)
    context = {
        'count': count,
        'category': category,
        'data': data,
    }
    return render(request, 'flashcards/make_test.html', context)
