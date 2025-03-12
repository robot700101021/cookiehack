import requests
import json
# Set custom headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Make a GET request to fetch the initial response (with headers to avoid bot blocking)
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        print("Successfully fetched the page.")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

    # Extract and display cookies
    cookies = response.cookies
    print("Cookies received:")
    for cookie in cookies:
        print(f"{cookie.name}: {cookie.value}")

    # Fetch content again using received cookies
    response_with_cookies = requests.get(url, cookies=cookies, headers=headers, timeout=10)

    # Extract response text safely within Discord's limit
    html_snippet = response_with_cookies.text[:1800]  # Keeping it under Discord's limit
    print("Response fetched successfully.")

    # Discord webhook URL
    webhook_url = 'https://discord.com/api/webhooks/1345842563160211496/Bau8gJU5Cw6CDpHmwYXMMpi3T166rfE-g28MuQVhiUX_tK-E_QM4l75XIGlIY8eQD3YD'

    # Prepare message (excluding sensitive cookies)
    message = {
        "content": f"HTML Snippet from {url}:\n```{html_snippet}```"
    }

    # Send data to Discord webhook
    discord_response = requests.post(webhook_url, json=message)

    if discord_response.status_code == 204:
        print("Successfully sent the data to Discord.")
    else:
        print(f"Failed to send data. Status code: {discord_response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error occurred during requests: {e}")
