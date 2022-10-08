# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import re
# create a subclass and overshadows the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        if len(attrs)>0:
            for i in attrs:
                print('-> '+i[0]+' > '+str(i[1]))
    def handle_startendtag(self, tag, attrs):
        print (tag)
        if len(attrs)>0:
            for i in attrs:
                print('-> '+i[0]+' > '+str(i[1]))


y=''
for i in range(int(input())):
    y=y+input()
# instantiate the parser
parser = MyHTMLParser()
parser.feed(y)
    
          
