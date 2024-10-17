import requests

def get_Categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.status_code)
    categories_text = response.text
    print(categories_text)
    categories_json = response.json()
    for category in categories_json:
        print(category['name'])

