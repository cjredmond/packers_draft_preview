from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    packers = models.BooleanField()
    picture = models.FileField(null=True, blank=True)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return 'http://pccweb.ca/standrewsdresden/files/2016/03/Question-mark.png'
