from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student


# главная страница, выводит три студента
def index(request):
    context = {
        'objects_list': Student.objects.all(),
        'title': 'Главная',
    }
    return render(request, 'main/index.html', context)

#импортировать надо django.views.generic.ListView
class StudentListView(ListView):
    model = Student
    extra_context = {
        'title': 'Список студентов'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs) #метод на получение данных.родительский метод super
        context_data['title'] = context_data['object'] #object ключевое слово
        return context_data
# class StudentListView, StudentDetailView - реализован один студент и список студентов - read (CRUD)

# создаем студента
class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',) #поля из models class Student
    success_url = reverse_lazy('main:students_list') #отвечает куда вернуться после создания товара

# редактирование студента
class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:students_list')

# удаление студента
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:students_list')

#Деактивирование студента
def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk) # специальная ф-ия 404, модель ищет по ключу необходимый обьект
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:student_list', args=[student_item.pk]))
# from django.shortcuts import get_object_or_404 импорт.

# подменю студента карточка
# def student(request, pk):
#     student_item = Student.objects.get(pk=pk)
#     context = {
#         'objects': student_item,
#         'title': student_item,
#     }
#     return render(request, 'main/student.html', context)


# контакты
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'User {name} with email{email} send message: {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)
