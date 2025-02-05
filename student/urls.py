from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentLists.as_view(), name='student_list'), 
    path('home/', views.CreateStudent.as_view(), name='home'), 
    path('individual_information/<int:id>', views.individual_information, name='individual_information'),
    path('update_student/<int:id>', views.UpdateStudent.as_view(), name='update_student'), 
    path('delete_student/<int:id>', views.DeleteStudent.as_view(), name='delete_student'),
