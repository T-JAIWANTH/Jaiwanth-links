from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

components = {}

# ERROR LINKS
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html',
    title="Not Found",
    project_name="Linkhub",
    main_heading="404",
    content="The requested URL was not found. Check the URL and try again.",
    stylesheets=[
        "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Poppins&display=swap');</style>", 
        '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'linkhub.css\') }}"></link>'
    ],
    body_classes="font-pop",
    heading_classes="font-hsp",
    content_classes="font-pop",
    subhead_classes="",
    button_classes="rounded-md bg-black text-white",
    components=[
        {
            "type": "heading",
            "label": " "
        },
        {
            "type": "button",
            "label": "Go Back",
            "properties": {
                "link": "history.back()"
            }
        }
    ]
    )

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html',
    title="Internal Server Error",
    project_name="Linkhub",
    main_heading="500",
    content="There was some error with the server. Please try later, or check for errors.",
    stylesheets=[
        "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Poppins&display=swap');</style>", 
        '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'linkhub.css\') }}"></link>'
    ],
    body_classes="font-pop",
    heading_classes="font-hsp",
    content_classes="font-pop",
    subhead_classes="",
    button_classes="rounded-md bg-black text-white",
    components=[
        {
            "type": "heading",
            "label": " "
        },
        {
            "type": "button",
            "label": "Go Back",
            "properties": {
                "link": "history.back()"
            }
        }
    ]
    )
    
# PAGE ENDPOINTS

@app.route('/')
def index():
    with open('data/index.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="Links",
    project_name="Jaiwanth",
    main_heading="T Jaiwanth",
    content="Here are all the links to my socials.",
    stylesheets=["<style>@import url('https://fonts.googleapis.com/css2?family=ADLaM+Display&family=Montserrat&display=swap');</style>", ''],
    body_classes="font-body text-main",
    heading_classes="font-heading text-main",
    content_classes="text-main",
    subhead_classes="font-heading",
    button_classes="bg-main text-white rounded-md",
    components=components
    )

@app.route('/linkedin')
def linkedin():
    return redirect('https://www.linkedin.com/in/jaiwanth-tatuskar-455925260/')

@app.route('/instagram')
def instagram():
    return redirect('https://www.instagram.com/jaiwanth_tatuskar/')

@app.route('/github')
def github():
    return redirect('https://github.com/T-JAIWANTH')

