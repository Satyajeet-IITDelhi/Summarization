# test_request.py

import requests

# Set the API endpoint and headers
url = "http://127.0.0.1:8000/summarise"
headers = {
    "Content-Type": "application/json"
}

# Define the input prompt
data = {
    "prompt": "In businesses, data scientists typically mine data for information that can be used to predict customer behavior..."
}

# Send POST request to the API
response = requests.post(url, json=data, headers=headers)

# Print the response from the server
print(response.json())
