from api.api_client import APIClient
from api.endpoints import POSTS_ENDPOINT


def test_get_post():

    client = APIClient()

    response = client.get(
        f"{POSTS_ENDPOINT}/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1


def test_create_post():

    client = APIClient()

    request_data = {
        "title": "My First API Test",
        "body": "Learning API automation",
        "userId": 1
    }

    response = client.post(
        POSTS_ENDPOINT,
        data=request_data
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "My First API Test"
    assert data["body"] == "Learning API automation"
    assert data["userId"] == 1
    
def test_update_post():

    client = APIClient()

    update_data = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = client.put(
        f"{POSTS_ENDPOINT}/1",
        data=update_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated Title"
    assert data["body"] == "Updated Body"
    
def test_delete_post():

    client = APIClient()

    response = client.delete(
        f"{POSTS_ENDPOINT}/1"
    )

    assert response.status_code == 200