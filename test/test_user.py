import unittest
from faker import Faker
from src.user import User

class UserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale='es')
        

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        print(user.name, user.email)