from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.first_name)
        instance.author = validate_data.get('author', instance.last_name)
        instance.save()

        return instance

    def validate_title(self, value):

        return value
