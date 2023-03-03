import requests
from django.http import HttpResponse
from rest_framework.utils import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


class JokeApi(APIView):
    def __init__(self):
        self.headers = {}
        self.query_string = {}

    def create_params(self, user_format):
        if user_format:
            self.query_string["format"] = user_format

        else:
            self.query_string["format"] = "json"

    def extend_headers(self):
        self.headers.update({"X-RapidAPI-Key": "6c0ba2516dmsh21b1583473e4ddap183cc4jsn0af1b6d50837",
                             "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com",
                             "content-type": "application/json"})

    def get_joke(self, request, category):
        url = "https://jokeapi-v2.p.rapidapi.com/joke/" + category
        self.create_params(request.GET.get("format"))
        self.extend_headers()

        response = requests.request("GET", url, headers=self.headers,
                                    params=self.query_string)
        if self.query_string == ({"format": "json "}):
            body = response.json()["type"]
            if body == "twopart":  # to display only the joke (it's two types of jokes)
                joke_part_one = response.json()["setup"]
                joke_part_two = response.json()["delivery"]
                joke = [joke_part_one, joke_part_two]
                return HttpResponse(json.dumps(joke))
            else:
                joke = response.json()["joke"]
                return HttpResponse(json.dumps(joke))
        else:
            return HttpResponse(response.text)

    def get_category(self, request):
        url = "https://jokeapi-v2.p.rapidapi.com/categories"
        self.create_params(request.GET.get("format"))
        print(self.query_string)

        self.extend_headers()
        response = requests.request("GET", url, headers=self.headers,
                                    params=self.query_string)

        print("test")
        print(response.text)
        body = response.json()["categories"]
        body_json = json.dumps(body)  # display only categories list as json
        return HttpResponse(body_json)

    @csrf_exempt  # The CSRF required by server
    def submit_joke(self, request):
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
                "sexist": False,
            },
        }
        self.extend_headers()

        response = requests.request("PUT", url, json=payload, headers=self.headers)

        print(response.text)

        return HttpResponse(response.text)

    def get(self, request, category=None):
        if category:
            return self.get_joke(request, category)
        else:
            return self.get_category(request)

    def post(self, request):
        return self.submit_joke(request)
