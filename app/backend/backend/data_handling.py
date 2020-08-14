import requests
import jsonify
import json, urllib
from urllib.request import urlopen
from json import JSONEncoder
from django.http import JsonResponse
import re
import base64
from collections import namedtuple, OrderedDict, defaultdict
import io
import pandas
import datetime
from datetime import datetime
import pandas as pd
import nested_lookup
from nested_lookup import nested_lookup # use for counting accuracy_instance_count over all questions, counting total problem_completion for all questions
import sqlite3
# pandas.dataframe --> JSON --> python dict
# store JSON with pandas.dataFrame(), vice versa 
# write all functions to handle data (user input, computations on user input, read / write / insert changes to db) all in here, refactor code to perform computations under each view instance that interacts with JSON data stored in pandas.dataframe
# need to setup interactions with pandas.dataframe in order to read / write / add insertions to it based on specific event instances
# specify path to locate nested JSON objects through . notation in order to read dataframe and access dict objects
# convert pandas.dataframe --> python dict object --> pass through variable template (setup routes necessary, and refactor under views for /modules/training)


# wrap properly in function when refactoring for views (access normalized JSON to retrieve JSON objects)
# with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
#     # store as JSON object
#     data = json.loads(f.read(), strict=False)
#     # store JSON as pandas.dataframe
#     data = pd.DataFrame(data)
#     # display entire dataframe
#     pd.set_option('display.max_colwidth', None)
#     # normalize / flatten nested JSON in dataframe (parent_node=["questions"]), also need to set path for each question_number (1-n)
#     problems_df = pd.json_normalize(data["questions"])
#     print(problems_df)

#     # we need to store the nested JSON (choices) as it's own dataframe
#     choices_data = pd.json_normalize(data=data['questions'], record_path=['choices'])
#     choices_df = choices_data.head()
#     pd.set_option('display.max_colwidth', None)
#     print(choices_df)

    # convert JSON objects['questions.question_number.question', 'questions.question_number.choices'] into python dicts because we are pulling these two name / value pairs to be rendered in base template 
    
    # convert main dataframe back into python dicts to be rendered as strings in base template
    # problems_dict = problems_df.to_dict(orient="index")
    # print(problems_dict)


with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
    data = json.loads(f.read(), strict=False)
    print(data)
    startTime = datetime.now()
    print("starting timer for benchmark_exam...")

# when we make dataframe.insert to pandas.dataframe, we will then convert to python dict every time we need to index / search for key value
q10 = data["questions"]["question_10"]["problem_completion"]
print(q10)

# check for question 10 problem_completion 
if q10 == "True":
    endTime = datetime.now()
    session_time = endTime - startTime
    # pass session_time to be stored in JSON key value (search and insert key value in dict), then store in pandas.dataframe
    insert_session_time = data["questions"]["question_10"]["session_time"]
    # convert session_time to string
    session_time = str(session_time)
    # update session_time with calculated session_time
    data["questions"]["question_10"]["session_time"] = session_time 
    print(session_time)

with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
    # store as JSON object
    questions_dict = json.loads(f.read(), strict=False)
    print(questions_dict) 
    # search for question['value'] for each question stored in nested python dict to render as string
    # search for dict that matches question_1.question['value'] and return as string
    question_value = questions_dict["questions"]["question_1"]["question"]
    q1_choices_a = questions_dict["questions"]["question_1"]["choices"][0]["a"]
    q1_choices_b = questions_dict["questions"]["question_1"]["choices"][0]["b"]

# update the nested value in key / value pair for problem_completion given that the user has submitted the form 



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
with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
    # read in our JSON objects that were converted from pandas.dataframe to add insertions based on indexing
    data = json.loads(f.read(), strict=False)
form = QuestionForm(request.POST)
if form.is_valid()
    user_answer_choice = request.POST['user_answer_choice']
    # check for if it matches with correct_choice
        if data["questions"]["question_1"]["user_answer_choice"] == data["questions"]["question_1"]["correct_choice"]:
        print("hello")
        # add new key / value pair to the JSON dict
        accuracy_instance_count = 0
        accuracy_instance_count += 1