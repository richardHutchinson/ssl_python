class HeaderClass(object):
    
    def header(self,title):
        print("Content-type: text/html")
        print
        print("<html><head><title>"+title+"</title></head>")
        print("<body>")