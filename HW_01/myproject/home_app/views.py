from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def text(title, text):
    return f'<h1>Сайт Django</h1>' \
        f'<h2>{title}</h2>' \
        f'<p>{text}</p>'


def main_page(request):
    title = 'Добро пожаловать!'
    body_text = """
    <!DOCTYPE html>
    <html lang="en">        
        <body>     
            <p>Тут должен быть длинный текст, но его нет. Давайте притворимся, что он тут</p>        
            <h2> ^^ </h2>           
        </body>
    </html>
    """
    logger.info(f'Page "main" is open')
    return HttpResponse(text(title, body_text))


def about_me(request):
    title = 'О себе'
    body_text = """
    <!DOCTYPE html>
    <html lang="en">
        <body>
            <header>
                <h3>Снова здравствуйте! Меня зовут Мария, будем знакомы.</h3>
                <p>Есть много вещей, что мне нравится, а также много, что не нравиться. Что до моих увлечений, да, есть некоторые, а мои мечты, про них вам знать не обязательно.</p>
            </header>
        </body>
    </html>
    """
    logger.info(f'Page "about_me" is open')
    return HttpResponse(text(title, body_text))
