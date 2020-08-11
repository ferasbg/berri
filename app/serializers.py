from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    User, Modules
    )
from rest_framework import serializres
# import models that are handling object data to be serialized


# User, Profile, Multiplayer, Tutors

class Modules(models.model):
    class meta:
        model = Modules
        fields = ['user', 'question_id', 'problem_type', 'Arithmetic', 'Beginner', 'Intermediate', 'Advanced', 'question', 'choices', 'correct_choice', 'confidence_score', 'session_time', 'user_answer_choice', 'problem_completion', 'user_accuracy', 'total_correct_choices', 'accuracy_instance_count', 'est_mastery_time', 'performance_metrics']

# ORM req
    # Setup Modules.ModelSerializer() to setup serialization of python object --> JSON, ints, values in SQlite3 Database Table

