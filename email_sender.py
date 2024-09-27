class EmailSender:
    def __init__(self, recipient, subject, message):
        self.recipient = recipient
        self.subject = subject
        self.message = message

    # Simulate sending an email
    def send_email(self):
        print(f"Sending email to: {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"Message:\n{self.message}")

# Example usage
email_sender = EmailSender("test@example.com", "Weather Report", "Please find the weather report attached.")
email_sender.send_email()
