from http import HTTPStatus

import pytest
from django.urls import reverse
from pytest_lazy_fixtures.lazy_fixture import lf


@pytest.mark.django_db
def test_author_can_see_only_own_notes(author_client, stranger_client,
                                       test_note_author, test_note_stranger):
    url = reverse('notes:my_notes')
    response = author_client.get(url)
    assert test_note_author.text in response.content.decode()
    assert test_note_stranger.text not in response.content.decode()


@pytest.mark.django_db
def test_anonymous_cannot_see_notes(client, test_note_author):
    url = reverse('notes:my_notes')
    response = client.get(url)
    assert response.status_code == HTTPStatus.FOUND
    assert reverse('login') in response.url


@pytest.mark.django_db
@pytest.mark.parametrize('url_name',
                         ['notes:note_delete', 'notes:note_update'])
@pytest.mark.parametrize('user_fixture, response_status', [
    (lf('author_client'), HTTPStatus.OK),
    (lf('stranger_client'), HTTPStatus.FORBIDDEN),
    (lf('client'), HTTPStatus.FOUND),
])
def test_only_author_can_delete_update_notes(url_name, user_fixture,
                                             response_status,
                                             author_client, test_note_author):
    url = reverse(url_name, kwargs={'pk': test_note_author.id})
    response = user_fixture.get(url)
    assert response.status_code == response_status
