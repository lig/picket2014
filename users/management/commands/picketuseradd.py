from django.core.management.base import BaseCommand

from ...documents import User


class Command(BaseCommand):
    args = '<email> <display_name> <password>'
    help = 'Creates picket admin user'

    def handle(self, *args, **options):
        email, display_name, password = args
        user = User.create_user(email, display_name, password)
        print('User with id {} created.'.format(user.id))
