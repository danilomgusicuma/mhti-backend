from multiprocessing.spawn import prepare
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .preprocessor import Preprocessor
from .serializers import AnalysisResultSerializer, EmployeeAnswerSerializer
from .models import AnalysisResult, Company, EmployeeAnswer
from keras.models import load_model
import io
import numpy as np
from datetime import date

# Create your views here.
@csrf_exempt
def analysis_result_view(request):
    response = "fail"
    preprocessor = Preprocessor()

    if request.method == 'POST':
      stream = io.BytesIO(request.body)
      data = JSONParser().parse(stream)
      serializer = EmployeeAnswerSerializer(data=data)
      if serializer.is_valid():
        employeeAnswer = serializer.validated_data
        company = Company.objects.all().filter(id = employeeAnswer["companyId"]).get()

        # saving the answers 
        serializer.save()
        model = load_model("george")
        input_array = [[
          preprocessor.age(employeeAnswer["birthDate"]),
          preprocessor.familyHistory(employeeAnswer["hasFamilyHistory"]),
          preprocessor.employeeHistory(employeeAnswer["hasEmployeeHistory"]),
          preprocessor.isTechCompany(company.isTech),
          preprocessor.hasBenefits(employeeAnswer["hasBenefits"]),
          preprocessor.isFemale(employeeAnswer["gender"]),
          preprocessor.isMale(employeeAnswer["gender"]),
          preprocessor.otherGender(employeeAnswer["gender"]),
          preprocessor.isEnterprise(company.numberOfEmployees),
          preprocessor.isLargeEnterprise(company.numberOfEmployees),
          preprocessor.isMediumEnterprise(company.numberOfEmployees),
          preprocessor.isMicroEnterprise(company.numberOfEmployees),
          preprocessor.isSmallEnterprise(company.numberOfEmployees)
        ]]
        input = np.array(input_array)
        prediction = model.predict(input).tolist()[0][1]
        response = JsonResponse({'probabilityToHaveMentalDisorder':prediction})
    return HttpResponse(response)