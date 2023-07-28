from scrapy.item import Item, Field


class GameItem(Item):
    appid = Field()
    title = Field()
    tags = Field()
    reviews = Field()
    reviews_fancy = Field()
    price = Field()
    release_date = Field()
