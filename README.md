# What is Spin
Spin is a framework for building and running event-driven microservice applications with WebAssembly (Wasm) components.

# Spin Templete

spin templete is the layer of Spin-python-sdk for render html

# How to install spin_templete

```python
pip install spin_templete
```

### setup
```
mkdir templete
cd templete
touch index.html
```
### index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World Again Momin</h1>

    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>   
    <ul>
        {% for item in mylist %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>   



<h1>{{name}}</h1>

</body>
</html>
```

### app.py
```python
from spin_sdk.http import IncomingHandler, Request, Response
from spintemplete.templete import Render


html = Render("templete")

class IncomingHandler(IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        return html.render("index.html",items=[1,2,3,4,5],mylist=["hello","world"],name="momin")
```

### spin.toml
Add more html files your requirements
```

[component.myapp]
source = "app.wasm"
files = ["templete/index.html"]
```

Check Our Site : https://mefiz.com/about </br>
Developed by : Momin Iqbal