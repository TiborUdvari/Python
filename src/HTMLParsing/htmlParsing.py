#Fetching a web page
import urllib.request
from html.parser import HTMLParser

class TibiHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)
        
parser = TibiHTMLParser(strict=False)
parser.reset()
parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')


#f = urllib.request.urlopen("http://www.nytimes.com/2012/03/26/us/in-supreme-court-health-care-case-training-for-a-legal-marathon.html?_r=1&hp")
#read from object 
#s = f.read()
#print(s)

#f.close()