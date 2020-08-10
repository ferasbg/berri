# base 
import re
import base64
import io

# time
import time
from time import sleep
import datetime

# handling data
import pandas
import pandas as pd
import matplotlib
import numpy as np

# rendering
from django.shortcuts import render, redirect, render_to_response

# json(dependencies)
import jsonify
import json, urllib
from django.http import JsonResponse


# landing page
def index(request):
    return render(request, 'index.html')

# modules
def modules(request):
    return render(request, 'modules.html')

# modules/training (gateway for problem_sets)
def training(request):
    if request.method == 'GET':
        # hit studycounts API for each GET request for specific page 
        full_url = 'https://studycounts.com/api/v1/arithmetic/simple.json'
        # need to simply pass in a dict to the headers parameter
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOGQ3ZjkyZTM4MGNlZDM5YmFmZWE4MmY2NjAwZmUwMGQxNDQ4OTUxNzk5MWVmNGE2NGU1Y2IwOWRkYTJiMWVhNDZhYTI5YjY4NGE2MmVjZjUiLCJpYXQiOjE1OTY5MDk1NTUsIm5iZiI6MTU5NjkwOTU1NSwiZXhwIjoxNjI4NDQ1NTU1LCJzdWIiOiIxMDUyIiwic2NvcGVzIjpbXX0.CpqfyY-6_a9hTDOkoaUyONtnToLuFMEkOyhf800eP_HFUyLOjvHtRNQIJKhurmR4r8l2JsFvZ-ekSE7qAl56HD2KilNYnXQ5Gb7R1fGOiJbD8bf_BckhxDZne7jl4gz-Lf2mQ60JRC8NlXXyMyNGzKT0aAH6ulQ_BmxnBPhjQg9-91HhjQskcvCmkZG3rDs8Qw-26IjaD80QLq4eRn2xW9t7cuNo2fmQOoc_M5XYXKdvfMa1qEZms_Z2OB-EVaMuWVKP8TzmykclhWiTEsUVxdWyXVCSXjbcoN5axTYyWkCfSX3Ob6eULHgoF_ZFWXI-9hAfdoPJBWZfX-lwpCPKklOdDAZgODRIprdYGDEWPqs3eASLfVm1_jhzmbCk0OJ9tH2nio0ankZWkIUy5U85ClsIGPq9wpokHGBwas5mooKqkKpookhAhsLZCSelajSuWk1neX4g6vzXI9vsACHjoj-7FEBqxZw9ev00r2SoknedxlyQsGqlVNxR82bmCBzxTAY1K98TXTFsIzcrB0rEd9R8lx7RjfiMEahX09ANTbp-6xgfTjOzb9pNvqtW35b9zqwcEHW-ZWbHGQxFXkRQmHq76yZnT6bsaWGqT3m6CU7H3xmSwiOw1J1psQuwcqaswfbC0s-cs4M5ilUIn2CMSxyzB_yk467BF1HsCRS0ZoI'
        }
        response = requests.get(full_url, headers=headers, data={}).json()
        
        # confirm retrieval of JSON from API
        print(response)
        
        # store JSON in pandas.dataframe, then store pandas.dataframe in SQLite

        # to add confidence_score && user_xp, use pandas.DataFrame.apply()

        # let's store our JSON first, then prepare it for server-side rendering (template)
        
        # store JSON from API call, and then pass JSON as python object

        # pull from database that stores JSON to be rendered in template
        
        # pass dict from JSON for server-side rendering w template
            #init
            # question = []
            # choices = [] 
            # exams = {}
            # exams['question'] = response['question']
            # exams['choices'] = response['choices']
    
        # when user wants to hit /modules/training (arithmetic) module, then perform api calls and then render the JSON into tabs)
        return render(request, '../templates/arithmetic.html', {'exams': exams})

    # make sqlite connection so you can pass JSON to be stored into pandas dataframe and then into SQLite Database
        # get templates working first
        # pandas.DataFrame.to_sql()
        # sqlite.connection()

# dashboard
    # pull analytics from pandas.dataframe which calls SQLite (stored JSON) and convert to matplotlib graphs
    # graph / plot:
        # estimated time of mastery, 
        # # of total correct questions solved, 
        # # of matches won, 
        # # of minutes spent on average per question, 
        # total xp (computed in respect to session_time, confidence_score, and if response['answer'] === form passed through template to backend)
    # def dashboard(request):
    # return render(request, 'dashboard.html')

# multiplayer
    # hit SQLite to pass JSON as python objects to be rendered as server-side template
    # simulate competition by rendering progress bar with PC competitor
    # feature request: setup CRUD properties to allow users to CRUD their own problem_sets
    # feature request: setup public / private sessions 


# tutors
    # grid of sample users (tutors)
    # filter via availability and category_speciality
    # render # of kids who have solved a specific a "difficult" problem (social pressure / motivation)
    # allow user to navigate for tutors and filter based on category
    # prompt for category specification
    # display active tutor users
    # store created users in SQL
    # must store user accounts, performance_metrics, status (tutor, student, both), exam_results

# profile
    # user can access settings / notifications page to personalize their settings
    # if request.method == 'GET': profile_pic = request.FILE['myfile'] (user can upload profile picture)   


# Build and implement confidence-based algorithm, for every 1 instance of completion {onSubmit} => {launch popup that collects user confidence ranked via 0-5}
# Scrape all problem sets for K-12 level mathematics that are high-signal, convert questions into problem sets (0/12), similar to KhanAcademy
# allow the user to focus on weaker problem types after assessing their baseline given confidence_score, accuracy, and assessing what problems must be returned in rank order of priority (in respect to weaker problem types)
# Weaker problem types will be prioritized in rank order based on results from popups
# Scale of distribution of matches for users (within classroom, then district, then region, then country)

# view decorators: https://docs.djangoproject.com/en/3.0/topics/http/decorators/

