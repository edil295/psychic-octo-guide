from django.shortcuts import render
from codify.models import Course, Student
import json
from django.core import serializers
from django.http import JsonResponse


def course_list_api(request):
    courses = Course.objects.all()
    serialized_courses = serializers.serialize('json', courses)
    return JsonResponse(serialized_courses, safe=False)