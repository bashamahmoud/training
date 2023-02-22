import requests
from django.http import HttpResponse
from rest_framework.utils import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# url:http://127.0.0.1:8000/joke/get/<category> #GET request
def get_joke(request, category):
    url = "https://jokeapi-v2.p.rapidapi.com/joke/" + category

    querystring = {"format": "json", "idRange": "0-150", "blacklistFlags": "nsfw,racist"}

    headers = {
        "X-RapidAPI-Key": "6c0ba2516dmsh21b1583473e4ddap183cc4jsn0af1b6d50837",
        "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    body = response.json()['type']
    if body == "twopart":  # to display only the joke (it's two types of jokes)
        joke_part_one = response.json()['setup']
        joke_part_two = response.json()['delivery']
        joke = [joke_part_one, joke_part_two]
        return HttpResponse(json.dumps(joke))
        pass
    else:
        joke = response.json()['joke']
        return HttpResponse(json.dumps(joke))


# url:http://127.0.0.1:8000/joke/categories #GET request
def get_category(request):
    url = "https://jokeapi-v2.p.rapidapi.com/categories"

    querystring = {"format": "json"}

    headers = {
        "X-RapidAPI-Key": "6c0ba2516dmsh21b1583473e4ddap183cc4jsn0af1b6d50837",
        "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    body = response.json()['categories']
    body_json = json.dumps(body)  # display only categories list as json
    return HttpResponse(body_json)
    pass


# http://127.0.0.1:8000/joke/submit-joke #put or POST request ,joke as json in body
@csrf_exempt  # The CSRF required by server
def submit_joke(request):
    url = "https://jokeapi-v2.p.rapidapi.com/submit"

    payload = {
        "formatVersion": 2,
        "category": "Miscellaneous",
        "type": "single",
        "joke": request.POST.get("joke"),  # get joke from body
        "flags": {
            "nsfw": False,
            "religious": False,
            "political": False,
            "racist": False,
            "sexist": False
        }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "6c0ba2516dmsh21b1583473e4ddap183cc4jsn0af1b6d50837",
        "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }

    response = requests.request("PUT", url, json=payload, headers=headers)

    print(response.text)

    return HttpResponse(response.text)
    pass
