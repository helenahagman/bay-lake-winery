from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    subscribe_to_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.name
