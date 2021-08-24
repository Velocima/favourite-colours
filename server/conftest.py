import pytest
import app

from app import people_data


@pytest.fixture
def api(monkeypatch):
    test_people = [{"person": "colour"}]
    monkeypatch.setattr(app, "people_data", test_people)
    api = app.app.test_client()
    return api