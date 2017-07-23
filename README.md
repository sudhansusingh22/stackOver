## stackOver
Webcrawler for stackoverflow questions sorted by Newest first. </br>

### Objective:
Extracts the following information from Stackoverflow:
* Question Title 
* Question URL 
* Username, who posted the question 
* User URL 

* Save the details to MongoDB collection.

### Requirements:
* Scrapy
* pyMongo

### Steps to Run: 
```python
scrapy crawl stack
```

### Sample output: 
```json
'title'     : u'Is there a reason that many database admins use sizes of 2^n when creating database tables?', </br>
'url'       : u'/questions/37281799/is-there-a-reason-that-many-database-admins-use-sizes-of-2n-when-creating-datab', </br>
'userName'  : u'jros',</br>
'userUrl'   : u'/users/5095731/jros' </br>
```

##### Ref : https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/
