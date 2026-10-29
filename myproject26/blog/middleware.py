import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Log the request details
        print(
            f"Request Method: {request.method}, Path: {request.path}, Time: {datetime.datetime.now()}"
        )

    def process_response(self, request, response):
        # Log the response details
        print(
            f"Response Status Code: {response.status_code}, Time: {datetime.datetime.now()}"
        )
        return response


class BlockIPMiddleware(MiddlewareMixin):
    BLOCKED_IPS = ["127.0.0.1"]  # Example blocked IPs

    def process_request(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.BLOCKED_IPS:
            return HttpResponse("Your IP is blocked.", status=403)
