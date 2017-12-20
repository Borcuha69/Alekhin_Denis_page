from django.shortcuts import render
from .forms import SubscriberForm


def landing(requests):
    return render(requests, 'landing/landing.html', locals())