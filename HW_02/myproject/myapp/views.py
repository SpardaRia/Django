from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request: index')
    return HttpResponse('<h2> работаем через консоль, загляните в файл view</h2>')
