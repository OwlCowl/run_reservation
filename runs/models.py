from django.db import models


# Create your models here.


''' Here we have information about types of runs'''
class RunType(models.Model):
    distance = models.IntegerField()
    type = models.CharField(max_length=20, default='ultra') #make it a selectors

'''  All accessable runs from landing page. 
        User also should be able to enroll to run from landing page. 
        Ralation OneToMany to RunType'''
class RunDetails(models.Model):
    run_name = models.CharField(max_length=64)
    run_city = models.CharField(max_length=25)
    run_distance = models.IntegerField()
    run_date = models.DateField()
    run_type = models.ForeignKey(RunType, on_delete = models.CASCADE)
    active_registration = models.BooleanField(default=True)

    def get_detail_url(self):
        return f"/RunDetails/{self.id}"


''' Registration - Base with info about participants and payments.
    Separate registrration form. User wouldn't be required to create an account to be able to enroll to run.
    ManyToMany relation to RunDetails'''
class Registration(models.Model):
    runner_name = models.CharField(max_length=25)
    runner_surname = models.CharField(max_length=25)
    runner_date_of_birth = models.DateField()
    runner_email = models.CharField(max_length=25)
    runner_phone = models.IntegerField()
    registration_payment = models.BooleanField(default=False)
    run_connection = models.ManyToManyField(RunDetails)

    def get_detail_url(self):
        return f"/Registration/{self.id}"

''' User private account base: all about user runs, payments '''
class UserPrivateData(models.Model):
    user_data = models.ForeignKey(Registration, on_delete = models.CASCADE, default=False)
    user_runs = models.ForeignKey(RunDetails, on_delete = models.CASCADE, default=False)



class Contacts(models.Model):
    runner = models.ForeignKey(UserPrivateData, on_delete = models.CASCADE)
    EC = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    telephone = models.IntegerField()




# ''' RunDetails - All accessable runs'''
# ''' UserPrivateData - User private account base: all about his booked runs'''
# ''' RunDetails - Details about specific run'''
# ''' Registration - Base with info about participants and payments'''
# ''' Payment - Base with payment info'''
''' Participants where we store all users who enrolled'''
''' Contacts '''








