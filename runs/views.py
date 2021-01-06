from django.shortcuts import render, redirect
from django.views import View
from runs.models import Main, RunEnroll

# Create your views here.
class RunsListView(View):
    def get(self, request):
        runs = Main.objects.all()
        return render(request, 'landing.html', {'runs_list':runs})

class AddRunView(View):
    def get(self, request):
        return render(request, 'add_run_view.html')

    def post(selfself, request):
        name = request.POST.get("name")
        city = request.POST.get("city")
        distance = request.POST.get("distance")
        registration = request.POST.get("registration")
        term = request.POST.get("term")
        Main.objects.create(name=name,city=city,distance=distance, registration=registration, term=term)
        return redirect("run_list")

class RunDetailsView(View):
    def get(self, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        return render(request, "details_about_run.html", {'run': specified_run})

class RunDelete(View):
    def get(selfself, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        specified_run.delete()
        return redirect("run_list")

class RunEdit(View):
    def get(self, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        return render(request, "modify_run.html")

    def post(self, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        name = request.POST.get("name")
        city = request.POST.get("city")
        distance = request.POST.get("distance")
        registration = request.POST.get("registration")
        term = request.POST.get("term")
        Main.objects.create(name=name,city=city,distance=distance, registration=registration, term=term)
        return redirect("run_list")


'''
Here user will enroll to run and after successful registration return to list of his own runs
pick up user runs by id
relation many to one

'''
class RunEnrollView(View):
    def get(self, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        return render(request, "enroll_form.html")

    def post(self, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        name_pr = request.POST.get("name_pr")
        surname_pr = request.POST.get("surname_pr")
        date_of_birth_pr= request.POST.get("date_of_birth_pr")
        email = request.POST.get("name_pr")
        gender = request.POST.get("surname_pr")
        number= request.POST.get("date_of_birth_pr")
        RunEnroll.objects.create(run_enroll_id = specified_run, name_pr=name_pr, surname_pr=surname_pr,date_of_birth_pr=date_of_birth_pr,
                                 email=email, gender=gender,number=number)

        return redirect("run_list")




