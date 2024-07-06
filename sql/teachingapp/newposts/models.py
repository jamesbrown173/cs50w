from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=64)
    dob = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

    def __str__(self):
        return f"Username: {self.username}, DOB: {self.dob}, Location: {self.location}"


class Post(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="Users")
    postcontent = models.CharField(max_length=64)
    posttitle = models.CharField(max_length=64)
    rating = models.IntegerField()

    def __str__(self):
        return f"Username: {self.username} Title: {self.posttitle} Content: {self.postcontent}"
