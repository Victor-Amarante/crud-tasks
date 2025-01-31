from django.db import models


class Tasks(models.Model):
  status_choice = [
    ('pending', 'Pending'),
    ('working', 'Working'),
    ('done', 'Done'),
  ]
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=False)
  status = models.CharField(max_length=255, choices=status_choice, default='pending')
  due_date = models.DateField(blank=True, null=True)
  
  class Meta:
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'
  
  def __str__(self):
    return self.title
