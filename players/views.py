from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer


# Create your views here.


class TeamView(APIView):
    def post(self, request):
        data = request.data
        serializer = TeamSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)

    def get(self, request, pk=None):
        if pk:
            team = Team.objects.get(id=pk)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        else:
            team = Team.objects.all()
            serializer = TeamSerializer(team, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        team = Team.objects.get(id=pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PlayerView(APIView):
    def post(self, request):
        data = request.data
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)

    def get(self, request, pk=None):
        if pk:
            player = Player.objects.get(id=pk)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        else:
            player = Player.objects.all()
            serializer = PlayerSerializer(player, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=404)

    def delete(self, request, pk):
        player = Player.objects.get(id=pk)
        player.delete()
        return Response({"message": "deleted"}, status=200)
