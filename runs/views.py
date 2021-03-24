from django.shortcuts import render, redirect
from django.views import View
from runs.models import RunDetails, RunType, Registration
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

''' Here will be landing page view with all possible runs'''
class RunsListView(View):
    def get(self, request):
        runs = RunDetails.objects.all()
        return render(request, 'landing.html', {'runs_list':runs})



''' Here should add user rights that only admin could see that page and add runs'''
class AddRunView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        return render(request, 'add_runs.html')

    def post(self, request):
        run_name = request.POST.get("name")
        run_city = request.POST.get("city")
        run_distance = request.POST.get("distance")
        run_date = request.POST.get("run_date")
        active_registration = request.POST.get("registration")
        if int(run_distance) >= 100:
            rt = RunType(distance=int(run_distance), type = 'ultra')
            rt.save()

        if int(run_distance) == 42:
            rt = RunType(distance=int(run_distance), type='marathon')
            rt.save()

        if int(run_distance) == 21:
            rt = RunType(distance=int(run_distance), type='half-marathon')
            rt.save()

            rd = RunDetails(run_name=run_name,run_city=run_city,
                                  run_distance=run_distance, active_registration=active_registration,
                                  run_type = rt, run_date=run_date)
            rd.save()
        return redirect("run_list")


class RunDetailsView(View):
    def get(self, request, run_id):
        detailsRun = RunDetails.objects.get(id=run_id)
        return render(request, "details_about_run.html", {'run': detailsRun})


'''
Here user will enroll to run and after successful registration return to list of his own runs
pick up user runs by id
relation many to one
table has data of enrolled people

'''
class RegistrationView(View):
    def get(self, request, run_id):
        specified_run = RunDetails.objects.get(id=run_id)
        return render(request, "enroll_form.html")

    def post(self, request, run_id):
        specified_run = RunDetails.objects.get(id=run_id)
        runner_name = request.POST.get("runner_name")
        runner_surname = request.POST.get("runner_surname")
        runner_date_of_birth= request.POST.get("runner_date_of_birth")
        runner_email = request.POST.get("runner_email")
        runner_phone = request.POST.get("runner_phone")

        # registration_payment= request.POST.get("registration_payment")
        Registration.objects.create(runner_name=runner_name, runner_surname=runner_surname,runner_date_of_birth=runner_date_of_birth,
                                 runner_email=runner_email, runner_phone=runner_phone)




        return redirect("run_list")



'''
# here should be data of enrolled person runs
Here you pick up user by id and may get his personal data + from Registration + from RunsDetails'''
class UserPrivateDataView(View):

    def get(self, request, user_id):
        run_list= Registration.objects.all()
        user_enroll = run_list.get(pk=user_id)

        return render(request, 'user_account.html', {'run_list':run_list})



class ContactsView(View):
    def get(self, request):
        contactsList = Registration.objects.all()
        return render(request, 'dropmsg.html')


