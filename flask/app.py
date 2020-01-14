from flask import Flask,request,render_template,url_for,redirect

app=Flask(__name__)

posts=dict()

@app.route('/')
def index():
    return render_template('index.html',posts=posts)

@app.route('/upload',methods=["GET","POST"])
def upload():
    if request.method=="GET":
        return render_template('upload.html')
    elif request.method=="POST":
        file=request.files["file"]
        file.save("./static/"+str(len(posts))+".txt")
        posts["post"]={"title":str(request.form['title']),"path":"./static/"+str(len(posts))+".txt"};
        return redirect(url_for('index'))

@app.route('/static/<filename>')
def get_file(filename):
    return app.send_static_file(filename)

if __name__=="__main__":
    app.run()