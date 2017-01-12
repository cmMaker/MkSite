from django.shortcuts import render_to_response as response


def index(request):

    return response('home/index.html')
