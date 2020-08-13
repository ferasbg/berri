import requests
import jsonify
import json, urllib
from urllib.request import urlopen
from json import JSONEncoder
from django.http import JsonResponse
import re
import base64
from collections import namedtuple
import io
import pandas
import pandas as pd
import sqlite3
# store JSON with pandas.dataFrame() and SQLite database
# write all functions to handle data (user input, computations on user input, read / write / insert changes to db) all in here, refactor code to perform computations under each view instance that interacts with JSON data stored in pandas.dataframe

with open('/home/ferasbg/projects/Berri/app/backend/db/core.json', encoding="utf8") as f:
    # store as JSON object
    data = json.loads(f.read(), strict=False)
    # store JSON as pandas.dataframe
    data = pd.DataFrame(data)
    # display entire dataframe
    pd.set_option('display.max_colwidth', None)
    # normalize / flatten nested JSON in dataframe (parent_node=["questions"]), also need to set path for each question_number (1-n)
    df = pd.json_normalize(data["questions"])
    print(df)
    # we need to store the nested JSON (choices) as it's own dataframe
    choices_data = pd.json_normalize(data=data['questions'], record_path=['choices'])
    choices_df = choices_data.head()
    print(choices_df)

    # need to setup interactions with pandas.dataframe in order to read / write / add insertions to it based on specific event instances

    # specify path for nested JSON objects through . notation in order to read dataframe and access dict objects
    # df = pd.json_normalize(data["questions"], record_path="questions")
    # pass in json_normalize: 
        # record_path=question, choices
        # max_level=4
        # metadata=id, question_number, category, difficulty)
    # save pandas.dataframe as python dict
    # data = df.to_dict(data)
 
 



