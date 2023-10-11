from .models import remainder
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = remainder.objects.get(username=username)
            if user.password == password:
                return user
        except remainder.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return remainder.objects.get(pk=user_id)
        except remainder.DoesNotExist:
            return None
