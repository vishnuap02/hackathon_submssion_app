from datetime import datetime

from django.db import models
# from django.urls import reverse
# from rest_framework.reverse import reverse as api_reverse

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    mail_id = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return f'user: {self.name}>'

    class Meta:
        ordering = ('name','mail_id','password')
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Hackathon(models.Model):
    image = models.ImageField(upload_to='Image/', default='img.jpg', blank=True)
    file = models.FileField(upload_to='files/', default='file.txt', blank=True)
    link = models.CharField(max_length=250, blank=True)
    PRIORITY_CHOICES = (
        (0, 'Image'),
        (1, 'File'),
        (2, 'Link')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hackathons')
    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    background_image = models.ImageField(upload_to='backgrounds/', default='bg.jpg')
    hackathon_image = models.ImageField(upload_to='hackathons/', default='hk.jpg')
    submission_type = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'hackathon: {self.title}>'

    class Meta:
        verbose_name = 'hackathon'
        verbose_name_plural = 'hackathons'


class Register(models.Model):
    sl_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, auto_created=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    title = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, auto_created=True)
    is_favourite = models.BooleanField(default=False)
    github_link = models.CharField(max_length=250, blank=True)
    other_link = models.CharField(max_length=250, blank=True)
    sub_date = models.DateTimeField()

    # 3 choices from  hackathon model
    image = models.ImageField(upload_to='Image/', default='img.jpg', blank=True)
    file = models.FileField(upload_to='files/', default='file.txt', blank=True)
    link = models.CharField(max_length=250, blank=True)
    def save(self, *args, **kwargs):
        # Access fields in the child model
        image_value = self.image
        file_value = self.file
        link_value = self.link

        # Store values in the parent model
        self.hackathon.image = image_value
        self.hackathon.file = file_value
        self.hackathon.link = link_value

        # Save the parent model
        self.hackathon.save()

        super(Submission, self).save(*args, **kwargs)
    def __str__(self):
        return self.title


