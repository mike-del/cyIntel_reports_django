from django.shortcuts import render

from . import models

def subject_list(request):
	'''Lists all available subjects'''
	subject_list = models.Subject.objects.all()
	return render(request, 'reports/subject_list.html',
		{'subject_list': subject_list})

def subject_reports(request, pk):
	'''Show all or a selected date range of
	reports for a given subject'''
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')
	if end_date:
		reports = models.Report.objects.filter(
		date__range=[start_date, end_date], subject=pk)
	else:
		reports = models.Report.objects.filter(subject=pk)
	return render(request, 'reports/subject_reports.html',
		{'reports': reports})
