from django.contrib import admin
from .models import AnalysisResult, Company, EmployeeAnswer

class AnalysisResultAdmin(admin.ModelAdmin):
  list_display = ['probability']

class CompanyAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'numberOfEmployees', 'sector', 'isTech')

class EmployeeAnswerAdmin(admin.ModelAdmin):
  list_display = (
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
    'medicalLeave'
  )

# Register your models here.
admin.site.register(AnalysisResult, AnalysisResultAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(EmployeeAnswer, EmployeeAnswerAdmin)
