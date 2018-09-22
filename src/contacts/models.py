from django.db import models


class ContactGroup(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64, null=True)
    building_number = models.IntegerField(null=True)
    flat_number = models.IntegerField(null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(ContactGroup)


class PhoneNumber(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=64)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    address = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)