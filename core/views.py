from actionviews import TemplateView

from .documents import Issue
from .forms import IssueForm


class IssueView(TemplateView):

    def do_list(self: ''):
        return {'issues': Issue.objects.all()}

    def do_create(self):
        request = self.request

        if request.method == 'POST':
            form = IssueForm(request.POST)

            if form.is_valid():
                issue = Issue(**form.cleaned_data)
                issue.save()

        else:
            form = IssueForm()

        return {'form': form}
