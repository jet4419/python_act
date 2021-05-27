from flask import Flask, render_template
from data import pets

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/")
@app.route("/animals/")
def index(): 
    return render_template('index.html')

@app.route("/animals/<pet_type>/")
def animals(pet_type):

    return render_template('animals.html', pets=pets, pet_type=pet_type, counter=0)

@app.route("/animals/<pet_type>/<int:pet_id>/")
def pet(pet_type, pet_id):

    
    # html = '<h1> Invalid pet. Please try again. </h1>'
    
    # if pet_type in pets:

    #     try:
    #         pet = pets[pet_type][pet_id]
    #         html = '<h1>{}</h1>'.format(pet['name'])
    #         html += '<img src={}>'.format(pet['url'])
    #         html += '<p>{}</p>'.format(pet['description'])
    #         html += '<ul>'
    #         html += '<li>{}</li>'.format(pet['breed'])
    #         html += '<li>{}</li>'.format(pet['age'])
    #         html += '</ul>'
    #     except:
    #         pass
            
    return render_template('pet.html', pets=pets, pet_type=pet_type, pet_id=pet_id, is_valid_pet=pet_id <= (len(pets[pet_type]) -1))
    
if __name__ == '__main__':
    app.run(debug=True)