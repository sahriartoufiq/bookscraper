import scrapy
from bookscraper.items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    base_url = "https://books.toscrape.com/"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):

        books = response.css('article.product_pod')

        for book in books:

            relative_url = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = self.base_url + relative_url
            else:
                book_url = self.base_url + 'catalogue/' + relative_url

            yield response.follow(book_url, callback=self.parse_book_page)

    def parse_book_page(self, response):

        row_data_list = response.css('table tr')

        book = BookItem()

        book['title'] = response.css('.product_main h1::text').get()
        book['upc'] = self.getRowData(row_data_list, 0)
        book['product_type'] = self.getRowData(row_data_list, 1)
        book['price'] = self.getRowData(row_data_list, 3)
        book['tax'] = self.getRowData(row_data_list, 4)
        book['description'] = response.css('#product_description + p::text').get()

        yield book

    def getRowData(self, row_data_list, row_index):
        return row_data_list[row_index].css('td::text').get()
