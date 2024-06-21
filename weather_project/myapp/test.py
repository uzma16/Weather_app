from django.test import Client

# Initialize the test client
client = Client()

# Obtain the token for your user
response = client.post('/api-token-auth/', {'username': 'testuser', 'password': 'testpassword'})
token = response.json()['token']

# Use the token in subsequent requests
headers = {'HTTP_AUTHORIZATION': f'Token {token}'}
response = client.get('/api/weather/', **headers)
print(response.json())
