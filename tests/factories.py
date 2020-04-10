import factory.fuzzy

from players.models import Team, Player


class TeamFactory(factory.DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.fuzzy.FuzzyText(length=50)
    club_state = factory.fuzzy.FuzzyText(length=50)


class PlayerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Player

    team = factory.SubFactory(TeamFactory)
    first_name = factory.fuzzy.FuzzyText(length=50)
    last_name = factory.fuzzy.FuzzyText(length=50)
    jersey_number = factory.fuzzy.FuzzyInteger(00, 99)
    country = factory.fuzzy.FuzzyText(length=50)
