#!\Python27\python

from models.Views import Views

viewModel = Views()

class IndexControllerClass():
    
    def getParsValue(self,pars,data={}):
        
        if "action" not in pars:
            action = "home"
            print("<p><strong>" + action + ":</strong><br />- is working <br />- IndexControllers.py <br />- there is no action</p>")
        else:
            action = pars.getvalue("action")
            
        if action == "home":
            viewModel.getView("home",data)
        elif action == "about":
            viewModel.getView("about",data)
        elif action == "posts":
            viewModel.getView("posts",data)
        else:
            viewModel.getView("home",data)
            print("<p><strong>" + action + ":</strong><br />- the action value is not recognized</p>")