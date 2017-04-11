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
    date = models.DateField(auto_now=False)
    order = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject)
    content = models.TextField(blank=True, default='')
    
    class Meta:
        ordering = ['order',]
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reports:subject_reports', kwargs={'pk':self.pk})
