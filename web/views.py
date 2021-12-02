from django.shortcuts import HttpResponseRedirect
from django.utils import translation

def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # I use HTTP_REFERER to direct them back to previous path 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))