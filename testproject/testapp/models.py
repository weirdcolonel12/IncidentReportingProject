from django.db import models

# Create your models here.

LOCATION_CHOICES= (
    ('corporate headoffice', 'Corporate Headoffice'),
    ('main area', 'Main Area'),
    ('far away', 'Far Away'),
    )

SEVERITY_CHOICES = (
    ('severe' , 'Severe'),
    ('moderate' , 'Moderate'),
    ('minor' , 'Minor'),
)


class Subincidenttype(models.Model):
    types=models.CharField(max_length=264)

    def __str__(self):
        return self.types



class ReportingModel(models.Model):
    location = models.CharField(max_length=64, choices=LOCATION_CHOICES)
    incidentdescription = models.TextField()
    date = models.DateTimeField()
    incidentlocation = models.TextField(default='', blank=True)
    internalseverity = models.CharField(max_length=64, choices=SEVERITY_CHOICES)
    suspectedcause = models.TextField(default='', blank=True)
    immediateactionstaken = models.TextField(default='', blank=True)
    subincidenttypes = models.ManyToManyField(Subincidenttype, blank=True, verbose_name="subincident types")
    reportedby = models.CharField(max_length=264)

    def __str__(self):
        return self.reportedby
