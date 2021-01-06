from django.db import models


# Create your models here.
'''
    Here will be the list with whole runs
'''
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

# class DistanceOptions(models.Model):
#     small = models.IntegerField()
#     medium = models.IntegerField()
#     marathon = models.IntegerField()
#     ultra = models.IntegerField()

# class Payment(models.Model):
#     price_s = models.DecimalField(max_digits=5, decimal_places=2)
#     price_m = models.DecimalField(max_digits=5, decimal_places=2)
#     price_l = models.DecimalField(max_digits=5, decimal_places=2)
#     price_u = models.DecimalField(max_digits=5, decimal_places=2)




class RunEnroll(models.Model):
    run_enroll_id = models.ForeignKey(Main, on_delete=models.CASCADE)
    name_pr = models.CharField(max_length=25)
    surname_pr = models.CharField(max_length=25)
    date_of_birth_pr = models.DateField()
    email = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    number = models.IntegerField()

    def get_detail_url(self):
        return f"/runenroll/{self.id}"


