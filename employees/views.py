from django.shortcuts import render, redirect
from .models import Employee


def register(request):
    if request.method == "POST":
        employee_id = request.POST["employee_id"]
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        department = request.POST["department"]
        designation = request.POST["designation"]
        salary = request.POST["salary"]
        joining_date = request.POST["joining_date"]
        address = request.POST["address"]

        profile_photo = request.FILES.get("profile_photo")

        Employee.objects.create(
            employee_id=employee_id,
            full_name=full_name,
            email=email,
            phone=phone,
            department=department,
            designation=designation,
            salary=salary,
            joining_date=joining_date,
            address=address,
            profile_photo=profile_photo
        )

        return redirect("register")

    return render(request, "employees/register.html")