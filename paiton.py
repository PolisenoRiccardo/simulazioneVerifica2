import datetime
from flask import Flask, render_template
app = Flask(__name__)

def sfondo(oras):
        if oras < 12 and oras > 5:
          return 'mattino'
        elif oras > 12 and oras < 18:
         return 'pomeriggio'
        else: 
         return 'notte'

@app.route('/')
def home():    
   return render_template("tour.html", img1 = "static/images/persona.jpg", img2 = "static/images/gruppo.jpg", img3 = "static/images/guida.jpg", tasto1 = "/singolo", tasto2 = "/gruppo", tasto3 = "/guida", ora = sfondo(datetime.datetime.now().hour))

@app.route('/singolo')
def singolo():
    return render_template("tour.html", img1 = "static/images/esc.jpg", img2 = "static/images/10$.jpg", img3 = "static/images/blanc.jpg", tasto1 = "/", tasto2 = "/singolo", tasto3 = "/singolo", ora = sfondo(datetime.datetime.now().hour))

@app.route('/gruppo')
def gruppo():
    return render_template("tour.html", img1 = "static/images/esc.jpg", img2 = "static/images/8.jpg", img3 = "static/images/blanc.jpg", tasto1 = "/", tasto2 = "/gruppo", tasto3 = "/gruppo", ora = sfondo(datetime.datetime.now().hour))

@app.route('/guida')
def guida():
    return render_template("tour.html", img1 = "static/images/esc.jpg", img2 = "static/images/12$.jpg", img3 = "static/images/blanc.jpg", tasto1 = "/", tasto2 = "/guida", tasto3 = "/guida", ora = sfondo(datetime.datetime.now().hour))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)