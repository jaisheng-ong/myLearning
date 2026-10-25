import requests
import pandas as pd

# Get Endpoint below:
"https://lol.balldontlie.io/?python#league-of-legends-api"

# Make API request to get LoL teams
response = requests.get(
    "https://api.balldontlie.io/lol/v1/teams",
    headers={"Authorization": "91b10ac9-4772-4033-9ab4-a4e546f235b7"},
    params={"per_page": 25}
)

# Check if successful
print("=" * 50)
print(f"Status Code: {response.status_code}")
print(f"Request Header: {response.request.headers}")
print(f"Request Body: {response.request.body}")
print("=" * 50)

r = response.headers

print("")
print("=" * 50)
print(f"Response Header: {r}")

print("")
print(f"Date of Request Sent: {r['Date']}")

print(f"Type of Data: {r['Content-Type']}")
print(f"Encoding: {response.encoding}") # Encoding tells the computer which "alphabet system" to use to read the text

print("=" * 50)


if response.status_code == 200:
    print("✓ Success! Data retrieved\n")
    
    # Convert to DataFrame
    data = response.json()
    df = pd.DataFrame(data['data'])  # Extract 'data' key from response
    
    # Display results
    print(f"Retrieved {len(df)} teams")
    print("\nFirst 5 teams:")
    print(df.head())
    
    # Show column names
    print(f"\nColumns available: {df.columns}")
    
    # Filter for a specific team
    print("\n" + "="*50)
    print("Filtering for T1 team:")
    print("="*50)
    key_team = df[df['name'] == '^-^']
    
    if not key_team.empty:
        print("\nTeam Found:")
        print(key_team)
    else:
        print("\nTeam not found. Available teams:")
        print(df['name'].tolist())
    
else:
    print(f"✗ Error: {response.status_code}")
    print(response.text)

