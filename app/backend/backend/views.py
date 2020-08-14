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
import requests
import nested_lookup

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

def login(request):
    # functions to handle react components
    return render(request, "login.html")

def signup(request):
    # functions to handle react components
    return render(request, "signup.html")

# modules
def modules(request):
    return render(request, "modules.html")

def tutors(request):
    return render(request, "tutors.html")

def dashboard(request):
    # pass in data stored in pandas.dataframe to python dict then use data viz / lib functions to render charts / graphs
    return render(request, "dashboard.html")

def multiplayer(request):
    return render(request, "multiplayer.html")

def about(request):
    return render(request, "about.html")

# modules/training (gateway for problem_sets) = render arithmetic.html
def arithmetic(request):
    if request.method = 'GET':
        

    #if request.method == 'GET':
        # track startTime and mark endTime when user submits question 10 with datetime, calculate delta between endTime and startTime
        # if statements for event instances
            # save_for_tutor = save id based on save_for_tutor instance, and then index question that matches id
            # database insertions to pandas.dataframe with pandas.dataframe.apply() = user_xp, est_mastery_time, confidence_score, saved_for_tutor, problem_completion, user_accuracy_instance_count
        # store db insertions in pandas.dataframe

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

    # get all answer choices
    with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
        # store as JSON object
        questions_dict = json.loads(f.read(), strict=False) 

        
        # question_1
        # template tag: {{% firstof question_number_choice = object that stores each integer %}}
        q1_choices_a = questions_dict["questions"]["question_1"]["choices"][0]["a"]
        q1_choices_b = questions_dict["questions"]["question_1"]["choices"][1]["b"]
        q1_choices_c = questions_dict["questions"]["question_1"]["choices"][2]["c"]
        q1_choices_d = questions_dict["questions"]["question_1"]["choices"][3]["d"]

        # question_2
        q2_choices_a = questions_dict["questions"]["question_2"]["choices"][0]["a"]
        q2_choices_b = questions_dict["questions"]["question_2"]["choices"][1]["b"]
        q2_choices_c = questions_dict["questions"]["question_2"]["choices"][2]["c"]
        q2_choices_d = questions_dict["questions"]["question_2"]["choices"][3]["d"]

        # question_3
        q3_choices_a = questions_dict["questions"]["question_3"]["choices"][0]["a"]
        q3_choices_b = questions_dict["questions"]["question_3"]["choices"][1]["b"]
        q3_choices_c = questions_dict["questions"]["question_3"]["choices"][2]["b"]
        q3_choices_d = questions_dict["questions"]["question_3"]["choices"][3]["b"]

        # question_4
        q4_choices_a = questions_dict["questions"]["question_4"]["choices"][0]["a"]
        q4_choices_b = questions_dict["questions"]["question_4"]["choices"][1]["b"]
        q4_choices_c = questions_dict["questions"]["question_4"]["choices"][2]["b"]
        q4_choices_d = questions_dict["questions"]["question_4"]["choices"][3]["b"]

        # question_5
        q5_choices_a = questions_dict["questions"]["question_5"]["choices"][0]["a"]
        q5_choices_b = questions_dict["questions"]["question_5"]["choices"][1]["b"]
        q5_choices_c = questions_dict["questions"]["question_5"]["choices"][2]["b"]
        q5_choices_d = questions_dict["questions"]["question_5"]["choices"][3]["b"]

        # question_6
        q6_choices_a = questions_dict["questions"]["question_6"]["choices"][0]["a"]
        q6_choices_b = questions_dict["questions"]["question_6"]["choices"][1]["b"]
        q6_choices_c = questions_dict["questions"]["question_6"]["choices"][2]["b"]
        q6_choices_d = questions_dict["questions"]["question_6"]["choices"][3]["b"]

        # question_7
        q7_choices_a = questions_dict["questions"]["question_7"]["choices"][0]["a"]
        q7_choices_b = questions_dict["questions"]["question_7"]["choices"][1]["b"]
        q7_choices_c = questions_dict["questions"]["question_7"]["choices"][2]["b"]
        q7_choices_d = questions_dict["questions"]["question_7"]["choices"][3]["b"]

        # question_8
        q8_choices_a = questions_dict["questions"]["question_8"]["choices"][0]["a"]
        q8_choices_b = questions_dict["questions"]["question_8"]["choices"][1]["b"]
        q8_choices_c = questions_dict["questions"]["question_8"]["choices"][2]["b"]
        q8_choices_d = questions_dict["questions"]["question_8"]["choices"][3]["b"]

        # question_9
        q9_choices_a = questions_dict["questions"]["question_9"]["choices"][0]["a"]
        q9_choices_b = questions_dict["questions"]["question_9"]["choices"][1]["b"]
        q9_choices_c = questions_dict["questions"]["question_9"]["choices"][2]["b"]
        q9_choices_d = questions_dict["questions"]["question_9"]["choices"][3]["b"]

        # question_10
        q10_choices_a = questions_dict["questions"]["question_10"]["choices"][0]["a"]
        q10_choices_b = questions_dict["questions"]["question_10"]["choices"][1]["b"]
        q10_choices_c = questions_dict["questions"]["question_10"]["choices"][2]["b"]
        q10_choices_d = questions_dict["questions"]["question_10"]["choices"][3]["b"]

    return render(request, "arithmetic.html", {'question_1': question_1, 'question_2': question_2, 'question_3': question_3, 'question_4': question_4, 'question_5': question_5, 'question_6': question_6, 'question_7': question_7, 'question_8': question_8, 'question_9': question_9, 'question_10': question_10}, {})
    





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

