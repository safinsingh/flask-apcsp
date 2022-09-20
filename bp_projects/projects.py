from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/Kalani/')
def Kalani():
    return render_template("Kalani.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/navan/')
def navan():
    return render_template("navan.html")

@app_projects.route('/safin/')
def safin():
    return render_template("safin.html")

@app_projects.route('/AlexsPage/')
def hawkers():
    return render_template("Alexs-Page.html")