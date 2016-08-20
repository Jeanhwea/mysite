from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s%s' % (self.last_name, self.first_name)
    full_name = property(_get_full_name)

    def __str__(self):              # __unicode__ on Python 2
        return self.full_name

@python_2_unicode_compatible
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60, help_text='Your name')
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


@python_2_unicode_compatible
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateField()
    invite_reason = models.CharField(max_length=64)


