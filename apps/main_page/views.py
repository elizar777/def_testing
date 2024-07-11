from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (EmployeeSerializer,
                          CounterSerializer)
from .models import (Employee,
                     Counter)


class MainPageView(APIView):
    def get(self, request, *args, **kwargs):
        #TODO   Вот тут будут другие данные главной страницы
        data = CounterSerializer(data=Counter, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutUsView(APIView):
    def get(self, request, *args, **kwargs):
        #TODO   Тут тоже возможно будут другие данные, по типу История и Устав
        data = EmployeeSerializer(data=Employee, many=True).data[:4]
        return Response(data=data, status=status.HTTP_200_OK)


class DirectorateListView(ListAPIView):
    queryset = Employee.objects.filter(category='directorate')
    serializer_class = EmployeeSerializer


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.filter(category='employees')
    serializer_class = EmployeeSerializer


class AcademicCouncilListView(ListAPIView):
    queryset = Employee.objects.filter(category='academic_council')
    serializer_class = EmployeeSerializer


