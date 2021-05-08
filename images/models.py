from django.db import models


class UploadImage(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/", default=None)

    def __str__(self):
        return self.title
