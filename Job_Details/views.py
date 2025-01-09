from rest_framework import viewsets, status
from .models import Application
from .serializers import ApplicationSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import action
from rest_framework.response import Response
from employee.models import Employee

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        try:
            employer = self.request.user.employee  # Access the Employee instance
        except Employee.DoesNotExist:
            raise ValueError("The logged-in user is not associated with an employer.")

        serializer.save(employer=employer)

        # Send email to applicant
        application = serializer.instance
        applicant_subject = "Application Received"
        applicant_message = render_to_string('application_received.html', {'application': application})
        applicant_plain_message = strip_tags(applicant_message)
        send_mail(
            subject=applicant_subject,
            message=applicant_plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[application.email],
            html_message=applicant_message,
        )
