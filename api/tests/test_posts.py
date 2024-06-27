import pytest
from fastapi import status


def test_get_all_posts_unauthorized(client):
    res = client.get('/api/v1/posts')

    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize(('title', 'content', 'is_published'), [
    ('Test Post 01', 'This is a test post 01', True),
    ('Test Post 02', 'This is a test post 02', False),
    ('Test Post 03', 'This is a test post 03', True),
    ('Test Post 04', 'This is a test post 04', True),
    ('Test Post 05', 'This is a test post 05', False),
    ('Test Post 06', 'This is a test post 06', True),
])
def test_create_posts(authorized_client, title, content, is_published):
    data = {
        'title': title,
        'content': content,
        'is_published': is_published,
    }
    res = authorized_client.post('/api/v1/posts', json=data)

    assert res.status_code == status.HTTP_201_CREATED
    assert res.json().get('title') == data['title']
    assert res.json().get('content') == data['content']


def test_get_all_posts(authorized_client):
    res = authorized_client.get('/api/v1/posts')

    assert res.status_code == status.HTTP_200_OK
    assert len(res.json()) == 6
