# coding: utf-8
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from annoying.decorators import ajax_request

from .models import Job
from .forms import JobForm


class JobsHomeView(FormMixin, ListView):
    """ Render Job Opportunities home page. """
    model = Job
    queryset = Job.objects.filter(is_active=True, is_approved=True)
    form = JobForm
    template_name = 'jobs_home.html'


@ajax_request
def new_job(request):
    """ Add a new job"""
    if request.POST:
        form = form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return {'success': True}
        else:
            return {'success': False, 'errors': form.errors.keys()}
    return {'success': False, 'error': 'Request not valid'}


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'
