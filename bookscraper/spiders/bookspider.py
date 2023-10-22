import scrapy


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

        rows = response.css('table tr')

        book_item = {
            'upc': rows[0].css('td::text').get()
        }

        yield book_item
