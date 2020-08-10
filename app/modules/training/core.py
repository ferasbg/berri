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
# let's put filtered json response to be parsed with json.parse() (already with converted mathml strings)

problems = {
    {'id': 'yhcqbzbr', 'question': '<mn>22</mn><mo> - </mo><mo> ( </mo><mn>10</mn><mo> + </mo><mn>13</mn><mo> ) </mo>', 'choices': ['<math><mn>6</mn></math>', '<math><mo>-</mo><mn>1</mn></math>', '<math><mn>1</mn></math>', '<math><mo>-</mo><mn>23</mn></math>', '<math><mn>32</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ygjkg', 'question': '<mn>7</mn><mo> &#xF7; </mo><mo> ( </mo><mn>8</mn><mo> + </mo><mn>5</mn><mo> ) </mo>', 'choices': ['<math><mo>-</mo><mn>1</mn></math>', '<math><mn>1</mn><mfrac><mn>1</mn><mn>14</mn></mfrac></math>', '<math><mo>-</mo><mn>43</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></math>', '<math><mfrac><mn>7</mn><mn>13</mn></mfrac></math>', '<math><mo>-</mo><mn>3</mn><mfrac><mn>1</mn><mn>8</mn></mfrac></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yccf', 'question': '<mn>2</mn><mo> &Cross; </mo><mn>4</mn>', 'choices': ['<math><mn>24</mn></math>', '<math><mn>32</mn></math>', '<math><mn>15</mn></math>', '<math><mn>8</mn></math>', '<math><mn>6</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yclg', 'question': '<mn>9</mn><mo> &Cross; </mo><mn>5</mn>', 'choices': ['<math><mn>4</mn></math>', '<math><mn>12</mn></math>', '<math><mn>6</mn></math>', '<math><mn>60</mn></math>', '<math><mn>45</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yddzh', 'question': '<mn>30</mn><mo> &#xF7; </mo><mn>6</mn>', 'choices': ['<math><mn>4</mn></math>', '<math><mn>6</mn></math>', '<math><mn>3</mn></math>', '<math><mn>12</mn></math>', '<math><mn>5</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ybbpnt', 'question': '<mn>11</mn><mo> - </mo><mn>5</mn>', 'choices': ['<math><mn>35</mn></math>', '<math><mn>6</mn></math>', '<math><mn>15</mn></math>', '<math><mn>0</mn></math>', '<math><mn>14</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yhccnpq', 'question': '<mn>2</mn><mo> - </mo><mo> ( </mo><mn>2</mn><mo> - </mo><mn>12</mn><mo> ) </mo>', 'choices': ['<math><mn>12</mn></math>', '<math><mo>-</mo><mn>20</mn></math>', '<math><mn>0</mn></math>', '<math><mn>39</mn></math>', '<math><mn>15</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ycgf', 'question': '<mn>5</mn><mo> &Cross; </mo><mn>4</mn>', 'choices': ['<math><mn>14</mn></math>', '<math><mn>20</mn></math>', '<math><mn>28</mn></math>', '<math><mn>96</mn></math>', '<math><mn>182</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ylbcbhk', 'question': '<mn>1</mn><mo> &Cross; </mo><mn>2</mn><mo> + </mo><mn>6</mn><mo> &Cross; </mo><mn>8</mn>', 'choices': ['<math><mn>55</mn></math>', '<math><mn>44</mn></math>', '<math><mn>32</mn></math>', '<math><mn>69</mn></math>', '<math><mn>50</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'yjfnpdnp', 'question': '<mo> ( </mo><mn>4</mn><mo> - </mo><mn>1</mn><mo> ) </mo><mo> &Cross; </mo><mo> ( </mo><mn>3</mn><mo> - </mo><mn>1</mn><mo> ) </mo>', 'choices': ['<math><mo>-</mo><mn>60</mn></math>', '<math><mn>12</mn></math>', '<math><mo>-</mo><mn>108</mn></math>', '<math><mn>160</mn></math>', '<math><mn>6</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ycdj', 'question': '<mn>3</mn><mo> &Cross; </mo><mn>7</mn>', 'choices': ['<math><mn>21</mn></math>', '<math><mn>9</mn></math>', '<math><mn>18</mn></math>', '<math><mn>35</mn></math>', '<math><mn>4</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yddrd', 'question': '<mn>33</mn><mo> &#xF7; </mo><mn>3</mn>', 'choices': ['<math><mn>11</mn></math>', '<math><mn>30</mn></math>', '<math><mn>10</mn></math>', '<math><mn>8</mn></math>', '<math><mn>2</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yglbnq', 'question': '<mn>9</mn><mo> &#xF7; </mo><mo> ( </mo><mn>1</mn><mo> - </mo><mn>2</mn><mo> ) </mo>', 'choices': ['<math><mn>1</mn><mfrac><mn>1</mn><mn>10</mn></mfrac></math>', '<math><mfrac><mn>1</mn><mn>2</mn></mfrac></math>', '<math><mo>-</mo><mn>9</mn></math>', '<math><mn>22</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></math>', '<math><mo>-</mo><mn>5</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ybbnqq', 'question': '<mn>1</mn><mo> - </mo><mn>22</mn>', 'choices': ['<math><mo>-</mo><mn>20</mn></math>', '<math><mn>52</mn></math>', '<math><mn>19</mn></math>', '<math><mo>-</mo><mn>21</mn></math>', '<math><mn>23</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yfbhnw', 'question': '<mn>1</mn><mo> &Cross; </mo><mo> ( </mo><mn>6</mn><mo> - </mo><mn>7</mn><mo> ) </mo>', 'choices': ['<math><mn>91</mn></math>', '<math><mn>40</mn></math>', '<math><mo>-</mo><mn>1</mn></math>', '<math><mn>104</mn></math>', '<math><mo>-</mo><mn>18</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yhbcql', 'question': '<mn>1</mn><mo> - </mo><mo> ( </mo><mn>22</mn><mo> + </mo><mn>9</mn><mo> ) </mo>', 'choices': ['<math><mo>-</mo><mn>30</mn></math>', '<math><mo>-</mo><mn>18</mn></math>', '<math><mn>5</mn></math>', '<math><mo>-</mo><mn>3</mn></math>', '<math><mn>2</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ycjbr', 'question': '<mn>7</mn><mo> &Cross; </mo><mn>13</mn>', 'choices': ['<math><mn>91</mn></math>', '<math><mn>8</mn></math>', '<math><mn>21</mn></math>', '<math><mn>22</mn></math>', '<math><mn>20</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yhjctnp', 'question': '<mn>7</mn><mo> - </mo><mo> ( </mo><mn>25</mn><mo> - </mo><mn>1</mn><mo> ) </mo>', 'choices': ['<math><mn>13</mn></math>', '<math><mo>-</mo><mn>14</mn></math>', '<math><mo>-</mo><mn>9</mn></math>', '<math><mo>-</mo><mn>17</mn></math>', '<math><mn>7</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yfjkb', 'question': '<mn>7</mn><mo> &Cross; </mo><mo> ( </mo><mn>8</mn><mo> + </mo><mn>1</mn><mo> ) </mo>', 'choices': ['<math><mn>27</mn></math>', '<math><mn>110</mn></math>', '<math><mn>52</mn></math>', '<math><mo>-</mo><mn>70</mn></math>', '<math><mn>63</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ybdqd', 'question': '<mn>32</mn><mo> + </mo><mn>3</mn>', 'choices': ['<math><mo>-</mo><mn>7</mn></math>', '<math><mn>45</mn></math>', '<math><mn>24</mn></math>', '<math><mn>35</mn></math>', '<math><mn>22</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ybbxnrz', 'question': '<mn>18</mn><mo> - </mo><mn>30</mn>', 'choices': ['<math><mn>30</mn></math>', '<math><mo>-</mo><mn>12</mn></math>', '<math><mn>57</mn></math>', '<math><mo>-</mo><mn>13</mn></math>', '<math><mo>-</mo><mn>4</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ylkbbdg', 'question': '<mn>8</mn><mo> &Cross; </mo><mn>1</mn><mo> + </mo><mn>3</mn><mo> &Cross; </mo><mn>5</mn>', 'choices': ['<math><mn>52</mn></math>', '<math><mo>-</mo><mn>7</mn></math>', '<math><mn>23</mn></math>', '<math><mn>36</mn></math>', '<math><mn>13</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ylcbbfl', 'question': '<mn>2</mn><mo> &Cross; </mo><mn>1</mn><mo> + </mo><mn>4</mn><mo> &Cross; </mo><mn>9</mn>', 'choices': ['<math><mn>77</mn></math>', '<math><mn>174</mn></math>', '<math><mn>38</mn></math>', '<math><mn>116</mn></math>', '<math><mn>28</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'yjbqnvgc', 'question': '<mo> ( </mo><mn>12</mn><mo> - </mo><mn>6</mn><mo> ) </mo><mo> &Cross; </mo><mo> ( </mo><mn>5</mn><mo> + </mo><mn>2</mn><mo> ) </mo>', 'choices': ['<math><mn>52</mn></math>', '<math><mn>48</mn></math>', '<math><mn>90</mn></math>', '<math><mn>30</mn></math>', '<math><mn>42</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'yfcbzbq', 'question': '<mn>2</mn><mo> &Cross; </mo><mo> ( </mo><mn>10</mn><mo> + </mo><mn>12</mn><mo> ) </mo>', 'choices': ['<math><mn>44</mn></math>', '<math><mn>15</mn></math>', '<math><mn>152</mn></math>', '<math><mn>90</mn></math>', '<math><mn>18</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yjdgch', 'question': '<mo> ( </mo><mn>3</mn><mo> + </mo><mn>5</mn><mo> ) </mo><mo> &Cross; </mo><mo> ( </mo><mn>2</mn><mo> + </mo><mn>6</mn><mo> ) </mo>', 'choices': ['<math><mn>36</mn></math>', '<math><mn>64</mn></math>', '<math><mn>91</mn></math>', '<math><mn>52</mn></math>', '<math><mn>20</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ybbtnrs', 'question': '<mn>15</mn><mo> - </mo><mn>34</mn>', 'choices': ['<math><mn>34</mn></math>', '<math><mn>23</mn></math>', '<math><mn>25</mn></math>', '<math><mo>-</mo><mn>16</mn></math>', '<math><mo>-</mo><mn>19</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ycjc', 'question': '<mn>7</mn><mo> &Cross; </mo><mn>2</mn>', 'choices': ['<math><mn>14</mn></math>', '<math><mn>9</mn></math>', '<math><mn>12</mn></math>', '<math><mn>24</mn></math>', '<math><mn>25</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ylblbdh', 'question': '<mn>1</mn><mo> &Cross; </mo><mn>9</mn><mo> + </mo><mn>3</mn><mo> &Cross; </mo><mn>6</mn>', 'choices': ['<math><mn>26</mn></math>', '<math><mn>138</mn></math>', '<math><mn>20</mn></math>', '<math><mn>27</mn></math>', '<math><mn>42</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ykgbtcnp', 'question': '<mo> ( </mo><mn>5</mn><mo> + </mo><mn>15</mn><mo> ) </mo><mo> &#xF7; </mo><mo> ( </mo><mn>2</mn><mo> - </mo><mn>1</mn><mo> ) </mo>', 'choices': ['<math><mn>2</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></math>', '<math><mo>-</mo><mn>1</mn><mfrac><mn>3</mn><mn>10</mn></mfrac></math>', '<math><mn>5</mn></math>', '<math><mn>20</mn></math>', '<math><mn>2</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ylbgbcc', 'question': '<mn>1</mn><mo> &Cross; </mo><mn>5</mn><mo> + </mo><mn>2</mn><mo> &Cross; </mo><mn>2</mn>', 'choices': ['<math><mo>-</mo><mn>2</mn></math>', '<math><mn>58</mn></math>', '<math><mn>60</mn></math>', '<math><mn>9</mn></math>', '<math><mn>84</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ycjd', 'question': '<mn>7</mn><mo> &Cross; </mo><mn>3</mn>', 'choices': ['<math><mn>6</mn></math>', '<math><mn>110</mn></math>', '<math><mn>66</mn></math>', '<math><mn>12</mn></math>', '<math><mn>21</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ylllbfd', 'question': '<mn>9</mn><mo> &Cross; </mo><mn>9</mn><mo> + </mo><mn>4</mn><mo> &Cross; </mo><mn>3</mn>', 'choices': ['<math><mn>5</mn></math>', '<math><mn>42</mn></math>', '<math><mn>14</mn></math>', '<math><mo>-</mo><mn>21</mn></math>', '<math><mn>93</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ybzchcgvd', 'question': '<mn>2</mn><mo> &Cross; </mo><mn>6</mn><mo> - </mo><mn>56</mn><mo> &#xF7; </mo><mn>3</mn>', 'choices': ['<math><mn>22</mn></math>', '<math><mo>-</mo><mn>6</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></math>', '<math><mo>-</mo><mn>9</mn><mfrac><mn>2</mn><mn>3</mn></mfrac></math>', '<math><mn>66</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></math>', '<math><mn>17</mn><mfrac><mn>7</mn><mn>8</mn></mfrac></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ybbrk', 'question': '<mn>13</mn><mo> + </mo><mn>8</mn>', 'choices': ['<math><mo>-</mo><mn>10</mn></math>', '<math><mn>2</mn></math>', '<math><mn>21</mn></math>', '<math><mn>33</mn></math>', '<math><mo>-</mo><mn>5</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yhbycqnqq', 'question': '<mn>19</mn><mo> - </mo><mo> ( </mo><mn>22</mn><mo> - </mo><mn>22</mn><mo> ) </mo>', 'choices': ['<math><mo>-</mo><mn>14</mn></math>', '<math><mo>-</mo><mn>22</mn></math>', '<math><mo>-</mo><mn>4</mn></math>', '<math><mo>-</mo><mn>8</mn></math>', '<math><mn>19</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ykgfgnq', 'question': '<mo> ( </mo><mn>5</mn><mo> + </mo><mn>4</mn><mo> ) </mo><mo> &#xF7; </mo><mo> ( </mo><mn>5</mn><mo> - </mo><mn>2</mn><mo> ) </mo>', 'choices': ['<math><mn>3</mn><mfrac><mn>5</mn><mn>6</mn></mfrac></math>', '<math><mo>-</mo><mn>3</mn><mfrac><mn>1</mn><mn>7</mn></mfrac></math>', '<math><mfrac><mn>5</mn><mn>8</mn></mfrac></math>', '<math><mn>12</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></math>', '<math><mn>3</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ydjzc', 'question': '<mn>70</mn><mo> &#xF7; </mo><mn>2</mn>', 'choices': ['<math><mn>7</mn></math>', '<math><mn>11</mn></math>', '<math><mn>35</mn></math>', '<math><mn>22</mn></math>', '<math><mn>37</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ycdbp', 'question': '<mn>3</mn><mo> &Cross; </mo><mn>11</mn>', 'choices': ['<math><mn>49</mn></math>', '<math><mn>10</mn></math>', '<math><mn>52</mn></math>', '<math><mn>48</mn></math>', '<math><mn>33</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'ybzdjbjwj', 'question': '<mn>3</mn><mo> &Cross; </mo><mn>7</mn><mo> + </mo><mn>77</mn><mo> &#xF7; </mo><mn>7</mn>', 'choices': ['<math><mn>15</mn><mfrac><mn>3</mn><mn>4</mn></mfrac></math>', '<math><mn>32</mn></math>', '<math><mo>-</mo><mn>24</mn></math>', '<math><mn>6</mn><mfrac><mn>2</mn><mn>5</mn></mfrac></math>', '<math><mn>28</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ybzdccbzk', 'question': '<mn>3</mn><mo> &Cross; </mo><mn>2</mn><mo> - </mo><mn>10</mn><mo> &#xF7; </mo><mn>8</mn>', 'choices': ['<math><mn>15</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></math>', '<math><mn>49</mn></math>', '<math><mn>20</mn><mfrac><mn>7</mn><mn>10</mn></mfrac></math>', '<math><mn>23</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></math>', '<math><mn>4</mn><mfrac><mn>3</mn><mn>4</mn></mfrac></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'ybbwcr', 'question': '<mn>17</mn><mo> + </mo><mn>23</mn>', 'choices': ['<math><mn>33</mn></math>', '<math><mn>15</mn></math>', '<math><mn>2</mn></math>', '<math><mn>40</mn></math>', '<math><mo>-</mo><mn>2</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Beginner'}
    {'id': 'yfcjns', 'question': '<mn>2</mn><mo> &Cross; </mo><mo> ( </mo><mn>7</mn><mo> - </mo><mn>4</mn><mo> ) </mo>', 'choices': ['<math><mn>56</mn></math>', '<math><mo>-</mo><mn>20</mn></math>', '<math><mn>6</mn></math>', '<math><mo>-</mo><mn>30</mn></math>', '<math><mn>20</mn></math>'], 'correct_choice': 2, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yljbbjl', 'question': '<mn>7</mn><mo> &Cross; </mo><mn>1</mn><mo> + </mo><mn>7</mn><mo> &Cross; </mo><mn>9</mn>', 'choices': ['<math><mo>-</mo><mn>2</mn></math>', '<math><mo>-</mo><mn>4</mn></math>', '<math><mn>68</mn></math>', '<math><mn>15</mn></math>', '<math><mn>70</mn></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Advanced'}
    {'id': 'yfgcbq', 'question': '<mn>5</mn><mo> &Cross; </mo><mo> ( </mo><mn>2</mn><mo> + </mo><mn>12</mn><mo> ) </mo>', 'choices': ['<math><mn>27</mn></math>', '<math><mn>12</mn></math>', '<math><mo>-</mo><mn>24</mn></math>', '<math><mn>70</mn></math>', '<math><mo>-</mo><mn>25</mn></math>'], 'correct_choice': 3, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yfjbzbp', 'question': '<mn>7</mn><mo> &Cross; </mo><mo> ( </mo><mn>10</mn><mo> + </mo><mn>11</mn><mo> ) </mo>', 'choices': ['<math><mn>147</mn></math>', '<math><mn>40</mn></math>', '<math><mn>68</mn></math>', '<math><mn>32</mn></math>', '<math><mn>24</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yfbcnw', 'question': '<mn>1</mn><mo> &Cross; </mo><mo> ( </mo><mn>2</mn><mo> - </mo><mn>7</mn><mo> ) </mo>', 'choices': ['<math><mo>-</mo><mn>5</mn></math>', '<math><mn>26</mn></math>', '<math><mn>140</mn></math>', '<math><mo>-</mo><mn>16</mn></math>', '<math><mn>84</mn></math>'], 'correct_choice': 0, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'yfhcj', 'question': '<mn>6</mn><mo> &Cross; </mo><mo> ( </mo><mn>2</mn><mo> + </mo><mn>7</mn><mo> ) </mo>', 'choices': ['<math><mn>10</mn></math>', '<math><mn>54</mn></math>', '<math><mn>72</mn></math>', '<math><mo>-</mo><mn>42</mn></math>', '<math><mn>18</mn></math>'], 'correct_choice': 1, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
    {'id': 'ygcrkf', 'question': '<mn>23</mn><mo> &#xF7; </mo><mo> ( </mo><mn>8</mn><mo> + </mo><mn>4</mn><mo> ) </mo>', 'choices': ['<math><mn>19</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></math>', '<math><mn>17</mn></math>', '<math><mfrac><mn>1</mn><mn>3</mn></mfrac></math>', '<math><mn>5</mn></math>', '<math><mn>1</mn><mfrac><mn>11</mn><mn>12</mn></mfrac></math>'], 'correct_choice': 4, 'instruction': 'Evaluate', 'category': 'Arithmetic', 'topic': 'Simple', 'difficulty': 'Intermediate'}
}

problems = json.parse(problems)
print(problems)










# function to extract key / values from JSON into dicts that can be rendered as plaintext
    #def customProblemDecoder(problemDict):
    #        return namedtuple('X', problemDict.keys())(*problemDict.values())
    ## problem_type = json.loads(response, object_hook=customProblemDecoder)
    ## print(problem.question, problem.choices, problem.correct_choice, problem.confidence_score)


# create models / serializers to store JSON objects as python django model objects (ref: https://docs.djangoproject.com/en/3.0/topics/db/models/)
# import JSON objects to be converted into python objects

# parse json into python dict object with attributes corresponding to dict keys

# init
question = []
choices = []

# pass dict from JSON for server-side rendering w template
# store JSON objects (with equations converted as mathml strings) as python dict objects and store as django models

# exams are just the problem_sets (must store this in django models)
exams = {}
exams['question'] = response['question']
exams['choices'] = response['choices']


# setup request.Session() in order to provide default data to request methods, setup cookies for sessions (store metadata)


# return render(request, 'arithmetic.html', {'exams': exams})


# serializers: https://www.django-rest-framework.org/api-guide/serializers/
# queries: https://docs.djangoproject.com/en/3.0/topics/db/queries/