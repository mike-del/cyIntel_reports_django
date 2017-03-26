from itertools import chain

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import models


def subject_list(request):
    subject_list = models.Subject.objects.all()
    return render(request, 'reports/subject_list.html',
    	{'subject_list': subject_list})


def report_detail(request, pk):
	reports = models.Report.objects.filter(subject=pk)
	return render(request, 'reports/report_detail.html', {'reports': reports})