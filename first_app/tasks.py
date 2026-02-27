from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import os


@shared_task
def send_employee_mail(e_id, e_name, dept, mobile, hr_status, admin_status):

    html_content = f"""
    <h2>Details of {e_name}</h2>
    <table border="1" cellpadding="10" cellspacing="0">
        <tr><td><b>Employee ID</b></td><td>{e_id}</td></tr>
        <tr><td><b>Employee Name</b></td><td>{e_name}</td></tr>
        <tr><td><b>Department Name</b></td><td>{dept}</td></tr>
        <tr><td><b>Mobile Number</b></td><td>{mobile}</td></tr>
        <tr><td><b>HR Status</b></td><td>{hr_status}</td></tr>
        <tr><td><b>Admin Status</b></td><td>{admin_status}</td></tr>
    </table>
    """

    email = EmailMultiAlternatives(
        subject="Employee Details",
        body="Employee Details",
        from_email=settings.EMAIL_HOST_USER,
        to=["neeraj.xzy@gmail.com"],
    )

    email.attach_alternative(html_content, "text/html")

    image_path = os.path.join(settings.BASE_DIR, 'first_app', 'static', 'img', 'pic.jpeg')

    with open(image_path, "rb") as img:
        email.attach("pic.jpeg", img.read(), "image/jpeg")

    email.send()