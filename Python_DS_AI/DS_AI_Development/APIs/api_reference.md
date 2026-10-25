
## Basic Operations

```python
# GET - Retrieve data
response = requests.get(url)

# POST - Send data
response = requests.post(url, data={'key': 'value'})

# With parameters
response = requests.get(url, params={'search': 'python'})
```

---

# Making Requests

## HTTP Methods - The Big 4

| Method | What it does | Has body? | Example use |
|--------|-------------|-----------|-------------|
| **GET** | Read/retrieve | ❌ | Get user list, search |
| **POST** | Create/send | ✅ | Login, create user, upload |
| **PUT** | Update | ✅ | Update user info |
| **DELETE** | Delete | ❌ | Remove record |

## GET vs POST - The Important Difference

### GET Request
```python
# Data goes in URL (visible to everyone!)
params = {"name": "Joseph", "ID": "123"}
r = requests.get("http://api.com/get", params=params)

print(r.url)          # http://api.com/get?name=Joseph&ID=123
print(r.request.body) # None
```

**Use GET for:** Search, filter, browse (non-sensitive data)

### POST Request
```python
# Data goes in body (hidden)
data = {"name": "Joseph", "ID": "123"}
r = requests.post("http://api.com/post", data=data)

print(r.url)          # http://api.com/post (clean!)
print(r.request.body) # name=Joseph&ID=123
```

**Use POST for:** Login, passwords, creating things

### 🔒 Security Rule
**NEVER use GET for passwords or sensitive data!** Everyone can see it in:
- Browser address bar
- History
- Server logs

---

## Query Strings (URL Parameters)

Add filters/parameters to URLs:

```
http://api.com/search ? q=python & lang=en & page=1
                      │   └──┬──┘   └──┬──┘   └──┬──┘
                      Start  Param1   Param2    Param3
```

```python
# Manual way (bad)
url = "http://api.com/search?q=python&lang=en"

# Better way - let Python build it
params = {"q": "python", "lang": "en"}
r = requests.get("http://api.com/search", params=params)
```

**Common uses:** `?search=`, `?page=`, `?limit=`, `?sort=`

---

# Understanding Responses

## Status Codes - What They Mean

### ✅ Success (2xx)
- **200 OK** - Success! Here's your data
- **201 Created** - Successfully created
- **204 No Content** - Success, but nothing to return

### ❌ Client Errors (4xx) - You messed up
- **400 Bad Request** - Invalid request
- **401 Unauthorized** - Need to login
- **403 Forbidden** - No permission
- **404 Not Found** - Doesn't exist
- **429 Too Many Requests** - Slow down!

### 💥 Server Errors (5xx) - They messed up
- **500 Internal Server Error** - Server broke
- **503 Service Unavailable** - Server down

### Quick Check
```python
response = requests.get(url)

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not found")
else:
    print(f"Error: {response.status_code}")
```

---

## Response Data Types

### 3 Ways to Get Data

```python
response = requests.get(url)

# 1. Text (HTML, XML, plain text)
text = response.text       # Returns string

# 2. JSON (APIs usually return this)
data = response.json()     # Returns dict/list

# 3. Binary (images, PDFs, videos)
bytes = response.content   # Returns bytes
```

### When to Use Which

| Use | For | Example |
|-----|-----|---------|
| `.text` | HTML, XML, plain text | Web pages |
| `.json()` | API data | `{"name": "John"}` |
| `.content` | Files, images, PDFs | Downloads |

---

## Encoding - Why Text Looks Weird

**Encoding** = How computers translate numbers ↔ text

```python
# Check encoding
print(response.encoding)  # Usually 'utf-8'

# UTF-8 handles everything
# ✅ English: Hello
# ✅ Chinese: 你好
# ✅ Arabic: مرحبا
# ✅ Emoji: 🎉
```

**Rule:** Always use UTF-8. It handles all languages and emojis.

---

# Common Patterns

## Download and Save a File

```python
import requests
import os

# 1. Get the file
r = requests.get('https://example.com/image.png')

# 2. Define where to save
path = os.path.join(os.getcwd(), 'image.png')

# 3. Save it (use 'wb' for binary files!)
with open(path, 'wb') as f:
    f.write(r.content)
```

**Key:** Use `.content` for files, not `.text`!

---

## Handle Errors Properly

```python
import requests

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raises error for bad status
    
    data = response.json()
    print("Success:", data)
    
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## Search/Filter with Parameters

```python
# Search API example
params = {
    "q": "python",
    "category": "books",
    "sort": "price",
    "limit": 10
}

response = requests.get("https://api.store.com/search", params=params)
# Builds: https://api.store.com/search?q=python&category=books&sort=price&limit=10
```

---

## POST with JSON Data

```python
# Creating a new user
new_user = {
    "name": "John",
    "email": "john@example.com",
    "age": 25
}

# Use json= for JSON data (not data=)
response = requests.post(
    "https://api.example.com/users",
    json=new_user  # Automatically sets Content-Type: application/json
)

if response.status_code == 201:
    print("User created!")
```

---

# Cheat Sheet

## Quick Reference

```python
import requests

# GET - Read data
r = requests.get(url)
r = requests.get(url, params={'key': 'value'})

# POST - Send data
r = requests.post(url, data={'key': 'value'})      # Form data
r = requests.post(url, json={'key': 'value'})      # JSON data

# Other methods
r = requests.put(url, json={'key': 'value'})       # Update
r = requests.delete(url)                            # Delete

# Response attributes
r.status_code    # 200, 404, etc.
r.text           # String (HTML, text)
r.json()         # Dict/list (JSON)
r.content        # Bytes (images, files)
r.headers        # Response headers
r.url            # Final URL
r.encoding       # Text encoding (utf-8)

# Request attributes
r.request.body   # What you sent
r.request.headers # Request headers
```

---

## Common Status Codes

| Code | Meaning | What to do |
|------|---------|------------|
| 200 | Success | Use the data |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Check your parameters |
| 401 | Unauthorized | Add authentication |
| 403 | Forbidden | You don't have permission |
| 404 | Not Found | Check the URL |
| 429 | Too Many Requests | Slow down, wait |
| 500 | Server Error | Try again later |

---

## File Modes

| Mode | Meaning | Use for |
|------|---------|---------|
| `'r'` | Read text | Reading text files |
| `'w'` | Write text | Writing text files |
| `'rb'` | Read binary | Reading images, PDFs |
| `'wb'` | Write binary | Saving images, PDFs |

---

## GET vs POST Summary

| | GET | POST |
|---|-----|------|
| **Data in** | URL | Body |
| **Python** | `params=` | `data=` or `json=` |
| **Use for** | Read, search | Create, login |
| **Secure?** | ❌ No | ✅ Better |
| **Example** | `?search=python` | Hidden in body |

---

