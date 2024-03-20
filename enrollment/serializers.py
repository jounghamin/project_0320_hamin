from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'
        extra_kwargs = {
            "lecture": {"read_only": True},
            "student": {"read_only": True}
            }

        # fields = ['title']