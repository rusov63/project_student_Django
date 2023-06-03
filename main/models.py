from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)
