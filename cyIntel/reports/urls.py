from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.subject_list, name='subject_list'),
    # url(r'(?P<subject_pk>\d+)/t(?P<report_step_pk>\d+)/$',
    # 	views.report_text_detail, name='report_text'),
    url(r'(?P<pk>\d+)/$',views.report_detail, name='report_detail'),
    # url(r'(?P<pk>\d+)/$', views.subject_detail, name='subject_detail'),
    
]