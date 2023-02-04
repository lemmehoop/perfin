import zoneinfo

from django.utils import timezone


class TimezoneMiddleware:
    """
    Middleware to activate/deactivate timezone support
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            tzname = request.COOKIES.get("timezone")
            if tzname:
                timezone.activate(zoneinfo.ZoneInfo(tzname))
            else:
                timezone.deactivate()
        except Exception as exc:
            print(exc)
            timezone.deactivate()

        return self.get_response(request)
