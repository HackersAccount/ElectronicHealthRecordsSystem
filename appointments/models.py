from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Slot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=50)
    minutesDuration = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.start} to {self.end}"


class Reason(models.Model):
    code = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.code


class Actor(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.name


class Appointment(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=50)
    appointment_type = models.CharField(max_length=100)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    supporting_info = models.CharField(max_length=255)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    based_on = GenericForeignKey("content_type", "object_id")
    description = models.TextField(null=True, blank=True)
    priority = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.start} - {self.appointment_type}"


class Participant(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.actor} - {self.status}"
