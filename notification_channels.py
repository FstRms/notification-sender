from base_notification import BaseNotification


class EmailNotification(BaseNotification):
    """Class to send notifications via email"""

    def __init__(self, message):
        super().__init__("Email", message)

    def apply_channel_specifics(self):
        print("Initialize email provider")
        print("Parse message to required format")


class PushNotification(BaseNotification):
    """Class to send notifications via PUSH"""

    def __init__(self, message):
        super().__init__("Push", message)

    def apply_channel_specifics(self):
        print("Communicate with Push provider")
        print("Load message")


class SMSNotification(BaseNotification):
    """Class to send SMS notifications"""

    def __init__(self, message):
        super().__init__("SMS", message)

    def apply_channel_specifics(self):
        print("Communicating with carrier")
        print("Preparing message")


class WhatsAppNotification(BaseNotification):
    """Class to send notifications via whatsapp"""

    def __init__(self, message):
        super().__init__("WhatsApp", message)

    def apply_channel_specifics(self):
        print("Checking if phone has funds")
        print("Cleaning emojis")


ACTIVE_CHANNELS = [
    SMSNotification,
    EmailNotification,
    PushNotification,
    WhatsAppNotification,
]
