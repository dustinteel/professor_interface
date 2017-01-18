from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Class
from django.contrib.auth.decorators import user_passes_test, login_required
#from .forms import ChangeAttendanceForm

# This view is for the index page that is the first page loaded.
def index(request):
    return HttpResponse("Welcome to the Attendance App Home Page!")

# This view shows the details of a class to the professor

def user_id_check(user):
    return user.groups.filter(name='Professors').exists() or user.is_superuser is True

@login_required
@user_passes_test(user_id_check, login_url='../../login', redirect_field_name=None)
def classDetails(request, class_id):
    if request.user.id != Class.objects.get(id=class_id).getProfessor() and request.user.is_superuser != True:
        return HttpResponse("Access denied. You are not the professor for this class.");
    return HttpResponse("You're viewing class %s with ID %s and owner %d." % (Class.objects.get(id=class_id).getName(), class_id, Class.objects.get(id=class_id).getProfessor()))

#This is the view which controls the form to update attendance.
#def get_attendance(request):
#    className = Class.objects.get(id=1).getName()
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from #the request
#        form = ChangeAttendanceForm(request.user, request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            # process the data in form.cleaned_data as required
#            # ...
#            # redirect to a new URL:
#            return HttpResponseRedirect('/class/')
#    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = ChangeAttendanceForm(request.user)
#    
#    return render(request, 'changeattendance.html', {'form':form, #'className':className})
  




