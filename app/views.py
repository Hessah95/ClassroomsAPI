from django.shortcuts import render
from classes.models import Classroom

from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, CreateAPIView,
	RetrieveUpdateAPIView, DestroyAPIView,
	)

from .serializer import (
	ClassroomSerializer, ClassroomDetailSerializer,
	ClassroomCreateSerializer
	)
# Create your views here.


class APIList (ListAPIView) :
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class APIDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class APICreate (CreateAPIView) :
	serializer_class = ClassroomCreateSerializer

	def perform_create (self, serializer) :
		serializer.save(teacher=self.request.user)

class APIUpdate(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class APIDelete(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'