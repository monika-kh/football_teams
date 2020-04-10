# from django.test import TestCase
# from players.models import Team, Player
#
#
# class ModelsTestCase(TestCase):
#     def setUp(self):
#         self.name = 'mi'
#         self.club_state = 'mumbai'
#
#         self.team = Team.objects.create(
#             name=self.name,
#             club_state=self.club_state
#         )
#
#         self.first_name = 'yuvi'
#         self.last_name = 'singh'
#         self.jersey_number = 66
#         self.country = 'india'
#         self.team = self.team
#
#         self.player = Player.objects.create(
#             first_name=self.first_name,
#             last_name=self.last_name,
#             jersey_number=self.jersey_number,
#             country=self.country,
#             team=self.team
#         )
#
#     def test_team(self):
#         team = Team.objects.get(id=1)
#         assert team.name == self.name
#         assert team.club_state == self.club_state
#
#     def test_player(self):
#
#         player = Player.objects.get(id=1)
#         assert player.first_name == self.first_name
#         assert player.last_name == self.last_name
#         assert player.jersey_number == self.jersey_number
#         assert player.country == self.country
#         assert player.team == self.team
#
