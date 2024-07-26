import requests

# URL and headers for the requests
url_confirm = "http://pt-test-qlick.dev.qlife.co.jp/users/confirm"
url_register = "http://pt-test-qlick.dev.qlife.co.jp/users/register"
headers = {
    "Cookie": "qlick_session=eyJpdiI6Im9KS2FRRXFNWHZrdUxWemgvU2ZRQXc9PSIsInZhbHVlIjoiK0ppZVNKTjBZMUdQWHVWUW1Hb0JyNEFEY0lCRjZVQ1IvbjhTWmNFOXVLMjVNK0Q1REdpVjRHQWxvQmpzTjdxdEVpUGdla2sxSFN3YVlHTjNac0MxdVBCR1F0c0dRS0lnTWtCM2UxQXBzWm1YLzgyVWRQR2pSR3N4Q3pVL1Y4K2siLCJtYWMiOiIyMjQ3Mzc2MTc2ZGM4MDEwZWI5NDAxNzlmM2M0ODRlNmY4MWFkYWNlYTUzYzZiZjU4ZTNhM2I3YWYyNjJhNmJmIiwidGFnIjoiIn0%3D;",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Data for the requests
data_confirm = {
    "organizationId": "269",
    "name": "ishan",
    "email": "ishan%40asa.ass",
    "roleId": "3",
    "_token": "pQmDc7bx9oXSrF6fdlJ9p3DXvcJmJIK13vp8kC5R"
}

data_register = {
    "_token": "pQmDc7bx9oXSrF6fdlJ9p3DXvcJmJIK13vp8kC5R"
}

def create_users(count=30):
    for _ in range(count):
        response_confirm = requests.post(url_confirm, headers=headers, data=data_confirm)
        response_register = requests.post(url_register, headers=headers, data=data_register)
        if response_confirm.status_code == 200 and response_register.status_code == 200:
            print("User created successfully")
        else:
            print("Failed to create user")

if __name__ == "__main__":
    create_users()
