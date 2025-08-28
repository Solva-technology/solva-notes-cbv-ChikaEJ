from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.parametrize('url_name', [
    'notes:note_detail',
    'notes:note_list',
    'notes:note_update',
    'notes:delete_note',
])
@pytest.mark.parametrize('client_fixture', 'expected_status_code', [
    (pytest.lazy_fixture('author_client'), HTTPStatus.OK),
    (pytest.lazy_fixture('stranger_client'), HTTPStatus.NOT_FOUND),
])
def test_note_permissions(url_name, client_fixture, expected_status_code,
                          test_note):
    url = reverse(url_name, args=(test_note.id,))
    response = client_fixture.get(url)
    assert response.status_code == expected_status_code
