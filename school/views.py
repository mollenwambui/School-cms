from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Student, Teacher, Classroom, StudentAttendance, TeacherAttendance
from datetime import datetime

def mark_attendance(request):
    classrooms = Classroom.objects.all()
    teachers = Teacher.objects.all()
    selected_classroom = request.GET.get('classroom')
    students = Student.objects.filter(stream=selected_classroom) if selected_classroom else []

    if request.method == 'POST':
        date = request.POST.get('date') or timezone.now().date()

        # Mark student attendance
        for student in students:
            present = request.POST.get(f"student_{student.id}") == "on"
            StudentAttendance.objects.update_or_create(
                student=student, date=date,
                defaults={'present': present}
            )

        # Mark teacher attendance
        for teacher in teachers:
            present = request.POST.get(f"teacher_{teacher.id}") == "on"
            TeacherAttendance.objects.update_or_create(
                teacher=teacher, date=date,
                defaults={'present': present}
            )

        return redirect('view_attendance')

    context = {
        'classrooms': classrooms,
        'students': students,
        'teachers': teachers,
        'selected_classroom': selected_classroom,
        'today': timezone.now().date()
    }
    return render(request, 'attendance/mark_attendance.html', context)

def view_attendance(request):
    date_filter = request.GET.get('date')
    classroom_filter = request.GET.get('classroom')

    attendance_records = StudentAttendance.objects.all().select_related('student')
    if date_filter:
        attendance_records = attendance_records.filter(date=date_filter)
    if classroom_filter:
        attendance_records = attendance_records.filter(student__stream=classroom_filter)

    teacher_records = TeacherAttendance.objects.all().select_related('teacher')
    if date_filter:
        teacher_records = teacher_records.filter(date=date_filter)

    context = {
        'attendance_records': attendance_records,
        'teacher_records': teacher_records,
        'classrooms': Classroom.objects.all(),
    }
    return render(request, 'attendance/view_attendance.html', context)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
