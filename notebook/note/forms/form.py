from django import forms
from note.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', 'status', 'categories']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
