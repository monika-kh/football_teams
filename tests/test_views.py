from django.test import TestCase
from rest_framework.test import APIClient

from players.models import *
from players.serializers import *

from .factories import TeamFactory
from players import views


class TestViews(TestCase):
    def setUp(self):
        self.team = TeamFactory()
        self.client = APIClient()

    def test_team_view(self,):
        request = {'name': self.team.name,
                   'club_state': self.team.club_state}
        res = self.client.post(views.TeamView.as_view())

