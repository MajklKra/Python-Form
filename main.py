
import webbrowser
import os

# Spustí jednoduchý HTTP server ve složce, kde máte index.html
import http.server
import socketserver
import webbrowser

import os
from pathlib import Path

PORT = 8000     # číslo portu

# Objektová reprezentace HTML elementů

class Label:
    def __init__(self, for_type='', style='', text=''):
        self.for_type = for_type
        self.style = style
        self.text = text

    def render(self):
        return f'<label for="{self.for_type}" style="{self.style}"> {self.text} </label>'


class Input:
    def __init__(self, input_type, id, name, placeholder='', value='', style=''):
        self.input_type = input_type
        self.id = id
        self.name = name
        self.placeholder = placeholder
        self.value = value
        self.style = style

    def render(self):
        return f'<input type="{self.input_type}" id="{self.id}" name="{self.name}" placeholder="{self.placeholder}" value="{self.value}" style="{self.style}">'


class Select:
    def __init__(self, name, id, style, options=None):
        if options is None:
            options = []
        self.name = name
        self.id = id
        self.style = style
        self.options = options

    def render(self):
        options_html = ''.join([f'<option value="{opt["value"]}">{opt["label"]}</option>' for opt in self.options])
        return f'<select name="{self.name}" id="{self.id}" style="{self.style}">{options_html}</select>'


class Anchor:
    def __init__(self, href, text, style, id):
        self.href = href
        self.text = text
        self.style = style
        self.id = id

    def render(self):
        return f'<a href="{self.href}" style="{self.style}" id = "{self.id}" >{self.text}</a>'

class Image:
    def __init__(self, src, alt, width, height, style):
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height
        self.style = style

    def render(self):
        return f'<img src="{self.src}" alt="{self.alt}" width="{self.width}" height="{self.height}" style="{self.style}">'


class Button:
    def __init__(self, text, style):
        self.text = text
        self.style = style
    

    def render(self):
        return f'<button style="{self.style}" onclick="this.innerText=\'Clicked!\'">{self.text}</button>'

class Div:
    def __init__(self, elements, id='', class_name='', style=''):
        self.elements = elements
        self.id = id
        self.class_name = class_name
        self.style = style

    def render(self):
        content_html = ''.join([element.render() for element in self.elements])
        return f'<div id="{self.id}" class="{self.class_name}" style="{self.style}">{content_html}</div>'


class Form:
    def __init__(self, action, method, content, style):
        self.action = action
        self.method = method
        self.content = content
        self.style = style

    def render(self):
        return f'<form action="{self.action}" method="{self.method}" style="{self.style}">{self.content}</form>'


# Vytvoření instancí jednotlivých elementů
label1 = Label('fname', "margin-top: 1rem; margin-right: 1rem;", 'Křestní&nbspjméno:' )
name1 = Input('text', 'fname','fname', 'Křestni jmeno', 'Michal','width:100%; margin-right: 1rem; margin-bottom: 1rem;')

label2 = Label('lname','margin-top: 1rem; margin-right: 1rem;', 'Příjmení:')
name2 = Input('text', 'lname','lname', 'Příjmení:', 'Kraninger','width:100%; margin-bottom: 1rem;')

label3 = Label('jobs', 'margin-top: 1rem; margin-right: 1rem;', 'Pracovní pozice:')

jobs_select = Select('jobs', 'jobs', 'margin-bottom: 1rem; width:100%', [
    {'value': 'IT', 'label': 'Programátor'},
    {'value': 'SAF', 'label': 'Technik BOZP'},
    {'value': 'TEA', 'label': 'Učitel'},
    {'value': 'UN', 'label': 'Nezaměstnaný'}
])

label4 = Label('a1', 'margin-top: 1rem; margin-right: 1rem;', 'Odkaz:')
link = Anchor('http://www.majkl.jecool.net/', 'Navštivte Majkl.jecool.net!','display:block;', 'a1')
img = Image('http://www.majkl.jecool.net/images/foto.jpg', 'Me','200px','','display:block; margin: 3rem auto; border-radius: 5px;')

##submit_button = Button(text="Submit - Bottom", style='margin: 1rem auto; width:100px; height:40px;')

submit = Input('submit','s','s', 'Submit', 'Submit','display:block;margin: 1rem auto; width:100px; height:40px;') 


# Vytvoření formuláře s vloženými elementy
form_content = ''.join([
    label1.render(), name1.render(), 
    label2.render(), name2.render(), 
    label3.render(), jobs_select.render(),
    label4.render(), link.render(), 
    img.render(), submit.render()  
])

##form = Form('/submit', 'POST', form_content, '')

form = Form('', '', form_content, '')


# Vložení formuláře do divu
div = Div([form], 'd1', 'container', 'display: flex; flex-direction: column; justify-content: center; align-items: center; margin-top: 3rem;')

# Výpis HTML formuláře
print(div.render())

x = div.render()

##print(x)

## vytvoření html souboru
with open("index.html", "w", encoding="utf-8") as file:
    html_content = """
    <!DOCTYPE html>
    <html lang="cs">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Moje Stránka</title>
        <link rel="stylesheet" href="styles.css">
        
        <style>
            @media screen and (max-width: 300px) 
            {

                #d1{
                    width:200px;margin: 1rem auto;
                }
                 
            
                body{
                 background-color: green;
                  display: flex; flex-direction: column; justify-content: center; align-items: center; 
                 }  
            }

            @media screen and (min-width: 301px)and (max-width: 400px) 
            {

                    #d1{
                        width:200px;margin: 1rem auto;
                    }
            
                    body{
                     background-color: purple;
                      display: flex; flex-direction: column; justify-content: center; align-items: center; 
                     }  
            }


            @media screen and (min-width: 401px) and (max-width: 575px) 
            {
                #d1{
                    width:200px;margin: 1rem auto;
                }

            
                body{
                 background-color: blue;
                  display: flex; flex-direction: column; justify-content: center; align-items: center; 
                 }  
            }

            @media screen and (min-width: 576px) and (max-width: 767px) 
            {
                    #d1{
                        width:200px;margin: 1rem auto;
                    }
            
                    body{
                     background-color: white;
                      display: flex; flex-direction: column; justify-content: center; align-items: center; 
                     }  
            }

            @media screen and (min-width: 767px) and (max-width: 991px) 
            {

                #d1{
                    width:200px;margin: 1rem auto;
                }
            
                 body{
                  background-color: orange;
                   display: flex; flex-direction: column; justify-content: center; align-items: center; 
                  }  
            }

            @media screen and (min-width: 992px) and (max-width: 1199px) 
            {

                #d1{
                    width:200px;margin: 1rem auto;
                }
                
                body{
                 background-color: yellow;
                  display: flex; flex-direction: column; justify-content: center; align-items: center; 
                 }  
            }

            @media screen and (min-width: 1200px)
            {

                    #d1{
                        width:200px;margin: 1rem auto;
                    }
            
                 body{
                 background-color: red;
                  display: flex; flex-direction: column; justify-content: center; align-items: center; 
                 }    
            }
        </style>
        
    </head>
    <body style="background-color:antiquewhite">
        <header>
            <h1><b>Vítejte na mé stránce</b></h1>
        </header>
        <main>
            <p style="font-style: italic;">Toto je ukázková stránka vytvořená pomocí Pythonu.</p>
            """ + x + """

        </main>
        <footer>
            <p>&copy; 2024 Michal Kraninger</p>
        </footer>
    </body>
    </html>
    """
    file.write(html_content)
print("Soubor index.html byl vytvořen.")


current_directory = os.getcwd()
print("Aktuální pracovní složka:", current_directory)

# Získání cesty do adresáře, kde je index.html

DIRECTORY = current_directory

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server běží na http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}/index.html")  # Otevře stránku v prohlížeči
    httpd.serve_forever()



