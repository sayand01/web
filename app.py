from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def hello():
    return render_template("hi.html")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True
            
            
            
            
            )
