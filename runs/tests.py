from django.test import TestCase
import pytest
# Create your tests here.
from django.urls import reverse

def test_check_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200