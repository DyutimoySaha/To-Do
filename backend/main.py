import requests
import json

# Your Trello API credentials
API_KEY = 'API-KEY' 
#ATCTT3xFfGN0afaxHt8O7-yGQ6hChneSjiATnP02Dvt4xu7HbVUt1f1rxe0Nbsx_XHJpU8GfgsZGzj-VVqwAJt7yP5abf3oIZ7WxK3VYAivoLq7I-2nvJsOa5xoC_4dUL6pW8z6LjsSSqJeMbfC3kvnLPt6PfNp3jVYGTpMs6yBguLgxvI-0Ckc=B188648D'
API_TOKEN = 'ATTAc5cf594e3a6d37f9d75e7f9a315b8d9bb61a627ce4128169a347a54845e812b0F7ABDBC3'
BOARD_ID = '66751a418bd27ab3c4f37f31'  # Replace with your Trello board ID f6d21ee4-05a1-403a-899d-248b52476426

# Trello API URL
url = "https://api.trello.com/1/"

# Create lists on the board
def create_list(board_id, name):
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
        'name': name,
        'idBoard': board_id
    }
    response = requests.post(url + 'lists', params=query)
    return response.json()

# Create a card (task) in a list
def create_card(list_id, name, desc, due, labels):
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
        'idList': list_id,
        'name': name,
        'desc': desc,
        'due': due,
        'idLabels': labels
    }
    response = requests.post(url + 'cards', params=query)
    return response.json()

# Example: Create lists
to_do_list = create_list(BOARD_ID, "To Do")['id']
in_progress_list = create_list(BOARD_ID, "In Progress")['id']
review_list = create_list(BOARD_ID, "Review")['id']
done_list = create_list(BOARD_ID, "Done")['id']

# Example: Create labels
def create_label(board_id, name, color):
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
        'name': name,
        'color': color,
        'idBoard': board_id
    }
    response = requests.post(url + 'labels', params=query)
    return response.json()

development_label = create_label(BOARD_ID, "Development", "blue")['id']
design_label = create_label(BOARD_ID, "Design", "green")['id']
content_label = create_label(BOARD_ID, "Content", "yellow")['id']

# Example: Create cards (tasks)
create_card(to_do_list, "Implement Homepage Design", "Detailed task description.", "2024-06-25T00:00:00.000Z", [development_label])
create_card(to_do_list, "Optimize Images for Homepage", "Detailed task description.", "2024-06-27T00:00:00.000Z", [design_label])
create_card(to_do_list, "Write Homepage Copy", "Detailed task description.", "2024-06-29T00:00:00.000Z", [content_label])

print("Tasks created successfully!")
