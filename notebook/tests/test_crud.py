from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_authenticated_user_can_create_a_note(author_client, status, category,
                                              author):
    new_note_url = reverse('notes:note_new')
    response = author_client.post(new_note_url,
                                  {'text': 'note text', 'author': author.id,
                                   'status': status.id,
                                   'categories': [category.id]})
    assert response.status_code == HTTPStatus.FOUND


@pytest.mark.django_db
def test_incorrect_data_from_form_returns_error_400(author_client, author,
                                                    status, category):
    new_note_url = reverse('notes:note_new')
    response = author_client.post(new_note_url,
                                  {'text': '',
                                   'author': author.id,
                                   'status': status.id,
                                   'categories': [category.id]})
    assert response.status_code == HTTPStatus.OK
    assert "form" in response.context
    assert response.context["form"].errors
    assert "text" in response.context["form"].errors
