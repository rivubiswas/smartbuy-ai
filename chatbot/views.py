from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .engine import get_response


def chatbot_response(request):

    user_input = request.GET.get("message")

    response = get_response(user_input)

    return JsonResponse({"response": response})