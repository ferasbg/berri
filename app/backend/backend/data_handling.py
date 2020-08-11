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
# store operations with pandas.dataFrame() and SQLite database
# then migrate code to perform computations under each view instance

# make sure that pandas can read in JSON data
data = pd.read_json(path_or_buf="/home/ferasbg/projects/Berri/app/backend/db/data/core.json")

df = pd.DataFrame({
    "question_1": {
        "choices": [{
            "a": "49", 
            "b": "10", 
            "c": "52", 
            "d": "48", 
            "e": "33"
        }],
        "question_id": 1,
        "correct_choice": "char",
        "user_answer_choice": "char",
        "confidence_score": "integer",
        "difficulty": "Intermediate",
        "category": "Arithmetic",
        "startTime": "time_value",
        "endTime": "time_value",
        "session_time": "time_value"
    },
    "question_2": {
        "choices": [{
            "a": "49", 
            "b": "10", 
            "c": "52", 
            "d": "48", 
            "e": "33"
        }],
        "question_id": 1,
        "correct_choice": "char",
        "user_answer_choice": "char",
        "confidence_score": "integer",
        "difficulty": "Intermediate",
        "category": "Arithmetic",
        "startTime": "time_value",
        "endTime": "time_value",
        "session_time": "time_value"
    }
})

print(df)

# store JSON in pandas.dataframe


# need to read JSON stored in pandas dataframe

# (pandas.DataFrame.to_json) = convert pandas dataframe to JSON, then convert JSON object to pythond dict that can be rendered through KaTeX

# handle database insertions with pandas.dataframe()