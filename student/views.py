from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# def home(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password = request.POST['password']
#         photo = request.FILES.get('photo')
#         checkbox = request.POST['checkbox']
#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False
#         student = Student(name=name, email=email, phone=phone, password=password, checkbox=checkbox, photo=photo)
#         student.save()
#         print(photo)
#         return render(request,'student/home.html')

#     return render(request, 'student/home.html')

#Class-based views

class StudentLists(ListView):
    model = Student
    template_name ='student/student_list.html'
    context_object_name ='students'

class CreateStudent(CreateView):
    form_class = StudentForm
    model = Student
    template_name ='student/index.html'
    success_url = reverse_lazy('student_list')
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Student added successfully.")
        return super().form_valid(form)
    
class UpdateStudent(UpdateView):
    form_class = StudentForm
    model = Student
    template_name ='student/index.html'
    success_url = reverse_lazy('student_list')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Student updated successfully.")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True  # Add a new key-value pair to the context dictionary
        return context
    
class DeleteStudent(DeleteView):
    model = Student
    template_name ='student/delete_student.html'
    success_url = reverse_lazy('student_list')
    pk_url_kwarg = 'id'
    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, "Student deleted successfully.")
        return super().delete(request, *args, **kwargs)


#End of Class-based views

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Student added successfully.")
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'student/index.html', {'form': form,})

def list_view(request):
    students = Student.objects.all()
    return render(request,'student/student_list.html', {'students': students})

def individual_information(request, id):
    student = Student.objects.get(id=id)
    context = {
       'student': student
    }
    return render(request, 'student/individual_student.html', context)


def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Student Updated successfully.")
            return redirect('/')
    return render(request, 'student/index.html', {'form': form, 'update': True})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.WARNING, "Student deleted successfully.")
    return redirect('/')
