from notification_channels import ACTIVE_CHANNELS


class NotificationSender:
    """Sends Notifications according to setted channels"""

    def __init__(self, message):
        self.message = message
        self.active_channels = ACTIVE_CHANNELS

    def run(self):
        for channel in self.active_channels:
            notification_channel = channel(self.message)
            notification_channel.send_notification()


if __name__ == "__main__":
    test_message = input("Tell me what to notify?")
    sender = NotificationSender(test_message)
    sender.run()
