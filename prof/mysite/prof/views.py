from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Class
from django.contrib.auth.decorators import user_passes_test, login_required
import csv
import codecs
#from .forms import ChangeAttendanceForm

# This view is for the index page that is the first page loaded.
def index(request):
    return render(request, "index.html", locals())

# This view shows the details of a class to the professor

def user_id_check(user):
    return user.groups.filter(name='Professors').exists() or user.is_superuser is True

#@login_required
@user_passes_test(user_id_check, login_url='/prof/login', redirect_field_name=None)
def classDetails(request, class_id):
    if request.user.id != Class.objects.get(id=class_id).getProfessor() and request.user.is_superuser != True:
        return HttpResponse("Access denied. You are not the professor for this class.");
    return HttpResponse("You're viewing class %s with ID %s and owner %d." % (Class.objects.get(id=class_id).getName(), class_id, Class.objects.get(id=class_id).getProfessor()))

#@login_required
@user_passes_test(user_id_check, login_url='/prof/login/')
def uploadstudents(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

    return render(request, "uploadstudents.html", locals())
  




