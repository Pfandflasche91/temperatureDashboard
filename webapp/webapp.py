from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hallo/<vorname>')
def hallo(vorname):

     willkommen = {
         'vorname' : vorname,
         'nachname': 'Huber'
         }
         
     return render_template('test.html', **willkommen)
app.run(host="0.0.0.0")