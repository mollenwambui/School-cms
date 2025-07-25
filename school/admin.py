from django.contrib import admin
from .models import Student,Teacher,Subject,Classroom,Grade,StudentAttendance,TeacherAttendance
# Register your models here.


# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(Subject)
# admin.site.register(Classroom)
# admin.site.register(Classroom)

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'admission_number', 'stream', 'level')
    list_filter=('stream', 'grade')
    search_fields=('student_first_name', 'student_last_name',)

class TeacherAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'staff_id', 'subject')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code')
    search_fields = ('subject_name', 'subject_code')


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'score', 'date_recorded')  # ✅ use commas *outside* quotes
    search_fields = ('student__name',)  # ✅ assuming Student model has a `name` field


from .models import StudentAttendance, TeacherAttendance

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'present')
    list_filter = ('date', 'present')
    search_fields = ('student__first_name', 'student__last_name')

@admin.register(TeacherAttendance)
class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'date', 'present')
    list_filter = ('date', 'present')
    search_fields = ('teacher__first_name', 'teacher__last_name')



admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Classroom,ClassroomAdmin)
admin.site.register(Grade,GradeAdmin)