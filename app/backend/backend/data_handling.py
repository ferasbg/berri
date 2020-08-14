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
import pandas as pd
import nested_lookup
from nested_lookup import nested_lookup
import sqlite3
# pandas.dataframe --> JSON --> python dict
# store JSON with pandas.dataFrame(), vice versa 
# write all functions to handle data (user input, computations on user input, read / write / insert changes to db) all in here, refactor code to perform computations under each view instance that interacts with JSON data stored in pandas.dataframe
# need to setup interactions with pandas.dataframe in order to read / write / add insertions to it based on specific event instances
# specify path to locate nested JSON objects through . notation in order to read dataframe and access dict objects
# convert pandas.dataframe --> python dict object --> pass through variable template (setup routes necessary, and refactor under views for /modules/training)


# wrap properly in function when refactoring for views (access normalized JSON to retrieve JSON objects)
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

    # convert JSON objects['questions.question_number.question', 'questions.question_number.choices'] into python dicts because we are pulling these two name / value pairs to be rendered in base template 
    
    # convert main dataframe back into python dicts to be rendered as strings in base template
    # problems_dict = problems_df.to_dict(orient="index")
    # print(problems_dict)


# hit JSON to get python dict, but ONLY read to pandas.dataframe to add insertions

with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
    # store as JSON object
    questions_dict = json.loads(f.read(), strict=False) 
    # search for question['value'] for each question stored in nested python dict to render as string
    # search for dict that matches question_1.question['value'] and return as string
    question_value = questions_dict["questions"]["question_1"]["question"]
    print(question_value)
    # pass question_value into django template



    # for interation loop defined in views.py, based on specific instance, make changes to pandas.dataframe
    # python dictionary must be rendered in base template  
    # store python dict in variable and then do dict lookup and then render the output
    # pass {{ mydict.questions.question_1.question }} in question_1 tab in arithmetic.html
    # convert python dict for each question ,tring to be rendered in django template with {{ problems_dict.get(questions.question_number.question[value]) }}
    
 
 



