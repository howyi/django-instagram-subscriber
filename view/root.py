from django.http import HttpResponse
from django.utils import timezone
from model.media.models import Media

def index(request):
    if 'hub.challenge' in request.GET:
        # Subscribe request
        return HttpResponse(request.GET['hub.challenge'])

    if 0 != len(request.POST):
        # New media notificate
        media = Media(date=timezone.now(), data=str(request.POST))
        media.save()
        return HttpResponse('New media received')

    return HttpResponse('hello')
