from django.urls import path
from .views import (AboutUsView,
                    DirectorateListView,
                    EmployeeListView,
                    AcademicCouncilListView,
                    MainPageView)



urlpatterns = [
    path('main_page', MainPageView.as_view()),
    path('about_us', AboutUsView.as_view()),
    path('directorate_list', DirectorateListView.as_view()),
    path('employees_list', EmployeeListView.as_view()),
    path('academic_council_list', AcademicCouncilListView.as_view())
]