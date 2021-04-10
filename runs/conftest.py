import os
import sys

from rest_framework.test import APIClient
from runs.tests import *
import pytest
from django.test import Client
from django.contrib.auth.models import User, Permission

sys.path.append(os.path.dirname(__file__))
faker = Faker("pl_PL")

@pytest.fixture
def client():
    c = Client()
    return c

