import pytest
from django.test.client import Client

from note.models import Category, Status, Note


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create_user(username='author', )


@pytest.fixture
def stranger(django_user_model):
    return django_user_model.objects.create_user(username='stranger', )


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def stranger_client(stranger):
    client = Client()
    client.force_login(stranger)
    return client


@pytest.fixture
def category():
    return Category.objects.create(title='Category 1',
                                   description='Category 1')


@pytest.fixture
def status():
    return Status.objects.create(name='status', is_final=True)


@pytest.fixture
def test_note(category, status, author_client):
    note = Note.objects.create(
        text='Test note',
        status=status,
        author=author_client,
    )
    note.add(category)
    return note
