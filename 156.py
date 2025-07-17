from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_voting():
    result = ""
    if request.method == 'POST':
        age = int(request.form['age'])
        if age >= 18:
            result = "You are eligible to vote."
        else:
            result = "You are not eligible to vote."
    return render_template('vote.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
