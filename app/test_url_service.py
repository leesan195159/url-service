from fastapi.testclient import TestClient
from app.database import redis_client
from app.main import app

client = TestClient(app)


def test_create_short_url():
    response = client.post("/shorten", json={"url": "https://example.com"})

    assert response.status_code == 200
    assert "short_url" in response.json()


def test_redirect_to_original_url():
    response = client.post("/shorten", json={"url": "https://example.com"})
    short_url = response.json()["short_url"].split("/")[-1]
    redirect_response = client.get(f"/{short_url}", follow_redirects=False)

    assert redirect_response.status_code == 301
    assert redirect_response.headers["location"] == "https://example.com"


def test_expired_url():
    response = client.post("/shorten", json={"url": "https://example.co.kr", "expires_at": "2024-07-15T08:30:00"})
    short_url = response.json()["short_url"].split("/")[-1]
    redirect_response = client.get(f"/{short_url}", follow_redirects=False)

    assert redirect_response.status_code == 404
    assert redirect_response.json() == {"detail": "Short URL not found"}


def test_hit_redis():
    response = client.post("/shorten", json={"url": "https://example.com"})
    short_url = response.json()["short_url"].split("/")[-1]
    redis_client.set(short_url, 0)
    client.get(f"/{short_url}")
    hits = redis_client.get(short_url)

    assert hits is not None
    assert int(hits) == 1


def test_redirect_to_original_url_not_found():
    invalid_short_url = "invalidshorturl"
    redirect_response = client.get(f"/{invalid_short_url}", follow_redirects=False)

    assert redirect_response.status_code == 404
    assert redirect_response.json() == {"detail": "Short URL not found"}


def test_get_stats():
    short_response = client.post("/shorten", json={"url": "https://example.com"})
    short_url = short_response.json()["short_url"].split("/")[-1]
    redis_client.set(short_url, 0)
    client.get(f"/{short_url}")  # Hit the URL to increase the count
    response = client.get(f"/stats/{short_url}")
    hits = redis_client.get(short_url)

    assert response.status_code == 200
    assert hits is not None
    assert "hits" in response.json()
    assert int(hits) == 1


def test_get_stats_not_found():
    invalid_short_url = "invalidshorturl"
    client.get(f"/{invalid_short_url}")  # Hit the URL to increase the count
    response = client.get(f"/stats/{invalid_short_url}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Short URL not found"}
