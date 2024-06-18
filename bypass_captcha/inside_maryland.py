import json
import requests


proxy = "u8b2e48e2564205c0-zone-custom-region-us-st-alabama-city-opelika:u8b2e48e2564205c0@43.159.28.126:2334"  # Indicate your proxy parameters
search_url = "https://casesearch.courts.state.md.us/casesearch/inquiry-search.jsp"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Reading cookies from a file
try:
    with open(r"C:\Users\Chicken Parmesean\Downloads\bypass_captcha\cookies_datadome.json", 'r') as json_file:
        cookies = json.load(json_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error reading updated cookie: {e}")
    cookies = None

if cookies and isinstance(cookies, dict):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'user-agent': user_agent,
        'referer': 'https://casesearch.courts.state.md.us/casesearch/',
        'origin': 'https://casesearch.courts.state.md.us',
        'connection': 'keep-alive',
        'upgrade-insecure-requests': '1',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1'
    }

    # Convert cookies to a format that requests library expects
    session_cookies = requests.cookies.RequestsCookieJar()
    for key, value in cookies.items():
        session_cookies.set(key, value)

    # Make the request with cookies and headers
    response = requests.get(search_url, headers=headers, cookies=session_cookies, proxies={'http': 'http://' + proxy}, verify=False)

    if response.status_code == 200:
        print("Entered the website successfully")
    else:
        print(f"Failed to enter the website, status code: {response.status_code}")
else:
    print("No valid cookie available or cookies are not in the correct format.")