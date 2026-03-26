import requests

note_id = "69c510b54bb95da73a450ac2"  

url = f"http://127.0.0.1:5000/update-note/{note_id}"

data = {
    "user_id": "YOUR_USER_ID",   # 👈 IMPORTANT (needed for permission)
    "title": "Updated Title",
    "content": "Updated content"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)