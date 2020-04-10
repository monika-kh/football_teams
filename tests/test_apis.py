from django.urls import reverse
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from players.models import Team, Player


class EndPointTestCase(APITestCase):
    def setUp(self):
        self.name = 'test'
        self.club_state = 'test_state'

        self.team = Team.objects.create(
            name=self.name,
            club_state=self.club_state)

        self.first_name = 'first_test'
        self.last_name = 'last_name'
        self.jersey_number = 77
        self.country = 'india'
        self.team = self.team

        self.player = Player.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            jersey_number=self.jersey_number,
            country=self.country,
            team=self.team
        )

    def test_post_team(self):
        url = reverse('team')
        res = self.client.post(url, {'name': self.name, 'club_state': self.club_state})
        assert res.status_code == 201

    def test_get_team(self):
        url = reverse('team')
        res = self.client.get(url)
        assert res.status_code == 200

    def test_get_team_by_id(self):
        url = reverse('team_id', kwargs={"pk": "1"})
        res = self.client.get(url)
        assert res.status_code == 200

    def test_put_team(self):
        url = reverse('team_id', kwargs={'pk': '1'})
        data = {'name': 'example', 'club_state': 'test_example'}
        res = self.client.put(url, data)
        assert res.status_code == 200

    def test_post_player(self):
        url = reverse('player')
        self.id = self.team.id
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'jersey_number': self.jersey_number,
            'country': self.country,
            'team': self.id
        }
        res = self.client.post(url, data)
        assert res.status_code == 201

    def test_get_player(self):
        url = reverse('player')
        res = self.client.get(url)
        assert res.status_code == 200

    def test_get_player_by_id(self):
        url = reverse('player_id', kwargs={'pk': '1'})
        res = self.client.get(url)
        assert res.status_code == 200

    def test_put_player(self):
        url = reverse('player_id', kwargs={'pk': '1'})
        data = {
            'first_name': 'test',
            'last_name': 'test',
            'jersey_number': '11',
            'country': 'australia',
            'team': 1
        }
        res = self.client.put(url, data)
        assert res.status_code == 202

    def test_delete_player(self):
        url = reverse('player_id', kwargs={'pk': '1'})
        res = self.client.delete(url)
        assert res.status_code == 200
