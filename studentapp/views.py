from django.shortcuts import render
from studentapp.models import Student
# Create your views here.
def home_view(request):
    students = Student.objects.all().order_by('marks')
    return render(request, 'studentapp/index.html',{'students': students})