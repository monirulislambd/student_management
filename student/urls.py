from django.urls import path
from . import views

urlpatterns = [
    #path('', views.list_view, name='student_list'), #for function-based views
    path('', views.StudentLists.as_view(), name='student_list'), #for class-based views
    path('home/', views.home, name='home'), #for function-based views
    path('home/', views.CreateStudent.as_view(), name='home'), #for class-based views
    path('individual_information/<int:id>', views.individual_information, name='individual_information'),
    # path('update_student/<int:id>', views.update_student, name='update_student'), #for function-based views
    path('update_student/<int:id>', views.UpdateStudent.as_view(), name='update_student'), #for class-based views
    # path('delete_student/<int:id>', views.delete_student, name='delete_student'), #for function-based views
    path('delete_student/<int:id>', views.DeleteStudent.as_view(), name='delete_student'), #for class-based views
]
