from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AQThermalUnit(models.Model):
    serial_number = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return f"Unit {self.serial_number} in {self.room.name}"

class Measurement(models.Model):
    unit = models.ForeignKey(AQThermalUnit, on_delete=models.CASCADE, related_name='measurements')
    timestamp = models.DateTimeField(auto_now_add=True)
    pm_10_value = models.FloatField()
    pm_2_5_value = models.FloatField()
    pm_1_value = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    co2_value = models.FloatField()
    voc_value = models.FloatField()
    aq_value = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thermal_image = models.ImageField(upload_to='thermal/', blank=True, null=True)

    def __str__(self):
        return f"Measurement from {self.unit.serial_number} at {self.timestamp}"
