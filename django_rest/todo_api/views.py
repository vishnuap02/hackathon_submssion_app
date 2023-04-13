# from django.db.models import Q
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import views
from django.http import JsonResponse
from rest_framework.response import Response

from .models import Hackathon,User,Register,Submission
from .serializers import (HackathonSerializer,UserSerializer,RegisterSerializer,SubmissionSerializer)



######### USER VIEW #########
class UserView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

######### Hackathon VIEW #########
class HackathonView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

######### REGISTER VIEW #########
class RegisterView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

######### REGISTER VIEW #########
class SubmissionView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

######### LIST ALL HACKATHONS #########
class ListView(views.APIView):
    def get(self, request):
        # Fetch all Hackathon objects from the database
        hackathons = Hackathon.objects.all()

        # Convert the queryset to a list of dictionaries
        hackathons_data = []
        for hackathon in hackathons:
            hackathons_data.append({
                'id': hackathon.id,
                'title': hackathon.title,
                'creater':hackathon.user.name,
                'description': hackathon.description,
                'start-date':hackathon.start_datetime,
                'end-date':hackathon.end_datetime,
                # 'bg-image':hackathon.background_image
                # Add more fields as needed
            })

        # Return a JSON response
        return JsonResponse({'hackathons': hackathons_data})

######### LIST SUBMISSION ##########
class ListSubmissionView(views.APIView):
    def get(self, request):
        # Fetch all Hackathon objects from the database
        submissions = Submission.objects.all()

        # Convert the queryset to a list of dictionaries
        submission_data = []
        for submission in submissions:
            submission_data.append({
                'id': submission.id,
                'title': submission.title,
                'summary':submission.summary,
                'sub_date':submission.sub_date,
                # 'bg-image':hackathon.background_image
                # Add more fields as needed
            })

        # Return a JSON response
        return JsonResponse({'submission': submission_data})
