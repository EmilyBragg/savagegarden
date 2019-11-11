from flask import Flask
import util 

app = Flask(__name__)

@app.route('/')
def index():
    return util.data_page()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
        
