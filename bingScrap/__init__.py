from bs4 import BeautifulSoup
import json
import urllib
import urllib.request as urllib2


def search(query):
    address = "http://www.bing.com/search?q={}".format(query)

    getRequest = urllib2.Request(address, None, {
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})

    urlfile = urllib2.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()

    soup = BeautifulSoup(htmlResult, 'html.parser')

    [s.extract() for s in soup('span')]
    unwantedTags = ['strong', 'cite']
    for tag in unwantedTags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    data = []

    results = soup.findAll('li', {"class": "b_algo"})
    for result in results:
        title = str(result.find('h2').text).replace(" ", " ")
        snippet = str(result.find('p').text).replace(" ", " ")
        link = result.find("a")['href']
        searchQuery = query


        data.append({
            "title": title,
            "snippet": snippet,
            "url": link,
            "q": searchQuery
        })

    allData = json.dumps(data)
    

    if results == []:
        address = "http://www.bing.com/search?q={}".format(query) + "&qs=n&sp=-1&pq=pen&sc=8-3&sk=&cvid=1A850DDC66AF4543ABDD38DDF1CB9811&first=7&FORM=PERE"
        search(query)

    return allData