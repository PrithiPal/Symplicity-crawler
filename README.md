# Symplicity Spider

## Description

---

### Purpose

This internet crawler indexes job postings sfu-symplicity website through crawling scrapy-spider followed by storing them locally in MongoDB database. Below are the key benefits served by the crawler :

* **Local Storage **: The local presence of online data provides with the independence of analysing, manipulating or quering. 
* **Deadline reminder** : The information of job-application deadline can be used for reminders using third-party applications.
* **Search algorithm** : Besides the symplicity-websites built in filters, the presence of data locally helps the user to write custom filters in programming language. Custom-written filters are completely according to the user needs which is not possible with built in filters.
* **Keywords** : As an extension to search algorithm, writing a sub-module to create keywords identifying job-outlines. Keywords roughly outlines the required skills and can be looked/searched upon rather than thoroughly reading whole job-description.

For now, the spider is capable only of storing scraped information locally. Apart from it, the procedures are not yet written to accomplish the next three features.

## Technical Information

---

The crawler is written in Python3-v3.6 and followed framework is scrapy-v1.33. Specifically downloaded dependencies are as follows :

* urllib 
* pymongo 
* selenium
* splinter 
* Chrome Driver \(To support selenium\)

I assumed other dependencies that I may have downloaded earlier or was available to me because of OS or python configurations. I worked on conda virtual environment to manage different dependencies. Refer to the [https://conda.io/docs/install/quick.html](https://conda.io/docs/install/quick.html "Conda Installation") for conda installation and usage.

```
conda list
```

```
# packages in environment at /Users/prithipalsingh/miniconda3/envs/scrapy:
#
attrs                     16.3.0                   py35_1    conda-forge
automat                   0.5.0                    py35_0  
ca-certificates           2017.1.23                     1    conda-forge
certifi                   2017.4.17                py35_0    conda-forge
cffi                      1.10.0                   py35_0    conda-forge
constantly                15.1.0                   py35_0  
cryptography              1.7.1                    py35_0  
cssselect                 1.0.0                    py35_0    conda-forge
hypothesis                3.6.1                    py35_0    conda-forge
icu                       58.1                          1    conda-forge
idna                      2.1                      py35_0    conda-forge
incremental               16.10.1                  py35_0  
libffi                    3.2.1                         3    conda-forge
libiconv                  1.14                          4    conda-forge
libxml2                   2.9.4                         4    conda-forge
libxslt                   1.1.29                        3    conda-forge
lxml                      3.7.3                    py35_0    conda-forge
ncurses                   5.9                          10    conda-forge
openssl                   1.0.2k                        0    conda-forge
parsel                    1.1.0                    py35_0  
pip                       9.0.1                    py35_0    conda-forge
pyasn1                    0.2.3                    py35_0    conda-forge
pyasn1-modules            0.0.8                    py35_0    conda-forge
pycparser                 2.17                     py35_0    conda-forge
pydispatcher              2.0.5                    py35_0    conda-forge
pymongo                   3.3.0                    py35_0  
pympler                   0.5                      py35_0    conda-forge
pyopenssl                 16.2.0                   py35_0    conda-forge
python                    3.5.3                         2    conda-forge
queuelib                  1.4.2                    py35_0  
readline                  6.2                           0    conda-forge
scrapy                    1.3.3                    py35_0    anaconda
selenium                  3.4.1                     <pip>
service_identity          16.0.0                   py35_0  
setuptools                33.1.1                   py35_0    conda-forge
six                       1.10.0                   py35_1    conda-forge
splinter                  0.7.5                     <pip>
sqlite                    3.13.0                        1    conda-forge
tk                        8.5.19                        1    conda-forge
twisted                   17.1.0                   py35_0  
w3lib                     1.17.0                   py35_0  
wheel                     0.29.0                   py35_0    conda-forge
xz                        5.2.2                         0    conda-forge
zlib                      1.2.11                        0    conda-forge
zope                      1.0                      py35_0  
zope.interface            4.3.3                    py35_0
```

These dependencies lays the foundation for the correct working of this crawler and try to match the library version with above in case of faced compatibility issues.

### Setup

---

There are few setup procedures required that vary from system to system. Besides the dependencies, the environment variable should be set in _simple/simple/settings.py. _

```
# MONGODB settings

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'simple_db'
MONGODB_COLLECTION = 'jobitem'

DOWNLOAD_DELAY = 3
```

Change these four variables according to your system's _db_ and corresponding _collection_.  Also it is recommended to keep feasible but large \_DOWNLOAD\_DELAY \_to prevent interference with targeted server's working. [http://stackoverflow.com/questions/8236046/typical-politeness-factor-for-a-web-crawler](http://stackoverflow.com/questions/8236046/typical-politeness-factor-for-a-web-crawler "POLITE CRAWLING")

### Usage

---

* Equip the custom environment using conda and switch to simple/simple/spiders directory where the primary crawler file is located

```
source activate [SCRAPY_ENV_NAME]
cd simple/simple/spiders
```

* Start the crawler 

```
(scrapy) ➜  spiders git:(master) ✗ scrapy crawl makdi -a username=[SFU_USERNAME] -a password=[SFU_PASSWORD]
```

* Following the execution, the initiated http requests by scrapy would be logged on the terminal. The terminal would look like this : 

```
2017-05-09 21:46:02 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:02 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/cookie {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2017-05-09 21:46:03 [selenium.webdriver.remote.remote_connection] DEBUG: GET http://127.0.0.1:59017/session/0b197c095d29f67319ba61deff8b5408/url {"sessionId": "0b197c095d29f67319ba61deff8b5408"}
```

* If the account credentials are correct and everything is in its place, data scrapping starts as demonstrated through below predicted lines in terminal : 

```
INSIDE JOB
PROCESS_ITEM
ITEM INSERTED
INSIDE JOB
PROCESS_ITEM
ITEM INSERTED
CLOSE SPIDER
```

* This completes the crawling. The results would be stored in database _simple\_db_ with collection _jobitem. _

### Contribution

---

Please feel free to fork this repository and modify the data

