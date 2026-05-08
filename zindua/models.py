from django.db import models

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Programme(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in months")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    
    lead_instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='programmes')

    def __str__(self):
        return self.name.title()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    
    enrolled_programmes = models.ManyToManyField(Programme, related_name='students')

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"