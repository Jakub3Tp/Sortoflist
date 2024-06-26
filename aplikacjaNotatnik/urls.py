from django.urls import path
from . import views

urlpatterns = [
    path('add_note/', views.add_note, name='add_note'),
    path("notes_list/", views.notes_list, name='notes_list'),
    path("detail_note/", views.detail_note, name='detail_note'),
    path("edit_note/", views.edit_note, name='edit_note'),
]