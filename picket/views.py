from actionviews import ActionResponse, TemplateView
from actionviews.decorators import action_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .documents import Issue
from .forms import IssueForm
from mongoengine.django.shortcuts import get_document_or_404


class IssueView(TemplateView):

    def do_list(self:'', page:r'\d+'=1):
        return {'issues': Issue.objects.all()}

    @action_decorator(login_required)
    def do_create(self):
        request = self.request

        if request.method == 'POST':
            form = IssueForm(request.POST)

            if form.is_valid():
                issue = Issue(
                    subject=form.cleaned_data['subject'],
                    creator=request.user,
                    comments=[form.cleaned_data['text']])
                issue.save()
                raise ActionResponse(redirect('list'))

        else:
            form = IssueForm()

        return {'form': form}

    def do_issue(self, n:r'\d+'):
        return {'issue': get_document_or_404(Issue, id=int(n))}
