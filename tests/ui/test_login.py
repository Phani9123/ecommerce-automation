import pytest

from test_data.data_loader import load_json_data


LOGIN_TEST_DATA = load_json_data(
    "test_data/login_data.json"
)


@pytest.mark.parametrize(
    "test_data",
    LOGIN_TEST_DATA,
    ids=[
        "valid_login",
        "invalid_login"
    ]
)
def test_login(login_page, test_data):

    login_page.open()

    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    if "expected_url_part" in test_data:

        assert (
            test_data["expected_url_part"]
            in login_page.driver.current_url
        )

    else:

        assert (
            login_page.get_error_message()
            == test_data["expected_error"]
        )