from actionviews.base import TemplateView
from actionviews.decorators import action_decorator
from django.contrib.auth.decorators import login_required


class UserView(TemplateView):

    @action_decorator(login_required)
    def do_profile(self:''):
        return {'profile': self.request.user}
