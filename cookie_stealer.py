import webbrowser

url = 'https://www.roblox.com/home'
webbrowser.open(url)
import requests

# URL of the website you want to interact with
url = 'https://www.roblox.com/home'

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

