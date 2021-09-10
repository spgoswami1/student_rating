import json
from django.http import JsonResponse
from rest_framework.views import APIView


class GenerateRating(APIView):
    def __init__(self):
        pass

    def get(self, request):
        username = request.GET["username"]
        response = {"success": True, "message": "test", "data": username}
        return JsonResponse(response)