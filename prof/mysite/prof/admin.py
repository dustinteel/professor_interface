from django.contrib import admin
from django import forms

# Register your models here.

from .models import Student, Class, AttendanceRecord

class ClassAdmin(admin.ModelAdmin):
    exclude = ('Professor',)
    
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(ClassAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.Professor.id:
            return False
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Class.objects.all()
        return Class.objects.filter(Professor=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.Professor = request.user
        obj.save()
        obj.save_m2m()

class AttendanceRecordAdminForm(forms.ModelForm):
  class Meta:
    model = AttendanceRecord
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(AttendanceRecordAdminForm, self).__init__(*args, **kwargs)
    self.fields['Absent_Students'].queryset = Student.objects.filter(class_list__id=1) #self.instance.get_associated_class_name())
    self.fields['Present_Students'].queryset = Student.objects.filter(class_list__id=1)

class AttendanceRecordAdmin(admin.ModelAdmin):
  form = AttendanceRecordAdminForm
  filter_horizontal = ('Absent_Students', 'Present_Students',)
  

admin.site.register(Class, ClassAdmin)
admin.site.register(Student)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)


