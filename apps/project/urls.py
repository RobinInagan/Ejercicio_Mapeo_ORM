from django.urls import path
from .views import ProjectAPIView

urlpatterns =[
    path('projects/',ProjectAPIView.as_view())
]