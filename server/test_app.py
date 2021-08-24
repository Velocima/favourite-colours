import json

class TestAPICase:
    def test_root_response(self, api):
        res = api.get('/')
        assert res.status == '200 OK'