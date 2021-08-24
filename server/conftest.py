import pytest
import app

from app import people_data


@pytest.fixture
def api(monkeypatch):
    test_people = [  {
    "id": 1,
    "name": "daniel",
    "cohort": "morris",
    "fave_colour": {
        "name": "mustard",
        "hex:": "#deb326",
        "rgb": "222, 179, 38"
    }
  },
  {
      "id": 2,
      "name": "jawwad",
      "cohort": "morris",
      "fave_colour": {
          "name": "grey",
          "hex:": "#808080",
          "rgb": "128,128,128"
      }
  },
  {
      "id": 3,
      "name": "max",
      "cohort": "morris",
      "fave_colour": {
          "name": "purple",
          "hex:": "#7F00FF",
          "rgb": "127, 0, 255"
      }
  }]
    monkeypatch.setattr(app, "people_data", test_people)
    api = app.app.test_client()
    return api