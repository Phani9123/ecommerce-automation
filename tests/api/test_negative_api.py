from api.api_client import APIClient
from api.endpoints import POSTS_ENDPOINT


def test_get_nonexistent_post():

    client = APIClient()

    response = client.get(
        f"{POSTS_ENDPOINT}/999999"
    )

    assert response.status_code == 404
    
def test_login_with_invalid_credentials():

    client = APIClient()

    response = client.login(
        "wrong_user",
        "wrong_password"
    )

    assert response.status_code == 400
    
def test_authenticated_request_with_invalid_token():

    client = APIClient()

    invalid_headers = {
        "Authorization": "Bearer invalid_token"
    }

    response = client.get(
        "https://dummyjson.com/auth/me",
        headers=invalid_headers
    )

    assert response.status_code == 401