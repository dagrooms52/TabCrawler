# TabCrawler
A web crawler to grab guitar tabs and display them nicely

---

I'm using this as an example project to learn the Python library [Scrapy](http://scrapy.org/).
The goal is to download tabs from [Ultimate-Guitar](http://www.ultimate-guitar.com/) and display them in a nicer format. I'd also like to download chord sheets from the site and convert them to tabs eventually. 

####To see it work:
- Clone the repository: `git clone https://github.com/dagrooms52/TabCrawler.git` <br>
- Cd into the repository: `cd TabCrawler` <br>
- Run the crawler: `scrapy crawl tab -o tabs.json`<br>
- Look at `tabs.json`, although it's not very interesting yet.

At this point, the web crawler is able to download the content of one page from [Ultimate-Guitar](http://www.ultimate-guitar.com/); however, it is a proof-of-concept.
