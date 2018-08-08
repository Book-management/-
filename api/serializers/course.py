from rest_framework import serializers


from app01 import models

class Course(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

