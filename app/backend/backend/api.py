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
# throwaway code for testing

full_url = 'https://studycounts.com/api/v1/arithmetic/simple.json'

# need to simply pass in a dict to the headers parameter
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOGQ3ZjkyZTM4MGNlZDM5YmFmZWE4MmY2NjAwZmUwMGQxNDQ4OTUxNzk5MWVmNGE2NGU1Y2IwOWRkYTJiMWVhNDZhYTI5YjY4NGE2MmVjZjUiLCJpYXQiOjE1OTY5MDk1NTUsIm5iZiI6MTU5NjkwOTU1NSwiZXhwIjoxNjI4NDQ1NTU1LCJzdWIiOiIxMDUyIiwic2NvcGVzIjpbXX0.CpqfyY-6_a9hTDOkoaUyONtnToLuFMEkOyhf800eP_HFUyLOjvHtRNQIJKhurmR4r8l2JsFvZ-ekSE7qAl56HD2KilNYnXQ5Gb7R1fGOiJbD8bf_BckhxDZne7jl4gz-Lf2mQ60JRC8NlXXyMyNGzKT0aAH6ulQ_BmxnBPhjQg9-91HhjQskcvCmkZG3rDs8Qw-26IjaD80QLq4eRn2xW9t7cuNo2fmQOoc_M5XYXKdvfMa1qEZms_Z2OB-EVaMuWVKP8TzmykclhWiTEsUVxdWyXVCSXjbcoN5axTYyWkCfSX3Ob6eULHgoF_ZFWXI-9hAfdoPJBWZfX-lwpCPKklOdDAZgODRIprdYGDEWPqs3eASLfVm1_jhzmbCk0OJ9tH2nio0ankZWkIUy5U85ClsIGPq9wpokHGBwas5mooKqkKpookhAhsLZCSelajSuWk1neX4g6vzXI9vsACHjoj-7FEBqxZw9ev00r2SoknedxlyQsGqlVNxR82bmCBzxTAY1K98TXTFsIzcrB0rEd9R8lx7RjfiMEahX09ANTbp-6xgfTjOzb9pNvqtW35b9zqwcEHW-ZWbHGQxFXkRQmHq76yZnT6bsaWGqT3m6CU7H3xmSwiOw1J1psQuwcqaswfbC0s-cs4M5ilUIn2CMSxyzB_yk467BF1HsCRS0ZoI'
}

# need to generate arithmetic problems and convert from MathML to JSON
r = 10
for i in range(r):
    response = requests.get(full_url, headers=headers, data={}).json()
    print(response)

# store JSON objects as python dict objects 
# parse json into python dict object with attributes corresponding to dict keys

# init
question = []
choices = []


# exams are just the problem_sets (must store this in django models)
exams = {}
exams['question'] = response['question']
exams['choices'] = response['choices']




# return render(request, 'arithmetic.html', {'exams': exams})


# serializers: https://www.django-rest-framework.org/api-guide/serializers/
# queries: https://docs.djangoproject.com/en/3.0/topics/db/queries/