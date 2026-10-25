# Lab 3: API Usage - Quick Reference

> Essential patterns and concepts for working with APIs

---

## 📋 Standard API Pattern

This pattern works for **most REST APIs**:

```python
# 1. Import required libraries
import requests
import json
import pandas as pd

# 2. Make GET request to API
response = requests.get("API_URL")

# 3. Check if successful
if response.status_code == 200:
    # 4. Parse JSON (Convert JSON string → Python dict/list)
    data = json.loads(response.text)
    
    # 5. Convert to DataFrame
    df = pd.DataFrame(data)
    
    # 6. Normalize if nested (optional)
    df = pd.json_normalize(data)
    
    # 7. Extract specific information
    result = df.loc[df["column"] == "value"]
```

---

## 🔧 When to Use `json_normalize()`

### Problem: Nested JSON Data

**Use `json_normalize()` when** your JSON contains nested dictionaries or lists.

### Example

**Before normalize:**
```python
{
  "name": "Apple",
  "nutrition": {
    "calories": 52,
    "fat": 0.4,
    "sugar": 10.3
  }
}
```

This creates a DataFrame with nested data:
```
| name  | nutrition                              |
|-------|----------------------------------------|
| Apple | {'calories': 52, 'fat': 0.4, ...}     |
```
❌ **Problem:** Can't easily access individual nutrition values!

---

**After normalize:**
```python
df = pd.json_normalize(data)
```

This creates a flat DataFrame:
```
| name  | nutrition.calories | nutrition.fat | nutrition.sugar |
|-------|-------------------|---------------|-----------------|
| Apple | 52                | 0.4           | 10.3            |
```
✅ **Solution:** Each nested field becomes its own column!

---

## 📊 Complete Example

```python
import requests
import pandas as pd

# Get fruit data
response = requests.get("https://fruityvice.com/api/fruit/all")

if response.status_code == 200:
    # Parse and normalize
    df = pd.json_normalize(response.json())
    
    # Now you can easily access nutrition data
    print(df[['name', 'nutritions.calories', 'nutritions.sugar']])
    
    # Filter for specific fruit
    banana = df.loc[df['name'] == 'Banana']
    print(f"Banana calories: {banana.iloc[0]['nutritions.calories']}")
```

---

## 🎯 Key Takeaways

| Concept | When to Use | Example |
|---------|-------------|---------|
| `requests.get()` | Get data from any API | `requests.get(url)` |
| `response.json()` | Parse JSON directly | `data = response.json()` |
| `json.loads()` | Parse JSON text | `data = json.loads(response.text)` |
| `pd.DataFrame()` | Simple/flat JSON | `df = pd.DataFrame(data)` |
| `pd.json_normalize()` | **Nested JSON** | `df = pd.json_normalize(data)` |
| `.loc[]` | Filter rows | `df.loc[df['name'] == 'Apple']` |

---

## 💡 Pro Tips

1. **Always check status code** before parsing:
   ```python
   if response.status_code == 200:
       # Process data
   ```

2. **Use `response.json()`** instead of `json.loads(response.text)`:
   ```python
   # Better:
   data = response.json()
   
   # Instead of:
   data = json.loads(response.text)
   ```

3. **Handle nested data immediately** with `json_normalize()`:
   ```python
   # Saves time and headaches!
   df = pd.json_normalize(response.json())
   ```

4. **Column naming convention** for nested data:
   ```
   parent.child.grandchild
   nutritions.calories
   address.street.name
   ```

---

## 🔗 See Also

- Full examples: `Lab3_API_Examples.ipynb`
- API Reference: `../../api_reference.md`
