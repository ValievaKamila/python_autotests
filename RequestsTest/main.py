import requests

URL='https://api.pokemonbattle.me:9104'
HEADER={'Content-Type': 'application/json',
        'trainer_token': 'dae5885c5abe75056115c7bd1f93051c'}

body={
    "name": "generate",
    "photo": "generate"
}

response=requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(response.text)

body={
    "pokemon_id": "29816",
    "name": "generate",
    "photo": "generate"
}

response=requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(response.text)

body={
    "pokemon_id": "29816"
}

response=requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(response.text)