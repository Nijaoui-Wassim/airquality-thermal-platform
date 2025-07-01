from django.urls import path
from .views import post_measurement
from .views import dashboard_view, export_data_view

urlpatterns = [
    path('api/post-measurement/', post_measurement, name='post_measurement'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('export/', export_data_view, name='export_data'),
]
