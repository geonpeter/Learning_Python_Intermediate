import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ''
        
    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'book':
            print('-----Book-------')
            # Initialize attributes for each new book
            self.title = ''
            self.author = ''
            self.year = ''

    def characters(self, content):
        # Add to each attribute only if there's non-empty content
        if self.current == 'title':
            self.title += content.strip()
        elif self.current == 'author':
            self.author += content.strip()
        elif self.current == 'year':
            self.year += content.strip()
            
    def endElement(self, name):
        if name == 'title':
            print(f'Title : {self.title}')
        elif name == 'author':
            print(f'Author : {self.author}')
        elif name == 'year':
            print(f'Year : {self.year}')
        self.current = ""  # Reset the current tag

# Setting up the parser and handler
parser = xml.sax.make_parser()
handler = MyHandler()
parser.setContentHandler(handler)

# Parsing the XML file
parser.parse('library.xml')
