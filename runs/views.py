from django.shortcuts import render, redirect
from django.views import View

from runs.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages #import messages
from runs.models import RunDetails, RunType, Registration
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("run_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("user_account")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("run_list")



# class LoginView(View):
#     def get(self, request):
#         return render(request, "loginpage.html")
#
#     def post(self, request):
#         username = request.POST.get('username')
#         useremail = request.POST.get('useremail')
#         userpass = request.POST.get('password')
#         adminUser = User.objects.create_superuser('yana',
#                                              '2947468@gmail.com', '123')
#         participant = User.objects.create_superuser('alex',
#                                              '123456@gmail.com', '123')



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

''


        return redirect("run_list")



'''
# here should be data of enrolled person runs
Here you pick up user by id and may get his personal data + from Registration + from RunsDetails'''
class UserPrivateDataView(View):

    def get(self, request, user_id):
        run_list= Registration.objects.all()
        # user_enroll = run_list.get(pk=user_id)

        return render(request, 'user_account.html', {'run_list':run_list})



class ContactsView(View):
    def get(self, request):
        contactsList = Registration.objects.all()
        return render(request, 'dropmsg.html')


