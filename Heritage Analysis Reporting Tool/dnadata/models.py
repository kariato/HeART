from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class FamilyManager(models.Manager):
    def families_for_user(self, user):
        return super(FamilyManager, self).get_queryset().filter(Q(user_id=user.id))


class Family(models.Model):
    user = models.ForeignKey(User, related_name="DNAMatches_user")
    familyName = models.CharField(max_length=300)

    objects = FamilyManager()

    def __str__(self):
        return "{0}".format(self.familyName)

class DNAKitManger(models.Manager):
    def kitsForFamily(self, family):
        return super(DNAKitManger, self).get_queryset().filter(Q(family_id=family.id))

class DNAKit(models.Model):
    family =  models.ForeignKey(Family)
    resultSet = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    objects = DNAKitManger()
    def __str__(self):
        return "{0} ({1})".format(self.name,self.resultSet)

class DNAKitUpload(models.Model):
    kit = models.ForeignKey(DNAKit)
    filename = models.CharField(max_length=300, blank=True)
    uploadType = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=300,  blank=True)
    log = models.CharField(max_length=300, blank=True)
    uploaded = models.DateTimeField('date created', default=datetime.now)
    files = models.FileField( blank=True)

class DNAMatch(models.Model):
    resultSet = models.ForeignKey(DNAKit)
    fullName = models.CharField(max_length=300)
    firstName = models.CharField(max_length=300)
    middleName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    matchDate = models.DateField()
    relationshipRange = models.CharField(max_length=300)
    suggestedRelationship = models.CharField(max_length=300)
    sharedCM = models.FloatField()
    longestBlock = models.FloatField()
    knownRelationship = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    ancestralSurnames = models.CharField(max_length=3000)

    def __str__(self):
        return "{0}({1})".format(self.fullName,self.suggestedRelationship)

# Create your models here.
class DNASegment(models.Model):
    matchname = models.ForeignKey(DNAMatch)
    chromosome = models.IntegerField()
    startLocation = models.IntegerField()
    endLocation = models.IntegerField()
    centimorgans = models.FloatField()
    matchingSnps = models.FloatField()

    def __str__(self):
        return "{0}:{1}-{2}".format(self.chromosome,self.startLocation,self.endLocation)

class ExampleModel(models.Model):
    model_file = models.FileField(upload_to = 'file_folder/', default = 'file_folder/None/no-file.csv')


