import requests
import json

def create_todo(url, data):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        return None

def main():
    url = "https://jsonplaceholder.typicode.com/todos"

    # Data to be sent in the POST request
    todo_data = {
        "title": "New Todo",
        "completed": False,
        "userId": 1
    }

    
    created_todo = create_todo(url, todo_data)

    
    if created_todo is not None:
        print("Created Todo:")
        print(json.dumps(created_todo, indent=2))

if __name__ == "__main__":
    main()
