
# Create your views here.
from django.shortcuts import render
from .models import ActivityTracker

from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

# @api_view(["POST"])
def save_example(request):
    if request.method == "POST":
        try:
            row_data = json.loads(request.body)["row_data"]
            a_id = int(row_data["id"])
            row_data.pop('id')
            print("~~~~"*20)
            print(row_data)
            print("~~~~"*20)
            ActivityTracker.objects.filter(id=a_id).update(**row_data)
            return JsonResponse({'status': True})
        except Exception as e:
            return JsonResponse(e)

