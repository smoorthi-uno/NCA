from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    is_staffs = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    experience = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class Victim(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True)
    disease_type = models.CharField(max_length=50)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)


class Activity(models.Model):
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='activities')
    volunteer = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING, related_name='activities')
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='activities')
    victim = models.ForeignKey(Victim, on_delete=models.DO_NOTHING, related_name='activities')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    created_date = models.DateField(default=timezone.now)
    updated_date = models.DateField(default=timezone.now)
    notes = models.CharField(max_length=200, blank=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)
