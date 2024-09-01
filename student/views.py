from django.shortcuts import render
from student.forms import StudentRegistrationForm
from django.shortcuts import redirect


# Create your views here.
def register_student(request):

    if request.method == "Post": 
            
        form = StudentRegistrationForm(request.Post)
        if form.is_valid():
            form.save()
            redirect("register_Student")
    else:
        form = StudentRegistrationForm()        
    return render(request, "student/register_student.html", {"form":form})
