
# Proposed Approach

scrapy_scraper_v2.py : This is a python based web scraper which uses scrapy framework to extract data based on the keywords 
passed as arguments. This module carries out a google keyword search on the org name passed as the parameter to extract
the probable domain or website address of that particular organization. After this step, the scraper method parses the website
for keywords from the home page, filters out the stop words and creates a list of relevant content which can be used for
categorization. The module takes a dictionary data set which consists of keys as domain names and a list of related words
for that domain as the values as the base for classification.
Eg. "Healthcare" : ["Health","Provider","Medicare","Coverage","Dental","Insurance","medicaid","pharmaceutical","services","preventive"],
A keyword processor carries out the word matching to predict the probale domain and functional are and a confidence score
based on the number of key words matched.

classifier.py : This is another proposed solution for this problem which can be an improvement upon the version of system
suggested above. This implements a MultonimialNB classification and a NLP based algorithm for categorization.
This module is just a blue print of what an implementation like this can be created but is still not integrated with above 
module.

## Requirements
```
* Python 3.7+
* Scrapy 1.8+
* BeautifulSoup
* nltk
* flashtext
```


## Git Repo



```
git clone https://github.com/Rishabh2991/g2crowd_task.git
```


## Test Run and results
1. Running this command in command prompt : python scrapy_scraper_v2.py "cigna"

Output:
```
2019-11-21 02:17:28 [scrapy.utils.log] INFO: Scrapy 1.8.0 started (bot: scrapybot)
2019-11-21 02:17:28 [scrapy.utils.log] INFO: Versions: lxml 4.2.1.0, libxml2 2.9.8, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 18.9.0, Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 18.0.0 (OpenSSL 1.1.1  11 Sep 2018), cryptography 2.5, Platform Windows-10-10.0.18362-SP0
2019-11-21 02:17:28 [scrapy.crawler] INFO: Overridden settings: {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
2019-11-21 02:17:28 [scrapy.extensions.telnet] INFO: Telnet Password: 74c9de5c06ba36f6
2019-11-21 02:17:28 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
++++++++
++++++++
++++++++
2019-11-21 02:17:29 [urllib3.connectionpool] DEBUG: Starting new HTTPS connection (1): www.cigna.com
2019-11-21 02:17:34 [urllib3.connectionpool] DEBUG: https://www.cigna.com:443 "GET / HTTP/1.1" 200 10823
{'Org name': 'cigna', 'Domain Name': 'https://www.cigna.com/', 'Field of work': 'Healthcare', 'Confidence Score': 0.7}
```
2. Running this command in command prompt : python scrapy_scraper_v2.py "gurutechnologies"

Output:
```
2019-11-21 02:16:13 [scrapy.utils.log] INFO: Scrapy 1.8.0 started (bot: scrapybot)
2019-11-21 02:16:13 [scrapy.utils.log] INFO: Versions: lxml 4.2.1.0, libxml2 2.9.8, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 18.9.0, Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 18.0.0 (OpenSSL 1.1.1  11 Sep 2018), cryptography 2.5, Platform Windows-10-10.0.18362-SP0
2019-11-21 02:16:13 [scrapy.crawler] INFO: Overridden settings: {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
2019-11-21 02:16:13 [scrapy.extensions.telnet] INFO: Telnet Password: 64e0b6228bc3fb52
2019-11-21 02:16:13 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
++++++++
++++++++
++++++++
2019-11-21 02:16:14 [urllib3.connectionpool] DEBUG: Starting new HTTPS connection (1): www.gurutechnologies.net
2019-11-21 02:16:15 [urllib3.connectionpool] DEBUG: https://www.gurutechnologies.net:443 "GET / HTTP/1.1" 200 14713
{'Org name': 'gurutechnologies', 'Domain Name': 'https://www.gurutechnologies.net/', 'Field of work': 'Technology', 'Confidence Score': 0.6}
```
