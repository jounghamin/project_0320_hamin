from rest_framework import serializers
from .models import Instructor


class InstructorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = '__all__'
        # fields = ['title']