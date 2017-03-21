from django.db import models

# Create your models here.
class Course(models.Model):
    #auto_now_add when a record is added its set to the timezone from settings
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
        
class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #blank true allows it to be optional
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title