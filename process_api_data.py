import requests
import json

def fetch_users(count=5):
    url = f"https://randomuser.me/api/?results={count}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise error if status != 200
        data = response.json()

        print("✅ API Data Fetched Successfully!\n")

        # Print full API data (for debugging/inspection)
        print(json.dumps(data, indent=4))

        # Extract only names and emails
        users = [
            {
                "name": f"{user['name']['first']} {user['name']['last']}",
                "email": user['email']
            }
            for user in data['results']
        ]

        # Save processed data to JSON file
        with open("users.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4)

        print("\n📂 Processed user data saved to users.json")
        return users

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching data: {e}")
        return []

if __name__ == "__main__":
    fetch_users(5)
