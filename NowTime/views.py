# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.http.response import JsonResponse
from .generic import *
from django.conf import settings
import json
import telebot


# Create your views here.
class TimeView(View):
    bot = telebot.TeleBot(settings.TGRM_TOKEN)

    def post(self, request, *args, **kwargs):
        test = request.body.decode('utf-8')
        body = json.loads(test)
        try:
            city = body['query']
        except KeyError:
            city = body['message']['text']
        chat_id = body['message']['chat']['id']
        text_help = "TimeBot - простой способ узнать сколько сейчас времени в интересующем вас городе.\
        \nПросто напишите название города. Например, чтобы узнать сколько сейчас времени в городе Чирчик,\
        отправьте сообщение 'Чирчик'."
        if city == '/help':
            self.bot.send_message(chat_id, text_help)
        elif city == '/start':
            self.bot.send_message(chat_id, text_help)
        else:
            cur_time = current_time(city)
            if cur_time:
                self.bot.send_message(chat_id, 'Текущее время в городе {} - {}'.format(city, cur_time))
            else:
                self.bot.send_message(chat_id, """Город не найден. Попробуйте уточнить запрос указав страну.
                Например: Чирчик, Узбекистан""")
        return JsonResponse({})

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TimeView, self).dispatch(request, *args, **kwargs)
