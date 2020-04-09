from rest_framework import serializers

from .models import Team, Player


class TeamSerializer(serializers.ModelSerializer):
    player = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        # fields = '__all__'
        fields = ['id', 'name', 'club_state', 'player']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    def to_representation(self, instance):
        # represent team's name, but for post method use team_id
        rep = super(PlayerSerializer, self).to_representation(instance)
        rep['team'] = instance.team.name
        return rep
