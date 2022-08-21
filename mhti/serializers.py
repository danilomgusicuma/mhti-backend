from dataclasses import field
from rest_framework import serializers
from .models import AnalysisResult, EmployeeAnswer

class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = ['probability']

class EmployeeAnswerSerializer(serializers.ModelSerializer):
  
  companyId = serializers.IntegerField()
  birthDate = serializers.DateField()
  gender = serializers.CharField()
  hasFamilyHistory = serializers.BooleanField()
  hasEmployeeHistory = serializers.BooleanField()
  hasHealthcareCoverage = serializers.BooleanField()
  hasBenefits = serializers.BooleanField()
  wasDiagnosed = serializers.BooleanField()
  
  class Meta:
    model = EmployeeAnswer
    fields = [
      'companyId',
      'birthDate',
      'gender',
      'hasFamilyHistory',
      'hasEmployeeHistory',
      'hasHealthcareCoverage',
      'hasBenefits',
      'wasDiagnosed'
    ]