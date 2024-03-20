from rest_framework import serializers
from .models import Lecture

class LectureSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = '__all__'
        extra_kwargs = {"instructor": {"read_only": True}}

        # fields = ['title']