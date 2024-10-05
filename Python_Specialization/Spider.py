import scrapy
from scrapy.crawler import CrawlerProcess


class DCspider(scrapy.Spider):
    name = "dc_spider"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1'
    }

    # Première requête pour lancer le processus de scraping
    def start_requests(self):
        url = 'https://www.datacamp.com/courses/all'
        yield scrapy.Request(url=url, callback=self.parse_front, headers=self.headers)

    # Fonction pour parser la page principale des cours
    def parse_front(self, response):
        # Sélectionner les blocs de cours
        course_blocks = response.css('div.course-block')
        # Extraire les liens relatifs vers les pages de cours
        course_links = course_blocks.xpath('./a/@href')
        links_to_follow = course_links.extract()

        # Vérifier et suivre les liens
        for url in links_to_follow:
            full_url = response.urljoin(url)  # Combiner l'URL de base avec les liens relatifs
            yield response.follow(url=full_url, callback=self.parse_pages)

    # Fonction pour parser chaque page de cours individuelle
    def parse_pages(self, response, dc_dict=None):
        # Extraire le titre du cours
        crs_title = response.xpath('//h1[contains(@class, "title")]/text()')
        crs_title_ext = crs_title.extract_first().strip()

        # Extraire les titres des chapitres
        ch_titles = response.css('h4.chapter__title::text')
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]

        # Initialiser le dictionnaire si nécessaire
        if dc_dict is None:
            dc_dict = {}

        # Ajouter les données extraites au dictionnaire
        dc_dict[crs_title_ext] = ch_titles_ext

        # Retourner les données extraites
        yield dc_dict


# Exemple pour tester le spider
if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'LOG_LEVEL': 'INFO',
        'FEEDS': {
            'dc_courses.json': {
                'format': 'json',
            },
        }
    })

    process.crawl(DCspider)
    process.start()  # Lancer le processus de scraping
