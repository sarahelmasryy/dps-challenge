# import requests

# github_url = "https://github.com/sarahelmasryy/dps-challenge"
# email = "sarahelmasryy@outlook.com"
# deployed_endpoint = "https://predictf-zptf65mnca-lm.a.run.app"
# notes = "Optional notes"

# # API endpoint URL
# api_url = "https://dps-challenge.netlify.app/.netlify/functions/api/challenge"

# # JSON payload
# payload = {
#     "github": github_url,
#     "email": email,
#     "url": deployed_endpoint,
#     "notes": notes
# }

# # Make the POST request
# response = requests.post(api_url, json=payload)

# # Check the response
# if response.status_code == 200:
#     print("POST request successful.")
# else:
#     print(f"Error: {response.status_code} - {response.text}")

import requests



request_body = {
    "year": 2020,
    "month": 10
}

url = "https://predictf-zptf65mnca-lm.a.run.app"

resp = requests.post(url, json=request_body)

# print("Response Code:", resp.status_code)

print("Response Text:", resp.text)
