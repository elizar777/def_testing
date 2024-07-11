from rest_framework import serializers
from .models import (Employee,
                     Counter)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = 'image name position'.split()


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = 'contacted discharged operated born'.split()