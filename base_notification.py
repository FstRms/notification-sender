class BaseNotification:
    """Base notification class"""

    def __init__(self, channel, message):
        self.channel = channel
        self.message = message

    def send_notification(self):
        self.apply_channel_specifics()
        print(f"Message: {self.message}. Sent via: {self.channel}")

    def apply_channel_specifics(self): ...
