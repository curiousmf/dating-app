from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    
    
    
    STATUS = (
        ('st', 'Учусь'),
        ('wk', 'Работаю'),
        ('sd', 'Туплю'),
        ('mm', 'Мамкин миллиардер'),
        ('mp', 'Мамин бродяга, папин симпотяга'),

    )
    status = models.CharField(max_length=50, choices=STATUS)
    salary = models.IntegerField(blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.surname}'
    
    def get_absolute_url(self):
        return f"/{self.pk}"