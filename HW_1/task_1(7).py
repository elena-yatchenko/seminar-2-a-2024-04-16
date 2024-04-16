# задача №7 семинара, которая осталась на дом

"""Задание №7
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст."""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "Hi. Add /news/"


@app.route("/news/")
def news():
    news_list = [
        {
            "title": "Новак заявил, что проект газового хаба с Турцией скоро начнёт реализовываться",
            "description": "Практическая реализация проекта газового хаба между Россией и Турцией начнётся в ближайшее время. Об этом заявил российский вице-премьер Александр Новак.",
            "date": "21 ноября 2023",
        },
        {
            "title": "Эберг и Самуэльссон выиграли сингл-микст на первом этапе Кубка мира",
            "description": "Сборная Швеции выиграла сингл-микст на первом этапе Кубка мира по биатлону в Эстерсунде (Швеция).",
            "date": "24 ноября 2023",
        },
        {
            "title": "Маск назвал пугающим дефицит боеприпасов в Соединённых Штатах",
            "description": "Бизнесмен Илон Маск прокомментировал пост предпринимателя Дэвида Сакса, заявившего о проблеме нехватки боеприпасов у Соединённых Штатов.",
            "date": "25 ноября 2023",
        },
        {
            "title": "Армения и Саудовская Аравия установили дипотношения",
            "description": "Между Арменией и Саудовской Аравией установлены дипломатические отношения.",
            "date": "25 ноября 2023",
        },
    ]

    context = {"name": "Страничка новостей", "news_table": news_list}

    return render_template("news.html", **context)


if __name__ == "__main__":
    app.run()