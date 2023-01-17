from django.http import HttpResponse


class Stripe_WebHook_Handler:
    """
    Handler to Stripe Webhooks
    """
    def __unit__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handler to Stripe Webhooks
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
            )