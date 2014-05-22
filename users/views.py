from actionviews.base import TemplateView
from actionviews.decorators import action_decorator
from django.contrib.auth.decorators import login_required
from mongoengine.django.shortcuts import get_document_or_404

from .documents import User


class UserView(TemplateView):

    @action_decorator(login_required)
    def do_profile(self:''):
        return {'profile': self.request.user}

    def do_user(self:'', user):
        return {'profile': get_document_or_404(User, pk=user)}
