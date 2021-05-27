from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=['POST', 'GET'])
def submitForm():

    if request.method == 'POST':
        data = request.form.to_dict()
        email = request.form['email']
        print(data)
        return render_template('thankyou.html', email = email)
    else:
        return 'Something went wrong. Please try again.'



if __name__ == '__main__':
    app.run(debug=True)