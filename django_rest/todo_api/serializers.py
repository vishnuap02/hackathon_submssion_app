from django.utils import timezone
from rest_framework import serializers

from .models import Hackathon,User,Register,Submission




class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Hackathon
        fields = ("id","user","title", "description", "background_image", "hackathon_image", "submission_type", "start_datetime", "end_datetime", "reward_prize")
        # , "image", "file", "link"

        read_only_fields = ('id',)


    def validate_deadline(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value

class UserSerializer(serializers.ModelSerializer):
    # hackathon_created = HackathonSerializer(many=True)
    class Meta:
        lookup_field = 'id'
        model = User
        fields = ('id', 'name','mail_id','password','hackathon',)
        read_only_fields = ('id', 'hackathon')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Register
        fields = ('id','sl_number','user','hackathon','is_available')
        read_only_fields = ('id','sl_number')

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Submission
        fields = ("id","title","user","summary","hackathon","image", "file", "link","github_link","other_link","is_favourite","sub_date")
        read_only_fields = ('id','sl_number')


