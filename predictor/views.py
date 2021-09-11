import json
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd
import os


class GenerateRating(APIView):
    def __init__(self):
        pass

    def get(self, request):
        username = request.GET["username"]
        df = pd.read_csv('predictor/student_consistency.csv')
        df = df[df['name']==username]
        if df.shape[0] == 0:
            response = {"success": False, "message": "Given Username Does not exist", "data": None}
            return JsonResponse(response)

        data = {"consistency_rating": df['consistency_rating'].values[0], "submission_rating": df['submission_rating'].values[0],
        "overall_rating": df['final_rating'].values[0]}
        response = {"success": True, "message": "test", "data": data}
        return JsonResponse(response)