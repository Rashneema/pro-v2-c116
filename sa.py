from flask import Flask, render_template
app = Flask(__name__)

#in the function return render_template(‘index.html’)

@app.route("/sa")
def student_webpage():
    #Create a variable
    name = 'John'
    # Pass the variable in the template
    return render_template('sa_index.html', student_name = name)
app.run(debug=True)