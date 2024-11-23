from flask import Flask, request, render_template

app = Flask(__name__)

# Calorie calculation function
def calculate_calories(height, weight, age, gender):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return "Invalid gender provided."
    return bmr

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        age = int(request.form['age'])
        gender = request.form['gender']
        calories = calculate_calories(height, weight, age, gender)
        return f"<h1>Your daily caloric needs are approximately {calories:.2f} kcal</h1>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
