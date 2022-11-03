from flask import Flask,request,render_template
import temp
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        link = request.form['searchbox']
        return temp.func(link)
    else:
        return render_template('analysis.html')


if __name__ == "__main__":
    app.run(debug=True)
