from flask import * #Flask, render_template, request


app = Flask(__name__) # to initiate an instance of Flask app

@app.route('/')

def welcome():
    return render_template('welcome.html')



if __name__ == '__main__':
    app.run(debug=True)
