from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes_list'),
    path('my-notes/',
         views.MyNoteListView.as_view(),
         name='my_notes'),
    path('note_detail/<int:pk>/',
         views.NoteDetailView.as_view(),
         name='note_detail'
         ),
    path('note/create/',
         views.NoteCreateView.as_view(),
         name='note_new'),
    path('note/<int:pk>/update/',
         views.NoteUpdateView.as_view(),
         name='note_update'),
    path('note/<int:pk>/delete/',
         views.NoteDeleteView.as_view(),
         name='note_delete'),
]
