from django.core.urlresolvers import reverse
from django.db import models


class Subject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject)
    content = models.TextField(blank=True, default='')
    
    class Meta:
        ordering = ['order',]
    
    def __str__(self):
        return self.title


# class Report_Text(Report_Step):
#     content = models.TextField(blank=True, default='')
    
#     def get_absolute_url(self):
#         return reverse('reports:report_text', kwargs={
#                 'subject_pk': self.subject_id,
#                 'report_step_pk': self.id
#             })


# class Report(Report_Step):
#     conclusion = models.TextField()
    
#     def get_absolute_url(self):
#         return reverse('reports:report', kwargs={
#                 'subject_course_pk': self.course_id,
#                 'report_step_pk': self.id
#             })