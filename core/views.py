from actionviews import TemplateView
from .documents import Issue


class IssueView(TemplateView):

    def do_list(self: ''):
        return {'issues': Issue.objects.all()}
