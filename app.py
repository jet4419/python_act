from flask import Flask 
from data import pets

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/")
@app.route("/animals/")
def index(): 
    html = '<h1>Adopt a pet!</h1>'
    html = html + '<p>Browse through the links below to find your new furry friend: </p>'
    html = html + '''<ul> 
                    <li><a href='/animals/dogs'>Dogs</a></li>
                    <li><a href='/animals/cats'>Cats</a></li>
                    <li><a href='/animals/rabbits'>Rabbits</a></li> </ul>
                    '''
    
    return html

@app.route("/animals/<pet_type>/")
def animals(pet_type):

    if pet_type in pets:

        html = '<h1>List of {} </h1>'.format(pet_type)
        i = 0
        for i, p in enumerate(pets[pet_type]):
            html += '<ul>'
            html += '<li><a href=/animals/{}/{}>{}</a></li>'.format(pet_type, i, p['name'])
            html += '</ul>'
            i += 1
        

        # for petData in pets[pet_type]:
        #     html = html + f'{petData}'
            # for myPet in petData:
            #     html = html + f'{myPet}'

    else:
        html = '<h1> Invalid pet. Please try again. </h1>'

    return html


@app.route("/animals/<pet_type>/<int:pet_id>/")
def pet(pet_type, pet_id):

    
    html = '<h1> Invalid pet. Please try again. </h1>'
    
    if pet_type in pets:

        try:
            pet = pets[pet_type][pet_id]
            html = '<h1>{}</h1>'.format(pet['name'])
            html += '<img src={}>'.format(pet['url'])
            html += '<p>{}</p>'.format(pet['description'])
            html += '<ul>'
            html += '<li>{}</li>'.format(pet['breed'])
            html += '<li>{}</li>'.format(pet['age'])
            html += '</ul>'
        except:
            pass
            
    return html
    
if __name__ == '__main__':
    app.run(debug=True)