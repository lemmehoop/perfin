import json

from django.http import JsonResponse
from django.views import View

from perfin.settings import DEBUG
from tgbot.tasks import process_telegram_event


class TelegramBotWebhookView(View):
    def post(self, request, *args, **kwargs):
        if DEBUG:
            process_telegram_event(update_json=json.loads(request.body))
        else:
            process_telegram_event.delay(update_json=json.loads(request.body))

        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})
