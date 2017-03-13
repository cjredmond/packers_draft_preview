from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    picture = models.FileField()
    take = models.TextField()
    pick = models.CharField(max_length=10)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return 'http://pccweb.ca/standrewsdresden/files/2016/03/Question-mark.png'
