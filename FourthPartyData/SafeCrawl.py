from selenium import webdriver
import selenium
import sqlite3 as lite
from urllib.parse import urlsplit

data = [r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\123movies.sqlite', r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\HMDB.sqlite',
        r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\housemovie.sqlite', r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\movie4k.sqlite',
        r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\movierill.sqlite', r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\movietowatch.sqlite',
        r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\PFTV.sqlite', r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\putlocker.sqlite',
        r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\sockshare.sqlite', r'C:\Users\crrat\PycharmProjects\StreamCrawler\fp\watchfree.sqlite']

output = open("SCData.txt", 'w+')

requests = 0
unsafe = 0
requestDict = {}
safeRatio = {}
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(profile)
driver.set_page_load_timeout(10)
driver.set_script_timeout(10)

for db in data:
    print("Site: %s" % db)
    try:
        con = lite.connect(db) #change name of sqlite
    except:
        print("Couldn't connect to DB")
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM http_requests")
        row = cur.fetchone()
    except:
        print("Couldn't fetch row")
    while row != None:
        requests += 1
        site = urlsplit(str(row[1])).hostname # Get site
        if site in requestDict.keys():
            requestDict[site][0] += 1

        else:
            try:
                driver.get("https://www.google.com/transparencyrepot")
                driver.get("https://www.google.com/transparencyreport/safebrowsing/diagnostic/?hl=en#url=" + site)

            except Exception:
                print("Couldn't visit site " + site)

            try:
                element = driver.find_element_by_xpath('//div[not(@class = "hidden")]/p[@id="sends-to-attack-string"]')
            except selenium.common.exceptions.NoSuchElementException:
                dangerous = "safe"
                unsafe += 1
            Status = dangerous
            # Add site to already visited
            requestDict[site] = [1, Status]
            if Status in safeRatio:
                value = safeRatio[Status]
                safeRatio[Status] = value + 1
            else: safeRatio[Status] = 1

        row = cur.fetchone()

    print("Requests :: %s" % requests)
    print("Unsafe :: %s" % unsafe)
    unsafe = 0
    requests = 0

for request in requestDict:
    output.write("%s: [%s, %s]\n" % (request, request[0], request[1]))