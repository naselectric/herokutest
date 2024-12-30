from flask import Flask, render_template, request,jsonify
import json

app = Flask(__name__,template_folder="templates")
@app.route('/')
def student():
   return render_template('index.html')

@app.route('/gaming')
def gaming():
   return render_template('gaming pcs.html')



if __name__ == '__main__':
	app.run(debug=True)