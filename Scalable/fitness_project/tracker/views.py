from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')
def bmi_page(request):
    return render(request, 'bmi.html')

def log_activity_page(request):
    return render(request, 'activity_log.html')

def progress_chart(request):
    return render(request, 'progress_chart.html')
import random

def get_workout_suggestion():
    workouts = [
        {"name": "30 mins HIIT", "calories": 300},
        {"name": "45 mins Brisk Walking", "calories": 200},
        {"name": "60 mins Cycling", "calories": 400},
        {"name": "20 mins Jump Rope", "calories": 250},
        {"name": "40 mins Swimming", "calories": 350},
        {"name": "30 mins Yoga", "calories": 150},
    ]
    return random.choice(workouts)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "User registered successfully"})
    return Response(serializer.errors)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def calculate_bmi(request):
    weight = float(request.data.get('weight'))
    height = float(request.data.get('height'))
    bmi = weight / ((height / 100) ** 2)
    return Response({'bmi': round(bmi, 2)})

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def log_activity(request):
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'status': 'Activity logged'})
    return Response(serializer.errors)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_progress(request):
    activities = Activity.objects.filter(user=request.user)
    total_calories = sum(a.calories_burned for a in activities)
    serializer = ActivitySerializer(activities, many=True)
    return Response({'total_calories': total_calories, 'activities': serializer.data})
