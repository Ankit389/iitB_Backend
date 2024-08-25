from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseInstanceViewSet(viewsets.ModelViewSet):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        queryset = CourseInstance.objects.all()
        year = self.request.query_params.get('year')
        semester = self.request.query_params.get('semester')
        if year and semester:
            queryset = queryset.filter(year=year, semester=semester)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        course_id = kwargs.get('course_id')
        year = kwargs.get('year')
        semester = kwargs.get('semester')
        instance = get_object_or_404(CourseInstance, course_id=course_id, year=year, semester=semester)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        course_id = kwargs.get('course_id')
        year = kwargs.get('year')
        semester = kwargs.get('semester')
        instance = get_object_or_404(CourseInstance, course_id=course_id, year=year, semester=semester)
        self.perform_destroy(instance)
        return Response(status=204)
    
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Course Management API")