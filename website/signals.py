# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Record

@receiver(post_save, sender=Record)
def send_customer_email(sender, instance, created, **kwargs):
    if created:  # Only send email when a new record is created
        subject = "Welcome to Our CRM"
        message = f"Hi {instance.first_name},\n\nThank you for joining our CRM!\n\nYour details:\nName: {instance.first_name} {instance.last_name}\nEmail: {instance.email}\nPhone: {instance.phone}\n\nRegards,\nYour Company"
        recipient_list = [instance.email]

        send_mail(
            subject,
            message,
            'your_email@gmail.com',  # Replace with your email
            recipient_list,
            fail_silently=False,
        )
