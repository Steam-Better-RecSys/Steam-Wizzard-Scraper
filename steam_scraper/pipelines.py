from scrapy.exporters import CsvItemExporter


class SteamScraperPipeline:
    def process_item(self, item, spider):
        return item
