from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

from employee.models import Employee
from .models import Application
from .serializers import ApplicationSerializer

# Set up logging
logger = logging.getLogger(__name__)

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        
        user = self.request.user

        if not user or user.is_anonymous:
            raise ValidationError({"error": "Authentication required"})

        employer = Employee.objects.filter(user=user).first()
        if not employer:
            raise ValidationError({"error": "Employer not found"})

        application = serializer.save(employer=employer)

        if not application.email:
            raise ValidationError({"error": "Applicant email is required"})

        self.send_application_email(application)

    def send_application_email(self, application):
        
        try:
            subject = "Application Received"
            html_message = render_to_string('application_received.html', {'application': application})
            plain_message = strip_tags(html_message)

            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[application.email],
                html_message=html_message,
            )
            logger.info(f"Application email sent successfully to {application.email}")
        except Exception as e:
            logger.error(f"Error sending application email: {e}")

    def get_queryset(self):
        
        user = self.request.user

        if not user.is_authenticated:
            return Application.objects.none()

        employer = Employee.objects.filter(user=user).first()
        if employer:
            return Application.objects.filter(employer=employer)

        return Application.objects.none()
