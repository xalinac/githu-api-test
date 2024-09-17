import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

BASE_URL = 'https://api.github.com'

HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'token {GITHUB_TOKEN}'
}

def create_repo():
    url = f'{BASE_URL}/user/repos'
    data = {
        'name': REPO_NAME,
        'private': False
    }
    response = requests.post(url, headers=HEADERS, json=data)
    return response

def check_repo_exists():
    url = f'{BASE_URL}/user/repos'
    response = requests.get(url, headers=HEADERS)
    repos = response.json()
    for repo in repos:
        if repo['name'] == REPO_NAME:
            return True

def delete_repo():
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(url, headers=HEADERS)
    return response

def test_github_api():
    response = create_repo()
    assert response.status_code == 201, f'Failed to create repo: {response.text}'

    assert check_repo_exists(), 'Repo does not exists'

    response = delete_repo()
    assert response.status_code == 204, f'Failed to delete repo: {response.text}'

    print('Test passed: Repo created and deleted successfully')

if __name__ == '__main__':
    test_github_api()