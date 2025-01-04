from twilio.rest import Client
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_whatsapp_message(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    from_whatsapp_number = settings.TWILIO_WHATSAPP_NUMBER
    to_whatsapp_number = f"whatsapp:+593{to}"

    client.messages.create(
        body=message, from_=from_whatsapp_number, to=to_whatsapp_number
    )


def send_whatsapp_message_via_api(to, message):
    import requests

    url = f"{settings.WHATSAPP_API_URL}/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": f"+593{to}",
        "type": "text",
        "text": {"body": message},
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    # response.raise_for_status()
    return response.json()
