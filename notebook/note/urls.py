from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes'),
    path('my-notes/',
         views.MyNoteListView.as_view(),
         name='my_notes'),
    path('note_detail/<int:pk>/',
         views.NoteDetailView.as_view(),
         name='note_detail'
         ),
    path('note/create/',
         views.NoteCreateView.as_view(),
         name='new_note'),
    path('note/<int:pk>/update/',
         views.NoteUpdateView.as_view(),
         name='update_note'),
    path('note/<int:pk>/delete/',
         views.NoteDeleteView.as_view(),
         name='delete_note'),
]
