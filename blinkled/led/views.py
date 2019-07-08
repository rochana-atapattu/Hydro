from django.shortcuts import render
import RPi.GPIO as GPIO

PUMP_PIN = 36

def turnOn(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(PUMP_PIN, GPIO.LOW)
    return HttpResponse('On')


def turnOff(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    return HttpResponse('Off')

