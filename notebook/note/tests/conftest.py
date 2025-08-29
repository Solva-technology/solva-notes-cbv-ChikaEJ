import pytest
from django.test.client import Client
from note.models import Category, Note, Status


@pytest.fixture
def client(request):
    return Client()


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create_user(
        username="author",
        email="author@example.com",
        password="password123"
    )


@pytest.fixture
def stranger(django_user_model):
    return django_user_model.objects.create_user(
        username="stranger",
        email="stranger@example.com",
        password="password123"
    )


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
    return Category.objects.create(
        title="Category 1",
        description="Category 1 description"
    )


@pytest.fixture
def status():
    return Status.objects.create(name="status", is_final=True)


@pytest.fixture
def test_note_author(category, status, author):
    note = Note.objects.create(
        text='Author',
        status=status,
        author=author,
    )
    note.categories.set([category])
    return note


@pytest.fixture
def test_note_stranger(category, status, stranger):
    note = Note.objects.create(
        text='Stranger',
        status=status,
        author=stranger,
    )
    note.categories.set([category])
    return note
