from flask import * #Flask, render_template, request


app = Flask(__name__) # to initiate an instance of Flask app

@app.route('/')

def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')

'''if __name__ == '__main__':
    app.run(debug=True)'''
