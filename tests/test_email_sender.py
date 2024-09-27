import unittest
from email_sender import EmailSender

class TestEmailSender(unittest.TestCase):
    def test_send_email(self):
        email_sender = EmailSender("test@example.com", "Test Subject", "Test Message")
        try:
            email_sender.send_email()
            success = True
        except Exception as e:
            success = False
            print(f"Error: {e}")
        self.assertTrue(success, "Email sending failed!")

if __name__ == "__main__":
    unittest.main()
