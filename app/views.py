from django.shortcuts import render
import numpy as np
import pandas
# need to import / create models
# need to store user responses from hardcoded problem_sets
# need to setup modules (render grid of modules, setup navbar, setup footer)


# dashboard
def index(request):
    return render(request, 'index.html')

# modules
    # render categories and problem_sets under modules

# tutor_portals 
    # allow user to navigate for tutors and filter based on category
    # prompt for category specification
    # display active tutor users
    # store created users in SQL
    # must store user accounts, performance_metrics, status (tutor, student, both), exam_results

# must setup javascript-based form in views for confidence for each instance of problem completion, and handle instance and store in database
# need to setup firebase auth
# must setup postgreSQL db to store users
# save and store user quiz_responses

# Build and implement confidence-based algorithm, for every 1 instance of completion {onSubmit} => {launch popup that collects user confidence ranked via 0-5}
# Scrape all problem sets for K-12 level mathematics that are high-signal, convert questions into problem sets (0/12), similar to KhanAcademy
# Ask for user’s time availability to schedule learning, and also allow the user to focus on weaker problem types after assessing their baseline. 
# Weaker problem types will be prioritized in rank order based on results from popups
# Scale of distribution of matches for users (within classroom, then district, then region, then country)
