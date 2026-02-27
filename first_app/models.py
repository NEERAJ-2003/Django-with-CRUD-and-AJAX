from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    pub_time = models.TimeField()
    files = models.FileField(upload_to='files/')
    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

class Person(models.Model):
    person_name = models.CharField(max_length=100)
    person_email = models.EmailField()
    skills = models.ManyToManyField(Skill, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.person_name


# for email
class Emp(models.Model):
    e_id = models.CharField(max_length=20)
    e_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    hr_status = models.CharField(max_length=50)
    admin_status = models.CharField(max_length=50)

    def __str__(self):
        return self.e_name