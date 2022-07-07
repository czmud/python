from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def success():
    return "Dojo"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    return "Hi " + name.title()+"!"
@app.route('/repeat/<repeat_count>/<message>/') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(repeat_count, message):
    webpage_message = ''
    for i in range(int(repeat_count)):
        webpage_message += message+'\n'
    print(webpage_message)
    return webpage_message
@app.route('/<path_not_found>')
def error_message(path_not_found):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
