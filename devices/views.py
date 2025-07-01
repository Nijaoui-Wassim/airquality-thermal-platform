from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AQThermalUnit, Room, Measurement
from .serializers import MeasurementSerializer
from django.shortcuts import render
from .models import Measurement, Room, AQThermalUnit
import csv
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_measurement(request):
    device_id = request.data.get('unit')
    room_id = request.data.get('room')

    # Check device and room existence and association
    try:
        unit = AQThermalUnit.objects.get(id=device_id)
        if room_id and unit.room.id != int(room_id):
            return Response({'error': 'Device not assigned to this room.'}, status=status.HTTP_400_BAD_REQUEST)
    except AQThermalUnit.DoesNotExist:
        return Response({'error': 'Device not found.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = MeasurementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def dashboard_view(request):
    # Filter options
    room_id = request.GET.get('room')
    device_id = request.GET.get('device')

    # Get filtered measurements
    measurements = Measurement.objects.all().order_by('-timestamp')
    if room_id and room_id != "all":
        measurements = measurements.filter(unit__room_id=room_id)
    if device_id and device_id != "all":
        measurements = measurements.filter(unit_id=device_id)

    # For charts, take last N entries or group by timestamp
    plot_data = measurements.order_by('-timestamp')[:100][::-1]  # last 100, oldest first

    rooms = Room.objects.all()
    devices = AQThermalUnit.objects.all()

    context = {
        'measurements': measurements[:50],  # Show 50 latest
        'rooms': rooms,
        'devices': devices,
        'plot_data': plot_data,
        'selected_room': room_id or "all",
        'selected_device': device_id or "all",
    }
    return render(request, 'devices/dashboard.html', context)

def export_data_view(request):
    rooms = Room.objects.all()
    devices = AQThermalUnit.objects.all()
    selected_rooms = request.GET.getlist('rooms')
    selected_devices = request.GET.getlist('devices')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    export = request.GET.get('export')

    measurements = Measurement.objects.all().select_related('unit', 'unit__room')

    if selected_rooms:
        measurements = measurements.filter(unit__room__id__in=selected_rooms)
    if selected_devices:
        measurements = measurements.filter(unit__id__in=selected_devices)
    if start_date:
        measurements = measurements.filter(timestamp__gte=start_date)
    if end_date:
        measurements = measurements.filter(timestamp__lte=end_date)

    if export == "csv":
        # CSV Export
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="measurements.csv"'
        writer = csv.writer(response)
        writer.writerow([
            'Time', 'Room', 'Device', 'PM10', 'PM2.5', 'PM1', 'Temperature', 'Humidity', 'CO2', 'VOC', 'AQ Value'
        ])
        for m in measurements.order_by('-timestamp'):
            writer.writerow([
                m.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                m.unit.room.name,
                m.unit.serial_number,
                m.pm_10_value,
                m.pm_2_5_value,
                m.pm_1_value,
                m.temperature,
                m.humidity,
                m.co2_value,
                m.voc_value,
                m.aq_value,
            ])
        return response

    return render(request, "devices/export.html", {
        "rooms": rooms,
        "devices": devices,
        "selected_rooms": [int(i) for i in selected_rooms],
        "selected_devices": [int(i) for i in selected_devices],
        "start_date": start_date,
        "end_date": end_date
    })