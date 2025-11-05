# 09 - API Testing (Requests + Pytest)

## Basic requests
```python
import requests
r = requests.get("https://api.example.com/users")
assert r.status_code == 200
data = r.json()
```

## POST/PUT/DELETE
```python
r = requests.post(url, json={"name":"anbu"})
```

## Authentication
- Token auth: pass headers `{'Authorization': 'Bearer <token>'}`

## Chaining requests
```python
r = requests.post(login_url, json=creds)
token = r.json()['token']
r2 = requests.get(protected, headers={'Authorization':f'Bearer {token}'})
```

## Validation
- Assert status codes, response schema (use `jsonschema`), and important fields.