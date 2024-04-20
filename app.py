from flask import Flask, render_template, url_for, redirect, request, abort

app=Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/login')  
def login():  
    return render_template("login.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        return redirect(url_for("success"))  
    return redirect(url_for("login"))  



@app.route('/success')  
def success():  
    return "logged in successfully"   
@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)