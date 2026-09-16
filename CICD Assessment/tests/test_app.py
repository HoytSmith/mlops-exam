import re
from collections.abc import Generator

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert re.match(".* on host .*", response.json())


# Add your tests here
def test_square(client):
    response = client.get("/square_root?number=2")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Square Root of 2.0 is 1.4142135623730951"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("a", "Input should be a valid number"),
        (-1, "Input should be greater than or equal to 0"),
        (None, "Field required"),
    ],
)
def test_square_invalid(client, test_input, expected):
    path = "/square_root"
    if test_input:
        path = path + f"?number={test_input}"
    response = client.get(path)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    assert expected in response.json().get("detail", "")[0].get("msg", "")
