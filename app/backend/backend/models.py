from django.db import models
from django.contrib.auth.models import User
from .forms import ModulesForm
from django.utils import simplejson as json
from django.conf import settings
from datetime import datetime
import time
from jsonfield import JSONField


class User(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=true)

    def __str__(self):
        return self.name

class Modules(models.model):
    # must optimize for db schema sanity
    question_id = models.IntegerField()
    question = models.CharField(max_length=500)
    # store choices as JSON, but converted when rendered in django template
    choices = JSONField()
    user_answer_choice = models.IntegerField(choices=choices, max_length=1)
    user = models.CharField(max_length=100)
    start_time = models.DateField(datetime.time())
    end_time = models.DateField()
    # # compute session_time based on delta of end_time and start_time
    session_time = models.TimeField()
    correct_choice = models.BooleanField()
    confidence_score = models.Integerfield(blank=true)
    # track instance of problem completion
    problem_completion = models.BooleanField(blank=true)
    # accuracy = if correct_choice === user_answer
    user_accuracy = models.BooleanField(blank=true)
    # estimated mastery time = compute given confidence_score & session_time per question
    total_correct_choices = models.IntegerField(count=accuracy_instance_count)
    # track number of correctly solved answer choices
    accuracy_instance_count = models.IntegerField(accuracy=accuracy)
    est_mastery_time = models.TimeField()
    performance_metrics = models.IntegerField(confidence_score=confidence_score, est_mastery_time=est_mastery_time, )


# setup viewsets, APIviews, serializers, queryset / serializer_classes / permission_classes
