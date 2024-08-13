from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/',response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Hello World</h1>
            <a href="/getdetails">Details</a>
        </body>
    </html>
    """
@app.get('/getdetails',response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>VAISHAL A S - 7376221CS339</h1>
        </body>
    </html>
    """