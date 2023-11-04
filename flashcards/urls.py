from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.index, name='index'),
    path('addcategory/', views.add_category, name='add_category'),
    path('allcategories/', views.show_all_categories, name='show_all_categories'),
    path('editcategory/<int:id>/<str:type>/', views.edit_category, name='edit_category'),
    path('deletecategory/<int:id>/<str:type>/', views.delete_category, name='delete_category'),
]