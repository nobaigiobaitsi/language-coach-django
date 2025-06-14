from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .openai_utils import get_brief_test_response

def api_test_view(request):
    response = get_brief_test_response()
    return HttpResponse(f"<h2>OpenAI Response:</h2><p>{response}</p>")
