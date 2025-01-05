from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import get_gpt_response, create_thread_openai


def assistant(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        print(user_input)
        response = get_gpt_response(user_input)
        return JsonResponse({"response": response})
    return render(request, "assistant/assistant.html")


@api_view(["POST"])
def chat_send_message(request):
    thread_id = request.data.get("thread_id")
    user_input = request.data.get("user_input")
    response = get_gpt_response(user_input, thread_id)
    print(user_input)
    return Response({"response": response})


@api_view(["POST"])
def create_thread(request):
    thread_id = create_thread_openai()
    return Response({"thread_id": thread_id})
