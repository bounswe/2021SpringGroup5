from django.contrib.auth.tokens import PasswordResetTokenGenerator
import hashlib
from datetime import datetime
from .models import User


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, User, timestamp):

        date_time_string = datetime.fromtimestamp(timestamp)
        string_to_hash = str(User.mail) + str(date_time_string)
        encoded = string_to_hash.encode()
        return hashlib.sha256(encoded)


generate_token = TokenGenerator()