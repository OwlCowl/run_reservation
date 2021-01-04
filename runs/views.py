from django.shortcuts import render, redirect
from django.views import View
from runs.models import Main

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

class RunEnroll(View):
    def get(self, request, run_id):
        specified_run = Main.objects.get(id=run_id)
        return render(request, "enroll_form.html")

    def post(self, request, run_id):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        date_of_birth= request.POST.get("date_of_birth")
        distance= request.POST.get("distance")
        team= request.POST.get("team")
        t_shirt= request.POST.get("t-shirt")
        Enroll.objects.create(name=name, surname=surname,date_of_birth=date_of_birth, distance=distance, team=team,t_shirt=t_shirt)

        return render(request, "finish_enroll.html")




