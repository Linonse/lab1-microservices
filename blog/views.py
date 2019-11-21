from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer


class PersonListView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serialized = PersonSerializer(persons, many=True)

        return Response(serialized.data)

    def post(self, request):
        serialized = PersonSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)

        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailView(APIView):
    def get(self, request, pk):
        person = get_object_or_404(Person.objects.all(), pk=pk)
        serialized = PersonSerializer(person)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        person = get_object_or_404(Person.objects.all(), pk=pk)

        serializer = PersonSerializer(instance=person, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = get_object_or_404(Person.objects.all(), pk=pk)
        person.delete()

        return Response({"message": "Person with id '{}' succesfully deleted".format(pk)},
                        status=status.HTTP_204_NO_CONTENT)
