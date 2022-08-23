from dataclasses import field
from rest_framework import serializers
from .models import AnalysisResult, EmployeeAnswer

class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = ['probability']

class EmployeeAnswerSerializer(serializers.ModelSerializer):
  
  companyId = serializers.IntegerField()
  age = serializers.IntegerField()
  gender = serializers.CharField()
  hasFamilyHistory = serializers.BooleanField()
  hasEmployeeHistory = serializers.BooleanField()
  hasReceivedTreatment = serializers.BooleanField()
  hasHealthcareCoverage = serializers.BooleanField()
  hasBenefits = serializers.BooleanField()
  wasDiagnosed = serializers.BooleanField()
  openToDiscussionWorkspace = serializers.BooleanField()
  talkToSupervisor = serializers.CharField()
  talkToCoworker = serializers.CharField()
  race = serializers.CharField()
  medicalLeave = serializers.CharField()
  
  class Meta:
    model = EmployeeAnswer
    fields = [
      'companyId',
      'age',
      'gender',
      'hasFamilyHistory',
      'hasEmployeeHistory',
      'hasReceivedTreatment',
      'hasHealthcareCoverage',
      'hasBenefits',
      'wasDiagnosed',
      'openToDiscussWorkspace',
      'talkToSupervisor',
      'talkToCoworker',
      'race',
      'medicalLeave',
      'interestOrPleasure',
      'downDepressedHopeless',
      'troubleFallingAsleep',
      'tiredLittleEnergy',
      'poorAppetiteOvereating',
      'feelingBad',
      'troubleConcentrating',
      'slowOrFast',
      'betterOfDead',
      'nervousAnxious',
      'cantStopWorrying',
      'worryingToMuch',
      'troubleRelaxing',
      'easilyAnnoyed',
      'feelingAfraid'
    ]