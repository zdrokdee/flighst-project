from twilio.rest import Client

account_sid = "ACa9f97f406a598b4c5cb3a02c245e2405"
auth_token = "5cbd4ad7a13155c74e2d01724d8fb329"
twilio_virtual_number = "+14158010725"
to_my_number = "+48884657661"

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_virtual_number,
            to=to_my_number)

        print(message.sid)


