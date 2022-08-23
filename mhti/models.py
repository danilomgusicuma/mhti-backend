from django.db import models

# Create your models here.

class AnalysisResult(models.Model):
    probability = models.IntegerField()

    def _str_(self):
        return self.probability

class Company(models.Model):
    @property
    def id(self):
        return self.id
    name = models.TextField()
    numberOfEmployees = models.IntegerField()
    sector = models.TextField()
    isTech = models.BooleanField()
    
    def _str_(self):
      return self.name

    def generateEmployeeAnswer(self):
      return EmployeeAnswer(
        companyNumberOfEmployees = self.numberOfEmployees,
        companySector = self.sector,
        isTechCompany = self.isTech
      )

class EmployeeAnswer(models.Model):
    companyId = models.IntegerField(null = True)
    age = models.IntegerField(null = True)
    gender = models.CharField(null = True, max_length=100)
    hasFamilyHistory = models.BooleanField(null = True)
    hasEmployeeHistory = models.BooleanField(null = True)
    hasReceivedTreatment = models.BooleanField(null = True)
    hasHealthcareCoverage = models.BooleanField(null = True)
    hasBenefits = models.BooleanField(null = True)
    wasDiagnosed = models.BooleanField(null = True)
    openToDiscussionWorkspace = models.BooleanField(null = True)
    talkToSupervisor = models.CharField(null = True, max_length=100)
    talkToCoworker = models.CharField(null = True, max_length=100)
    race = models.CharField(null = True, max_length=100)
    medicalLeave = models.CharField(null = True, max_length=100)
    interestOrPleasure = models.CharField(null = True, max_length=100)
    downDepressedHopeless = models.CharField(null = True, max_length=100)
    troubleFallingAsleep = models.CharField(null = True, max_length=100)
    tiredLittleEnergy = models.CharField(null = True, max_length=100)
    poorAppetiteOvereating = models.CharField(null = True, max_length=100)
    feelingBad = models.CharField(null = True, max_length=100)
    troubleConcentrating = models.CharField(null = True, max_length=100)
    slowOrFast = models.CharField(null = True, max_length=100)
    betterOfDead = models.CharField(null = True, max_length=100)
    nervousAnxious = models.CharField(null = True, max_length=100)
    cantStopWorrying = models.CharField(null = True, max_length=100)
    worryingToMuch = models.CharField(null = True, max_length=100)
    troubleRelaxing = models.CharField(null = True, max_length=100)
    easilyAnnoyed = models.CharField(null = True, max_length=100)
    feelingAfraid = models.CharField(null = True, max_length=100)