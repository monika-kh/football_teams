from django.test import TestCase
from players.models import Team, Player


from .factories import TeamFactory, PlayerFactory


class TestModels(TestCase):
    def test_team_factory(self):
        team = TeamFactory(
            name='mi',
            club_state='mumbai'
        )
        #self.assertEqual(team.name, 'mi')
        assert team.name == 'mi'
        assert team.club_state == 'mumbai'

    def test_player_factory(self):
        team = TeamFactory(
            name='mi',
            club_state='mumbai'
        )
        player = PlayerFactory(
            first_name='yuvi',
            last_name='singh',
            jersey_number='66',
            country='india',
            team=team
        )
        assert player.first_name == 'yuvi'
        assert player.last_name == 'singh'
        assert player.jersey_number == '66'
        assert player.country == 'india'
        assert player.team == team



