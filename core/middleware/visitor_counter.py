from django.utils import timezone
from core.models import Visitor

class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process client IP address
        ip = self.get_client_ip(request)
        today = timezone.now()

        # Log visitor if unique for the current day
        if not Visitor.objects.filter(ip_address=ip, visit_date__date=today.date()).exists():
            Visitor.objects.create(ip_address=ip, visit_date=today)

        # Process response
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """Retrieve the client's IP address, handling proxies."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # X-Forwarded-For may contain multiple IPs, use the first one
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            # Fallback to REMOTE_ADDR if X-Forwarded-For is not set
            ip = request.META.get('REMOTE_ADDR')
        return ip
