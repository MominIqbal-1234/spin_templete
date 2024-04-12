# import os
# from spin_sdk.http import Response
# from jinja2 import Template
# import json

# class Render:
    
#     def __init__(self,templete:str,static:str=None) -> None:
        
#         self.templete = templete
#         self.static = static


#     def render(self,htmlFileName:str,**args):
        
#         self.filePath:str = os.path.join(self.templete,htmlFileName)
#         template = Template(self.loadFile())
#         self.res = template.render(args)

#         return self.response("text/html")
    
#     def response(self,type:str):
#         return Response(200,{"content-type": type},bytes(f"{self.res}", "utf-8"))


#     def loadFile(self):
#         with open(self.filePath,'r') as file:
#             return file.read()

#     def loadJson(self,JsonFileName):
#         self.filePath:str = os.path.join(self.templete,JsonFileName)
#         self.res =  json.loads(self.loadFile)
#         return self.response("text/json")

#     def loadStatic(self,FileName):
#         self.filePath:str = os.path.join(self.static,FileName)
#         return self.filePath




import os
from jinja2 import Template
import json
from spin_sdk.http import Response

class Render:
    """
    The Render class is designed to facilitate rendering HTML templates,
    loading JSON
    """

    def __init__(self, template: str) -> None:
        """
        Initializes a new instance of the Render class with specified html template folder

        Args:
        template folder path
        """
        self.template = template

    def render(self, htmlFileName: str, **args):
        """
        Renders an HTML using the specified arguments.
        """
        
        self.filePath: str = os.path.join(self.template, htmlFileName)
        template = Template(self.loadFile())
        self.res = template.render(args)

        return self.response("text/html")
    
    def response(self, type: str):
        """
        Creates a response object for the rendered content.
        """
        return Response(200, {"content-type": type}, bytes(f"{self.res}", "utf-8"))

    def loadFile(self):
        """
        Reads and returns the content of the file
        """
        with open(self.filePath, 'r') as file:
            return file.read()

    def loadJson(self, JsonFileName):
        """
        Loads a JSON file
        """
        self.filePath: str = os.path.join(self.template, JsonFileName)
        self.res = json.loads(self.loadFile())

        return self.response("text/json")

    def loadStatic(self, FileName):
        """
        Constructs the file path for a static file and returns it.
        """
        self.filePath: str = os.path.join(self.static, FileName)
        
        return self.filePath
