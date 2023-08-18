import requests
import pytest
from jsonschema import validate, RefResolver

from blog.app import app
from blog.models import Article
# other code ....

@pytest.fixture
def client():
    app.config["TESTING"] = True
    
    with app.test_client() as client:
        yield client
        

@pytest.mark.e2e
def test_create_list_get(client):
    requests.post(
        "http://localhost:5000/create_article/",
        json={
            "author": "john@doe.com",
            "title":  "New Article",
            "content": "Some extra awesome content"
        }
    )
    response = requests.get(
        "http://localhost:5000/article-list/",
    )

    articles = response.json()

    response = requests.get(
        f"http://localhost:5000/article/{articles[0]['id']}/",
    )

    assert response.status_code == 200
