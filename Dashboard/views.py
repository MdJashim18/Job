from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Job_Listings.models import JobListing
from Job_Details.models import Application
from Job_Listings.serializers import JobListingSerializer
from Job_Details.serializers import ApplicationSerializer

class EmployerDashboardViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if not request.user.is_employer:
            return Response({"detail": "You are not authorized to view this dashboard."}, status=403)

        jobs = JobListing.objects.filter(employer=request.user)
        serializer = JobListingSerializer(jobs, many=True)
        return Response({"posted_jobs": serializer.data})

class JobSeekerDashboardViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if not request.user.is_job_seeker:
            return Response({"detail": "You are not authorized to view this dashboard."}, status=403)

        applications = Application.objects.filter(applicant=request.user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response({"applications": serializer.data})
