from django.test import TestCase
from Metadata.scrapper import scrapper


class Test(TestCase):
    
    def setUp(self):
      scraper_a = scrapper.retrive_metadata("https://stackoverflow.com/questions/41324624/test-driven-development-tdd-for-web-scraping")
      self.scraper_a = scraper_a

      scraper_b = scrapper.retrive_metadata("https://locust.io/")
      self.scraper_b = scraper_b

      scraper_c = scrapper.retrive_metadata("https://github.com/WebMetadataRetrieval")
      self.scraper_c = scraper_c

      # scraper_d = scrapper.retrive_metadata("https://www.myntra.com/flip-flops/us-polo-assn/us-polo-assn-men-off-white--navy-blue-azzaro-solid-thong-flip-flops/8650293/buy")
      # self.scraper_d = scraper_d

    #Test for Title
    def test_title(self):
       self.assertEqual("Test Driven Development (TDD) for Web Scraping", self.scraper_a.title)
       self.assertEqual("Locust - A modern load testing framework", self.scraper_b.title)


    #Test for Description
    def test_description(self):
        self.assertEqual("SE Group-15. Web Metadata Retrieval API has one repository available. Follow their code on GitHub.", self.scraper_c.description)
        #self.assertEqual("Buy U.S. Polo Assn. Men Off White & Navy Blue AZZARO Solid Thong Flip Flops - Flip Flops for Men from U.S. Polo Assn. at Rs. 649. Style ID: 8650293", self.scraper_d.description)
      

    #Test for Thumbnail
    def test_thumbnail(self):
       self.assertEqual("https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded", self.scraper_a.thumbnail)
       self.assertEqual("", self.scraper_b.thumbnail)