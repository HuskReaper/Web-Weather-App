# Import needed libraries #
import json, urllib
from flask import Flask, render_template, request, abort

# Start Flask App #
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def retrieve_weather():
    # Get weather from the user #
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'texas'
        if city is None:
            abort(400, 'No city arguments')

    # Get API url #
    key = '99fecb1b7254ee49835be17d078926c0'
    full_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key).read()
    list_of_data = json.loads(full_url)
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(round(list_of_data['main']['temp'])) + ' k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "temp_c" : str(round(list_of_data['main']['temp'] - 272.15)) + ' c'
    }
    print(data)
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
