import json
from django.shortcuts import render

def surprise(request):

    with open("../data.json", "r") as file:

        data = json.load(file)

    if data.get("type") == "love":

        return render(

            request,

            "love.html",

            {

                "name": data["name"],

                "message": data["message"],

                "images": data["images"],

                "caption": data["caption"]

            }

        )

    elif data.get("type") == "birthday":

        return render(

            request,

            "birthday.html",

            {

                "name": data["name"],

                "message": data["message"],

                "images": data["images"],

                "caption": data["caption"]

            }

        )
    elif data["type"] == "anniversary":

     return render(

        request,

        "anniversary.html",

        {

            "name": data["name"],

            "message": data["message"],

            "images": data["images"],

            "caption": data["caption"]

        }
     )
    elif data["type"] == "apology":

     return render(

        request,

        "sorry.html",


    )
    else:

        return render(

            request,

            "love.html",

            {

                "name": data["name"],

                "message": data["message"],

                "images": data["images"],

                "caption": data["caption"]

            }

        )