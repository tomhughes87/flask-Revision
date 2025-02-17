import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == "200 OK"

    def test_get_pokemon_handler(self, api):
        res = api.get("/pokemon")
        print('res is', res)
        print('res.json is', res.json)
        assert res.status == "200 OK"
        assert len(res.json) == 3

    def test_show_pokemon_handler(self, api):
        res = api.get('/pokemon/2')
        assert res.status == "200 OK"
        assert res.json['name'] == "wartortle"

    # def test_post_pokemon_handler(self, api):
    #     mock_pokemon = json.dumps({'name': 'pokemon1', "nickname": "sam", "type": "water", "level": 2})
    #     mock_headers = {'Content-Type': 'application/json'}

    #     res = api.post('/pokemon', data=mock_pokemon, headers=mock_headers)
    #     assert res.status == '201 CREATED'
    #     assert res.json['pokemon']['id'] == 4


