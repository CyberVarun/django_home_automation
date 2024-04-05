from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
import RPi.GPIO as GPIO

LED1 = 17
LED2 = 27
LED3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# Create your views here.
def state_check(led):
    if GPIO.input(led) == 1:
        return True
    else:
        return False
    
def logout(request):
    return redirect('login')

def dashboard(request):
    return render(request, "dashboard.html" , {'led_1': state_check(LED1), 'led_2': state_check(LED2), 'led_3': state_check(LED3)})

def toggleled(request, led, state): 
    if led == 1:
        led = LED1
    elif led == 2:
        led = LED2
    elif led == 3:
        led = LED3

    if state == 1:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)
        
    return redirect('dashboard')  

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user exists
        user = authenticate(request, username=username, password=password)
        
        # If the user exists
        if user is not None:
            return redirect('dashboard')
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create a new user object
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Save the user object to the database
        user.save()
        
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, "signup.html")