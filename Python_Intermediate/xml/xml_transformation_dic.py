import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ''
        self.myproduct = []  # List of products (dictionaries)
        self.current_product = {}  # Temporary dictionary for each product
        
    def startElement(self, name, args):
        self.current = name
        if self.current == 'product':
            print('------Product------')
            # Reset the current product data at the start of each new product
            self.current_product = {}

    def characters(self, content):
        # Store content for each tag (id, name, price)
        if self.current == 'id':
            self.current_product['id'] = content.strip()  # Strip spaces
        elif self.current == 'name':
            self.current_product['name'] = content.strip()
        elif self.current == 'price':
            self.current_product['price'] = content.strip()

    def endElement(self, name):
        if name == 'product':  # When a full product is read, add it to the list
            self.myproduct.append(self.current_product)
        self.current = ''  # Reset current tag after each element

    def print_elements(self):
        # Print the collected products
        for e in self.myproduct:
            print(e)

# Set up the handler and parser
handler = MyHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)

# Parse the XML file
parser.parse(r'C:\Users\igeon\Desktop\DataMine\NeuralNine\Python_Intermediate\xml\products.xml')

# Print the results after parsing
handler.print_elements()
