from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms.form import NoteForm
from .models import Note


class NoteMixin(LoginRequiredMixin):
    model = Note


class CheckPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        note = self.get_object()
        user = self.request.user
        return note.author == user or user.is_superuser or user.is_staff


class NoteListView(NoteMixin, ListView):
    template_name = 'notes/all_notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        only_mine = self.kwargs.get('only_mine', False)
        qs = (Note
              .objects
              .select_related('author', 'status')
              .prefetch_related('categories')
              .order_by('-created_at'))
        if only_mine:
            qs = qs.filter(author=self.request.user)
            self.template_name = 'notes/my_notes.html'
        return qs


class MyNoteListView(NoteMixin, ListView):
    template_name = 'notes/my_notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.select_related('author',
                                           'status').prefetch_related(
            'categories').filter(author=self.request.user).order_by(
            '-created_at')


class NoteDetailView(NoteMixin, DetailView):
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


class NoteCreateView(NoteMixin, CreateView):
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:my_notes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(NoteMixin, CheckPermissionMixin, UpdateView):
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:my_notes')


class NoteDeleteView(NoteMixin, CheckPermissionMixin, DeleteView):
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:my_notes')
