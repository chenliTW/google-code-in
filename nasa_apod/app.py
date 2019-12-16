from flask import Flask,render_template,request
import requests
import pdfkit

api_key=""

app=Flask(__name__)

def get_apod(date):
    res=requests.get("https://api.nasa.gov/planetary/apod?api_key="+api_key+"&date="+date)
    return res.json()

@app.route('/pdf/<file>',methods=["GET"])
def download_pdf(file):
    return app.send_static_file(file)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        data=get_apod(request.form["date"])
        if "code" in data:
            return "404<br>your requested apod not found in NASA",404
        html=render_template("result.html",title=data["title"],date=data["date"],image_url=data["url"],explanation=data["explanation"])
        html_footer="<body></html>"
        pdfkit.from_string(html+html_footer, "static/"+data["date"]+'.pdf')
        return  html+"<center><button  onclick=\"window.open('/pdf/"+data["date"]+".pdf')\">Download as PDF</button></center>"+html_footer

app.run()