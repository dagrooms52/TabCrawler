## Tab Crawler
A web crawler to download guitar tabs and display them nicely

---

I'm using this as a project to learn the Python library [Scrapy](http://scrapy.org/).
The goal is to download tabs from the internet, store them in a local library for the user, and display them in a nicer format.

### To see it work:
- Clone the repository: `git clone https://github.com/dagrooms52/TabCrawler.git` <br>
- Navigate into the repository: `cd TabCrawler` <br>
- Run the main script: `python main.py [tab link]`<br>

So far, this will output only the raw tab lines from the file. In the future, this application will allow the user to browse and view stored tabs.

---

#### 

##### Supported Tab Format
Tabs stored at the input link should roughly resemble the following example:

```
  Em                                B7
e:-7---------------7---------------|-----------9---------------------|
B:-7---------7-------------7---7---|-------7-------7-----------------|
G:-7-----7-------7---------7---9---|-----9-------9-------------------|
D:-9---9---9---9-------------------|-8---------------8---------------|
A:-9-------------------------------|---------9-----------------------|
E:-7-------------------------------|---------------------------------|
```

The parser is fairly lenient on formatting however. If you find a tab format that won't work, please open an issue!

##### Supported Domains
Different domains have different methods of storing their tabs. The currently supported domains are:
- [Ultimate-Guitar](http://www.ultimate-guitar.com/)

---

#### Feature Plan

##### Intended Features:
- Extract tabs from links :ballot_box_with_check:
- Extract all tabs from links with multiple tabs listed (such as an artist's tab listing)
- Store processed tabs in a database
- Allow user to scan stored tabs and display them from a list
- Display tabs in a nice format on the command line
- Parse chord links and convert them to tablature

##### Stretch Features:
- User interface with above intended features
- Process tabs and restructure graphically into a pdf or image output format
- Tab maker: let user write a tab, then format perfectly for upload to any tab site

---

###### This application is not intended for commercial purposes, or to steal commercial gain from the websites hosting tabs which it can process. The application is only intended to enhance the user experience of these tab services.
