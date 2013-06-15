#===============================================================================
# importing files
# http://docs.python.org/2/library/os.path.html
#===============================================================================
# from os.path import isfile
from ntpath import isfile
from string import Template

class Views:
    
    def __init__ (self):
        self.basePath = "views/"
        
    def getView(self, fileName, data={}):
        fullPathToView = self.basePath + str(fileName) + ".py"
#         print(fullPathToView)

#         print(fullPathToView + " this is the path")
        
        if isfile(fullPathToView):
            fileHandle = open(fullPathToView)
#             print(fileHandle)

            for line in fileHandle:
                print(Template(line).substitute(data))
                      #=========================================================
                      # Template(line).substitute(
                      #                           post_title = data['post_title'],
                      #                           something_else = data['something_else']
                      #                           )
                      # )
                      #=========================================================
