from django.urls import path
from apps.structure.views import BlockListAPIView, BlockRetrieveAPIView, DepartmentListAPIView, DepartmentRetrieveAPIView



urlpatterns = [
    path('block_list/', BlockListAPIView.as_view(), name='block_list'),
    path('block_list/<int:pk>/', BlockRetrieveAPIView.as_view(), name='block_list_detail'),
    path('department_list/', DepartmentListAPIView.as_view(), name='department_list'),
    path('department_list/<int:pk>/', DepartmentRetrieveAPIView.as_view(), name='department_list_detail'),
]
