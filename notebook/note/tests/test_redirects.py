import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_redirect_after_login_to_my_notes(author, client):
    login_url = reverse('login')
    my_notes_url = reverse('notes:my_notes')
    response = client.post(login_url, {'username': author.get_username(),
                                       'password': 'password123'},
                           follow=True)
    print(response)
    assert response.redirect_chain
    assert response.redirect_chain[-1][0] == my_notes_url
