import re
import base64
import io
import time
from time import sleep
from django.shortcuts import render, redirect, render_to_response
import jsonify
import json, urllib
from django.http import JsonResponse
import numpy as np
import pandas
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# dashboard
def index(request):
    return render(request, 'index.html')

# modules
def modules(request):
    return render(request, 'modules.html')

# render page that renders views for all of the API requests (arithmetic || core.py)

# tutor_portals
    # allow user to navigate for tutors and filter based on category
    # prompt for category specification
    # display active tutor users
    # store created users in SQL
    # must store user accounts, performance_metrics, status (tutor, student, both), exam_results

# Build and implement confidence-based algorithm, for every 1 instance of completion {onSubmit} => {launch popup that collects user confidence ranked via 0-5}
# Scrape all problem sets for K-12 level mathematics that are high-signal, convert questions into problem sets (0/12), similar to KhanAcademy
# Ask for user’s time availability to schedule learning, and also allow the user to focus on weaker problem types after assessing their baseline.
# Weaker problem types will be prioritized in rank order based on results from popups
# Scale of distribution of matches for users (within classroom, then district, then region, then country)

# view decorators: https://docs.djangoproject.com/en/3.0/topics/http/decorators/

