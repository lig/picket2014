from .documents import User


class Backend(object):

    def authenticate(self, username=None, email=None, password=None):
        email = User.normalize_email(username or email)
        user = User.objects(email=email.lower()).first()

        if user and password and user.check_password(password):
            return user

    def get_user(self, user_id): 
        return User.objects.with_id(user_id) 
