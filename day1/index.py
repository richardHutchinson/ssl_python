#!\Python27\python

#===============================================================================
# import cgi
# 
# cgi.test()
#===============================================================================

# from urlparse import urlparse - rich note: think this will import

import cgi
import views.Header
import views.Footer
import MySQLdb

from models.Views import Views

pars = cgi.FieldStorage()
headerClass = views.Header.HeaderClass()
footerClass = views.Footer.FooterClass()
viewModel = Views()
db = MySQLdb.connect(host="localhost",user="root",passwd="",db="blog")
cur = db.cursor()

# header content and content - headerAndContent(name,content)
headerClass.header("home")

# print("<h1>Home Page</h1>")

#===============================================================================
# views testing - start
#===============================================================================
# from models.Views import Views

# viewModel = Views()

data = {
        "home_title" : "home title works",
        "post_title" : "post title works",
        "something_else" : "something else works",
        "about_title" : "about title works"
        }

# viewModel.getView("about",data)

#===============================================================================
# views testing - end
#===============================================================================

#===============================================================================
# sql testing - start
#===============================================================================

#===============================================================================
# cur.execute("SELECT * FROM post")
# for row in cur.fetchall():
#     print("Title: " + row[1] + "<br />")
#===============================================================================
    
#===============================================================================
# sql testing - end
#===============================================================================

#===============================================================================
# url testing - start
#===============================================================================

if "controller" not in pars:
    con = "home"
    print("<p><strong>" + con + ":</strong><br />- controller <br />- default <br />- page url request</p>")
else:
    con = pars.getvalue("controller")
#     test by using ?controller=someValue in the url
    print("<p>controller <strong>" + con + ":</strong><br />- controller <br />- page url request</p>")
    
if con == "home":
    from controllers.IndexControllers import IndexControllerClass
    IndexControllerClass().getParsValue(pars, data)
elif con == "posts":
    from controllers.IndexControllers import IndexControllerClass
    IndexControllerClass().getParsValue(pars, data)
elif con == "about":
    from controllers.IndexControllers import IndexControllerClass
    IndexControllerClass().getParsValue(pars, data)
else:
    con = "home"
    from controllers.IndexControllers import IndexControllerClass
    IndexControllerClass().getParsValue(pars, data)
    print("<p>controller <strong>" + con + ":</strong><br />- the controllers value is not recognized</p>")

#===============================================================================
# url testing - end
#===============================================================================

# footer content
footerClass.footer()