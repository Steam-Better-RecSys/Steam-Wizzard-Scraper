FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 3000

CMD ["scrapy", "runspider", "steam_scraper/spiders/games.py", "-o", "games.json"]