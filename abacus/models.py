from django.db import models

# Create your models here.

# Teacher model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "1. Teachers"

    def __str__(self):
        return self.name

# Course Category model
class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "2. Course Categories"

    def __str__(self):
        return self.name

# Course model
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "3. Courses"

    def __str__(self):
        return self.title

# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=100)
    interested_categories = models.TextField()
    
    class Meta:
        verbose_name_plural = "4. Students"
    
    def __str__(self):
        return self.name
