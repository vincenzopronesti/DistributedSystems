from flask import Flask
from flask import render_template
from flask import request

from plotting import plot_function


app = Flask(__name__)


# TODO: State should not be here!!
counter = 0
last_plot = (None, None)


@app.route('/')
def home():
    return render_template('home.html', count=counter, message='', lastfigure=last_plot[0], lastuser=last_plot[1])

def is_valid (request, field):
    return field in request.form and len(request.form[field]) > 0


@app.route('/plot', methods=['POST'])
def request_plot():
    global counter
    global last_plot

    if not is_valid(request, "name") or not is_valid(request, "function"):
        return render_template('home.html', count=counter, message='Invalid request: a function and a user name must be provided!') 

    name = request.form['name']
    function = request.form['function']
    
    xmin,xmax = (0,10)
    try:
        if is_valid(request, "xmin"):
                xmin = float(request.form['xmin'])
        if is_valid(request, "xmax"):
                xmax = float(request.form['xmax'])
    except:
        pass # TODO: handle error...

    try:
        plot_base64 = plot_function (function, xmin, xmax)

        # Update state...
        counter = counter + 1
        last_plot = (plot_base64, name)

        return render_template('plot.html', user=name, image=plot_base64)
    except Exception as e:
        print(e)
        return render_template('home.html', count=counter, message='Could not plot the function.') 
    


