from users.models import User


class UserAuthenticate(object):

    def emailauthenticate(self, username=None, password=None):
        if username.isdigit():
            username = None
        try:
            user = User.objects.get(email=self.email)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def phoneauthenticate(self, username=None, password=None):
        if not username.isdigit():
            username = None
        try:
            user = User.objects.get(phone=self.email)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
