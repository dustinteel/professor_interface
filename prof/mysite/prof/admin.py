from django.contrib import admin
from django import forms

# Register your models here.

from .models import Student, Class, AttendanceRecord, StudentCsvModel

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

class StudentAdmin(admin.ModelAdmin):
    exclude = ('Professor',)
    
    def has_change_permission(self, request, obj=None):
        has_student_permission = super(StudentAdmin, self).has_change_permission(request, obj)
        if not has_student_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.Professor.id:
            return False
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Student.objects.all()
        return Student.objects.filter(Professor=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.Professor = request.user
        
        obj.save()  

class AttendanceRecordAdmin(admin.ModelAdmin):
    
    def has_change_permission(self, request, obj=None):
        has_record_permission = super(AttendanceRecordAdmin, self).has_change_permission(request, obj)
        if not has_record_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.Associated_Class.Professor.id:
            return False
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return AttendanceRecord.objects.all()
        return AttendanceRecord.objects.filter(Associated_Class__Professor=request.user)
        
        obj.save()  

admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)


