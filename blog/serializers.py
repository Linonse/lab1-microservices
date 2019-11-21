from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.save()

        return instance

    def validate_title(self, value):

        return value
