from django.db import models


# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    registration = models.BooleanField(default=True)
    term = models.DateField()

    def get_detail_url(self):
        return f"/main/{self.id}"

class RunReservation(models.Model):
    run_id = models.IntegerField()
    date = models.DateField()
    comment = models.TextField(null=True)

class DistanceOptions(models.Model):
    small = models.IntegerField()
    medium = models.IntegerField()
    marathon = models.IntegerField()
    ultra = models.IntegerField()

class Payment(models.Model):
    price_s = models.DecimalField(max_digits=5, decimal_places=2)
    price_m = models.DecimalField(max_digits=5, decimal_places=2)
    price_l = models.DecimalField(max_digits=5, decimal_places=2)
    price_u = models.DecimalField(max_digits=5, decimal_places=2)

class Awards(models.Model):
    place = models.IntegerField()
    price = models.IntegerField()
