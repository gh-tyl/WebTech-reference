from django.db import models

# Create your models here.
class ReferenceData(models.Model):
    title = models.TextField(null=True)
    url = models.TextField(null=True)

    def __str__(self):
        return u"{0}:{1}...".format(self.id, self.title[:], self.url[:])
