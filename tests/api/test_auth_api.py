from api.api_client import APIClient
from api.endpoints import ME_ENDPOINT


def test_login_and_get_authenticated_user():

    client = APIClient()

    response = client.login(
        "emilys",
        "emilyspass"
    )

    assert response.status_code == 200
    assert client.access_token is not None

    response = client.get(
        ME_ENDPOINT
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "emilys"