import json
from django.shortcuts import render

def surprise(request):

    with open("../data.json") as file:
        data = json.load(file)

    return render(
        request,
        "love.html",
        {
            "name": data["name"],
            "message": data["message"],
            "images": data["images"]
        }
    )
