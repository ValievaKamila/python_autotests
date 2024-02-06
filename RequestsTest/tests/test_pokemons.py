import requests
import pytest

URL='https://api.pokemonbattle.me:9104'
HEADER={'Content-Type': 'application/json',
        'trainer_token': 'dae5885c5abe75056115c7bd1f93051c'}
qwery={'id': 3863}

def test_status_code():
    #1. Тест на проверку статус кода
    response=requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    assert response.status_code==200, 'Unexpected status code'

def test_id_trainer():
    #2. Тест на проверку наличия id тренера в ответе
    response=requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    qwery in response.json()

def test_id_trainer2():
    #3. Тест на проверку наличия id тренера в ответе 2
    response=requests.get(url=f'{URL}/trainers', params=qwery, headers=HEADER, timeout=5)
    assert response.status_code==200, 'Unexpected status code'
 