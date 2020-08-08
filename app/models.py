from django.db import models

# need to render templates and do standard HTML/CSS before hooking react components

# Module(models.Model):
    # model = Module
    # fields = ['user', 'categories', 'units', 'progress', 'performance_metrics']

# Exams(models.Model)
    # class = Meta:
        # model = Exams
        # fields = ['user', 'question', 'choices', 'startTime', 'endTime', 'completion', 'confidence_score' ]
        # queryset = rank next exam given confidence_score
        # permission_classes = [permissions.AllowAny]
    # storing all data in JSON
    # ['url', 'user', 'email', 'groups' ]

# need viewset, serializer

# User(models.Model)
    # need to pass key of all JSON params   
# Profile(models.Model)

# ProfileViewSet

# UserViewSet
