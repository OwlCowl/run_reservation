from django.db import models


# Create your models here.
# ''' AllRuns - All accessable runs '''
class AllRuns(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    active_registration = models.BooleanField(default=True)
    term = models.DateField()


    def get_detail_url(self):
        return f"/AllRuns/{self.id}"



# ''' Details about specific run '''
class RunDetails(models.Model):
    run_name = models.CharField(max_length=64)
    run_distance = models.IntegerField()
    run_date = models.DateField()
    run_participants = models.IntegerField()


# ''' Registration - Base with info about participants and payments '''
class Registration(models.Model):
    name_pr = models.CharField(max_length=25)
    surname_pr = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    phone = models.IntegerField()
    payment = models.BooleanField(default=False)
    enrolledPeople = models.ManyToManyField(AllRuns)


    def get_detail_url(self):
        return f"/Registration/{self.id}"




# ''' Something trial'''
class RunReservation(models.Model):
    date = models.DateField()
    comment = models.TextField(null=True)


# ''' User private account base: all about his booked runs '''
class UserPrivateData(models.Model):
    run_name = models.CharField(max_length=25)
    run_city = models.CharField(max_length=25)
    run_date = models.DateField()
    run_distance = models.DecimalField(max_digits=5, decimal_places=2)
    run_payment = models.BooleanField(default = False)

# ''' Payment - Base with payment info'''
class Payment(models.Model):
    status = models.BooleanField(default=False)
    payment = models.ForeignKey(UserPrivateData, on_delete = models.CASCADE, default=False)


# ''' AllRuns - All accessable runs'''
# ''' UserPrivateData - User private account base: all about his booked runs'''
# ''' RunDetails - Details about specific run'''
# ''' Registration - Base with info about participants and payments'''
# ''' Payment - Base with payment info'''
''' Participants where we store all users who enrolled'''
''' Contacts '''








