from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.subject_list, name='subject_list'),
    url(r'(?P<pk>\d+)/',views.subject_reports, name='subject_reports'),
    
]	