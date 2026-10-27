import pytest
from api_client import get_post, create_post, update_post, delete_post, get_comments

def test_get_post_id():
    response = get_post(1)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["userId"] == 1
    assert isinstance(post["body"], str)
    assert post["title"] != ""
    assert post["body"] != ""

def test_create_post():
    title = "Мой тестовый пост"
    body = "Создан он мной"
    user_id = 1
    response = create_post(title, body, user_id)
    assert response.status_code == 201
    created_post = response.json()
    assert created_post["title"] == title
    assert created_post["body"] == body
    assert "id" in created_post

def test_update_post():
    title = "Измененный заголовок"
    body = "Измененный текст"
    user_id = 1
    response = update_post(1, title, body, user_id)
    assert response.status_code == 200
    updated = response.json()
    assert updated["title"] == title
    assert updated["body"] == body

def test_delete_post():
    response = delete_post(1)
    assert response.status_code == 200

def test_get_comments_check_not_empty():
    response = get_comments(1)
    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) > 0

def test_get_non_existent_post():
    response = get_post(99999)
    assert response.status_code == 404
    assert response.json() == {}
