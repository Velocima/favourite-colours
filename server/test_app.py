import json

class TestAPICase:
    def test_root_response(self, api):
        res = api.get('/')
        assert res.status == '200 OK'

    def test_response_length(self, api):
        res = api.get('/people')
        finished = res.json
        assert res.status == '200 OK'
        assert len(finished["people"]) == 3

    def test_route_not_found(self, api):
        res = api.get('/imnothere')
        assert res.status == '404 NOT FOUND'