from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.index, name='index'),
    path('addcategory/', views.add_category, name='add_category'),
    path('allcategories/', views.show_all_categories, name='show_all_categories'),
    path('editcategory/<int:id>/<str:type>/', views.edit_category, name='edit_category'),
    path('allwords/', views.show_all_words, name='show_all_words'),
    path('addword/', views.add_word, name='add_word'),
    path('editword/<int:id>/<str:type>/', views.edit_word, name='edit_word'),
    path('preparetest/', views.prepare_test, name='prepare_test'),
    path('maketest/<int:count>/<str:category>', views.make_test, name='make_test'),
]