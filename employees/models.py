from django.db import models
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    address = models.TextField()
    profile_photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name