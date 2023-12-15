from django.db import models
from django.utils import timezone


class Contact(models.Model):
    email = models.EmailField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    message = models.TextField(blank=False)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = "Contact Form Submission"

