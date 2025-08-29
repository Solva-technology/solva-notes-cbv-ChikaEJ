import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_my_notes_page_has_correct_context(author_client, test_note_author):
    url = reverse('notes:my_notes')
    response = author_client.get(url)
    assert 'У вас: 1 замет' in response.content.decode()
