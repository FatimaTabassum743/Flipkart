from flask import Flask,render_template
students=["Harinia","manikandan","rithika","preethi"]
app=Flask(__name__)
@app.route("/",methods=["GET"])

def portfolio():
    return render_template("index.html",names=students)
@app.route("/contact",methods=["GET"])
def contact():
    return  render_template("contact.html",names=students)
if __name__=="__main__":
    app.run(debug=True)