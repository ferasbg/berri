# base
import re
import base64
import io
import glob
import sys
import os

# time
import time
from time import sleep
import datetime
from datetime import timedelta

# handling data
import pandas
import pandas as pd
import matplotlib
import numpy as np
import requests
import nested_lookup
from nested_lookup import nested_lookup, nested_update

# rendering
from django.shortcuts import render, redirect, render_to_response

# json
import jsonify
import json, urllib
from django.http import JsonResponse
from urllib.request import urlopen
from json import JSONEncoder
from collections import namedtuple, OrderedDict, defaultdict

# db
import sqlite3
import pyrebase

# landing page
def index(request):
    return render(request, "index.html")

# login
def login(request):
    # handle form data to pass to firebase
    # functions to handle react components
    return render(request, "login.html")


# signup
def signup(request):
    # functions to handle react components
    # handle form data to pass to firebase
    return render(request, "signup.html")

# modules
def modules(request):
    return render(request, "modules.html")


# find tutors
def tutors(request):
    return render(request, "tutors.html")


# dashboard / analytics
def dashboard(request):
    # pass in data stored in pandas.dataframe to python dict then use data viz / lib functions to render charts / graphs
    return render(request, "dashboard.html")

def multiplayer(request):
    return render(request, "multiplayer.html")

def about(request):
    return render(request, "about.html")

# modules/training (gateway for problem_sets) = render arithmetic.html
def arithmetic(request):
    return render(request, 'arithmetic.html')
    
def benchmark_test(request, *args, **kwargs):
    # partition computation in benchmark_test view and practice_test view
    if request.method == 'GET':
        # get time when user makes GET request to `/benchmark_test`
        startTime = datetime.datetime.now()
        # get time when user finishes last question 
        with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
            data = json.loads(f.read(), strict=False)
            print(data)
            startTime = datetime.datetime.now()
            print("starting timer for benchmark_exam...")

            # when we make dataframe.insert to pandas.dataframe, we will then convert to python dict every time we need to index / search for key value
            q10 = data["questions"]["question_10"]["problem_completion"]
            print(q10)
        # pass multiple choice form to views django from arithmetic.html (check user_answer_choice after storing to pandas.datafranme)
        if request.method == 'POST':
            with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
                # read in our JSON objects that were converted from pandas.dataframe to add insertions based on indexing
                data = json.loads(f.read(), strict=False)
            form = QuestionForm(request.POST)
            if form.is_valid():
                user_answer_choice = request.POST['user_answer_choice']
                # check for if it matches with correct_choice

                # question_1
                if data["questions"]["question_1"]["user_answer_choice"] == data["questions"]["question_1"]["correct_choice"]:
                    print("hello")
                    # add new key / value pair to the JSON dict
                    accuracy_instance_count = 0
                    accuracy_instance_count += 1
                    # store the incremented count if the answer is correct in python dict, then store in pandas.dataframe
                    data["questions"]["question_1"]["accuracy_instance_count"] = accuracy_instance_count
                    df = pd.DataFrame(data)

                # store accuracy_instance_count if correct_choice === user_answer_choice (values)
                # do for every question 1 - 10

        # store user_xp in python dict (from pandas.dataframe) by multiplying 500 by nested_lookup("accuracy_instance_count", wild=True)

        # check for question 10 problem_completion 
        if q10 == "True":
            endTime = datetime.datetime.now()
            session_time = endTime - startTime
            # convert session_time to string
            session_time = str(session_time)
            # update session_time with calculated session_time
            data["questions"]["question_10"]["session_time"] = session_time 
            print(session_time)
        

    # normalize JSON objects stored in pandas.dataframe
    with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
        # store as JSON object
        data = json.loads(f.read(), strict=False)
        # store JSON as pandas.dataframe
        data = pd.DataFrame(data)
        # display entire dataframe
        pd.set_option('display.max_colwidth', None)
        # normalize / flatten nested JSON in dataframe (parent_node=["questions"]), also need to set path for each question_number (1-n)
        problems_df = pd.json_normalize(data["questions"])
        print(problems_df)
        # we need to store the nested JSON (choices) as it's own dataframe
        choices_data = pd.json_normalize(data=data['questions'], record_path=['choices'])
        choices_df = choices_data.head()
        pd.set_option('display.max_colwidth', None)
        print(choices_df)

    # get question from dict object that was converted from pandas.dataframe
    with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
        # store as JSON object
        questions_dict = json.loads(f.read(), strict=False) 
        # store each question_value indexed from dict (retrieve questions, and choices)
        question_1 = questions_dict["questions"]["question_1"]["question"]
        question_2 = questions_dict["questions"]["question_2"]["question"]
        question_3 = questions_dict["questions"]["question_3"]["question"]
        question_4 = questions_dict["questions"]["question_4"]["question"]
        question_5 = questions_dict["questions"]["question_5"]["question"]
        question_6 = questions_dict["questions"]["question_6"]["question"]
        question_7 = questions_dict["questions"]["question_7"]["question"]
        question_8 = questions_dict["questions"]["question_8"]["question"]
        question_9 = questions_dict["questions"]["question_9"]["question"]
        question_10 = questions_dict["questions"]["question_10"]["question"]

    # get all answer choices (retrieve all choices for each question)
    with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
        # store as JSON object
        questions_dict = json.loads(f.read(), strict=False) 
        # question_1
        # template tag: {{% firstof question_number_choice = object that stores each integer %}}
        q1_choices_a = questions_dict["questions"]["question_1"]["choices"][0]["a"]
        q1_choices_b = questions_dict["questions"]["question_1"]["choices"][0]["b"]
        q1_choices_c = questions_dict["questions"]["question_1"]["choices"][0]["c"]
        q1_choices_d = questions_dict["questions"]["question_1"]["choices"][0]["d"]

        # question_2
        q2_choices_a = questions_dict["questions"]["question_2"]["choices"][0]["a"]
        q2_choices_b = questions_dict["questions"]["question_2"]["choices"][0]["b"]
        q2_choices_c = questions_dict["questions"]["question_2"]["choices"][0]["c"]
        q2_choices_d = questions_dict["questions"]["question_2"]["choices"][0]["d"]

        # question_3
        q3_choices_a = questions_dict["questions"]["question_3"]["choices"][0]["a"]
        q3_choices_b = questions_dict["questions"]["question_3"]["choices"][0]["b"]
        q3_choices_c = questions_dict["questions"]["question_3"]["choices"][0]["c"]
        q3_choices_d = questions_dict["questions"]["question_3"]["choices"][0]["d"]

        # question_4
        q4_choices_a = questions_dict["questions"]["question_4"]["choices"][0]["a"]
        q4_choices_b = questions_dict["questions"]["question_4"]["choices"][0]["b"]
        q4_choices_c = questions_dict["questions"]["question_4"]["choices"][0]["c"]
        q4_choices_d = questions_dict["questions"]["question_4"]["choices"][0]["d"]

        # question_5
        q5_choices_a = questions_dict["questions"]["question_5"]["choices"][0]["a"]
        q5_choices_b = questions_dict["questions"]["question_5"]["choices"][0]["b"]
        q5_choices_c = questions_dict["questions"]["question_5"]["choices"][0]["c"]
        q5_choices_d = questions_dict["questions"]["question_5"]["choices"][0]["d"]

        # question_6
        q6_choices_a = questions_dict["questions"]["question_6"]["choices"][0]["a"]
        q6_choices_b = questions_dict["questions"]["question_6"]["choices"][0]["b"]
        q6_choices_c = questions_dict["questions"]["question_6"]["choices"][0]["c"]
        q6_choices_d = questions_dict["questions"]["question_6"]["choices"][0]["d"]

        # question_7
        q7_choices_a = questions_dict["questions"]["question_7"]["choices"][0]["a"]
        q7_choices_b = questions_dict["questions"]["question_7"]["choices"][0]["b"]
        q7_choices_c = questions_dict["questions"]["question_7"]["choices"][0]["c"]
        q7_choices_d = questions_dict["questions"]["question_7"]["choices"][0]["d"]

        # question_8
        q8_choices_a = questions_dict["questions"]["question_8"]["choices"][0]["a"]
        q8_choices_b = questions_dict["questions"]["question_8"]["choices"][0]["b"]
        q8_choices_c = questions_dict["questions"]["question_8"]["choices"][0]["c"]
        q8_choices_d = questions_dict["questions"]["question_8"]["choices"][0]["d"]

        # question_9
        q9_choices_a = questions_dict["questions"]["question_9"]["choices"][0]["a"]
        q9_choices_b = questions_dict["questions"]["question_9"]["choices"][0]["b"]
        q9_choices_c = questions_dict["questions"]["question_9"]["choices"][0]["c"]
        q9_choices_d = questions_dict["questions"]["question_9"]["choices"][0]["d"]

        # question_10
        q10_choices_a = questions_dict["questions"]["question_10"]["choices"][0]["a"]
        q10_choices_b = questions_dict["questions"]["question_10"]["choices"][0]["b"]
        q10_choices_c = questions_dict["questions"]["question_10"]["choices"][0]["c"]
        q10_choices_d = questions_dict["questions"]["question_10"]["choices"][0]["d"] 
    return render(request, 'benchmark_test.html', {'question_1': question_1, 'question_2': question_2, 'question_3': question_3, 'question_4': question_4, 'question_5': question_5, 'question_6': question_6, 'question_7': question_7, 'question_8': question_8, 'question_9': question_9, 'question_10': question_10, 'q1_choices_a': q1_choices_a, 'q1_choices_b': q1_choices_b, 'q1_choices_c': q1_choices_c, 'q1_choices_d': q1_choices_d, 'q2_choices_a': q2_choices_a, 'q2_choices_b': q2_choices_b, 'q2_choices_c': q2_choices_c, 'q2_choices_d': q2_choices_d, 'q3_choices_a': q3_choices_a, 'q3_choices_b': q3_choices_b, 'q3_choices_c': q3_choices_c, 'q3_choices_d': q3_choices_d, 'q4_choices_a': q4_choices_a, 'q4_choices_b': q4_choices_b, 'q4_choices_c': q4_choices_c, 'q4_choices_d': q4_choices_d, 'q5_choices_a': q5_choices_a, 'q5_choices_b': q5_choices_b, 'q5_choices_c': q5_choices_c, 'q5_choices_d': q5_choices_d, 'q6_choices_a': q6_choices_a, 'q6_choices_b': q6_choices_b, 'q6_choices_c': q6_choices_c, 'q6_choices_d': q6_choices_d, 'q7_choices_a': q7_choices_a, 'q7_choices_b': q7_choices_b, 'q7_choices_c': q7_choices_c, 'q7_choices_d': q7_choices_d, 'q8_choices_a': q8_choices_a, 'q8_choices_b': q8_choices_b, 'q8_choices_c': q8_choices_c, 'q8_choices_d': q8_choices_d, 'q9_choices_a': q9_choices_a, 'q9_choices_b': q9_choices_b, 'q9_choices_c': q9_choices_c, 'q9_choices_d': q9_choices_d, 'q10_choices_a': q10_choices_a, 'q10_choices_b': q10_choices_b, 'q10_choices_c': q10_choices_c, 'q10_choices_d': q10_choices_d})    
    

# pass questions 11-31 with difficulty="Advanced" in rank order of hard to easy
def practice_test(request):
    # normalize JSON objects stored in pandas.dataframe
    with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
        # store as JSON object
        data = json.loads(f.read(), strict=False)
        # store JSON as pandas.dataframe
        data = pd.DataFrame(data)
        # display entire dataframe
        pd.set_option('display.max_colwidth', None)
        # normalize / flatten nested JSON in dataframe (parent_node=["questions"]), also need to set path for each question_number (1-n)
        problems_df = pd.json_normalize(data["questions"])
        print(problems_df)
        # we need to store the nested JSON (choices) as it's own dataframe
        choices_data = pd.json_normalize(data=data['questions'], record_path=['choices'])
        choices_df = choices_data.head()
        pd.set_option('display.max_colwidth', None)
        print(choices_df)

    return render(request, 'practice_test.html')

# # pyrebase
# config = {
#     apiKey: "AIzaSyD0HmBdRKbpexLH-Z9dk16gjf_9i20-KaY",
#     authDomain: "berri-c0bb3.firebaseapp.com",
#     databaseURL: "https://berri-c0bb3.firebaseio.com",
#     projectId: "berri-c0bb3",
#     storageBucket: "berri-c0bb3.appspot.com",
#     messagingSenderId: "787660474330",
#     appId: "1:787660474330:web:26e867d764bd464f1e62e3",
#     measurementId: "G-BB398RGVHB"
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

# def userSignIn(email, password) {
#     email = request.form["login_email"]
#     password = request.form["login_password"]
#     if (request.method=="POST" and email and password):
#         user = auth.sign_in_with_email_and_password(email, password)
# }

# def userSignOut() {
#     auth().signOut()
# }


# wrap computations in function to handle pulling and adding JSON data through pandas.dataframe
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
# allow the user to focus on weaker problem types after assessing their baseline given confidence_score, accuracy, and assessing what problems must be returned in rank order of priority (in respect to weaker problem types)
# Weaker problem types will be prioritized in rank order based on results from popups
# Scale of distribution of matches for users (within classroom, then district, then region, then country)

# view decorators: https://docs.djangoproject.com/en/3.0/topics/http/decorators/

