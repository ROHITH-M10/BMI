from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calculate():
    height = 0
    weight = 0
    bmi = 0
    if request.method == 'POST' and 'height' in request.form and 'weight' in request.form:
            try:
                height = float(request.form['height'])
                weight = float(request.form['weight'])
                bmi = weight / (height * height)
                return render_template('index.html', bmi= 'Your BMI is: ' + str(bmi))
            except:
                return render_template('index.html', bmi='Please enter a valid height and weight')

    return render_template('index.html')
app.run(debug=True)