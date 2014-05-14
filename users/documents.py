from django.utils.translation import ugettext_lazy as _
from mongoengine.django.auth import make_password, check_password
from mongoengine.django.utils import datetime_now
from mongoengine.document import Document
from mongoengine.fields import StringField, EmailField, DateTimeField


class User(Document):
    """A User document that aims to mirror most of the API specified by Django
    at http://docs.djangoproject.com/en/dev/topics/auth/#users
    """
    email = EmailField(verbose_name=_('e-mail address'))
    display_name = StringField(max_length=255, verbose_name=_('first name'))
    password = StringField(
        max_length=128,
        verbose_name=_('password'),
        help_text=_(
            "Use '[algo]$[iterations]$[salt]$[hexdigest]' or use the"
            " <a href=\"password/\">change password form</a>."))
    last_login = DateTimeField(
        default=datetime_now,
        verbose_name=_('last login'))
    date_joined = DateTimeField(
        default=datetime_now,
        verbose_name=_('date joined'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    meta = {
        'allow_inheritance': True,
        'indexes': [
            {'fields': ['email'], 'unique': True, 'sparse': True}
        ]
    }

    def __unicode__(self):
        return self.display_name

    def get_full_name(self):
        return self.display_name

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def set_password(self, raw_password):
        """Sets the user's password - always use this rather than directly
        assigning to :attr:`~mongoengine.django.auth.User.password` as the
        password is hashed before storage.
        """
        self.password = make_password(raw_password)
        self.save()
        return self

    def check_password(self, raw_password):
        """Checks the user's password against a provided password - always use
        this rather than directly comparing to
        :attr:`~mongoengine.django.auth.User.password` as the password is
        hashed before storage.
        """
        return check_password(raw_password, self.password)

    @classmethod
    def normalize_email(cls, email):

        try:
            email_name, domain_part = email.strip().split('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])

        return email

    @classmethod
    def create_user(cls, email, display_name, password):
        """Create (and save) a new user with the given email address, display
        name and password.
        """
        now = datetime_now()
        email = cls.normalize_email(email)
        user = cls(email=email, display_name=display_name, date_joined=now)
        user.set_password(password)
        user.save()
        return user

    def email_user(self, subject, message, from_email=None):
        "Sends an e-mail to this User."
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, [self.email])
