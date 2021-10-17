from django.http import HttpResponseForbidden


def validate_request(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()