from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.structure.models import Block, Department
from apps.structure.serializer import BlockSerializer, DepartmentSerializer

class BlockListAPIView(ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class BlockRetrieveAPIView(RetrieveAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer 
    
class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveAPIView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer 
    
