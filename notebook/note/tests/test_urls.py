from http import HTTPStatus

import pytest
from django.urls import reverse
from pytest_lazy_fixtures.lazy_fixture import lf


@pytest.mark.django_db
@pytest.mark.parametrize('url_name',
                         ['notes:note_detail', 'notes:note_update',
                          'notes:note_delete'])
@pytest.mark.parametrize('client_fixture, expected_status_code',
                         [(lf('author_client'), HTTPStatus.OK),
                          (lf('client'), HTTPStatus.FOUND)
                          ]
                         )
def test_notes_url_permissions_with_pk(client_fixture, expected_status_code,
                                       url_name,
                                       test_note_author):
    url = reverse(url_name, kwargs={'pk': test_note_author.id})
    response = client_fixture.get(url)
    assert response.status_code == expected_status_code


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', ['notes:notes_list', 'notes:note_new'])
@pytest.mark.parametrize('client_fixture, expected_status_code',
                         [(lf('author_client'), HTTPStatus.OK),
                          (lf('client'), HTTPStatus.FOUND)])
def test_notes_url_permissions_without_pk(
        client_fixture,
        expected_status_code,
        url_name):
    url = reverse(url_name)
    response = client_fixture.get(url)
    assert response.status_code == expected_status_code


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', ['users:all_users'])
@pytest.mark.parametrize('client_fixture, expected_status_code',
                         [(lf('author_client'), HTTPStatus.OK),
                          (lf('client'), HTTPStatus.FOUND)])
def test_notes_url_permissions_without_pk(client_fixture, expected_status_code,
                                          url_name):
    url = reverse(url_name)
    response = client_fixture.get(url)
    assert response.status_code == expected_status_code


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', ['users:user'])
@pytest.mark.parametrize('client_fixture, expected_status_code',
                         [(lf('author_client'), HTTPStatus.OK),
                          (lf('client'), HTTPStatus.FOUND)])
def test_notes_url_permissions_with_pk(client_fixture, expected_status_code,
                                       url_name, author):
    url = reverse(url_name, kwargs={'pk': author.id})
    response = client_fixture.get(url)
    assert response.status_code == expected_status_code
