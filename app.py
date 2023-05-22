from flask import Flask, render_template, request, jsonify
import dijkstra as dij


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_route', methods=['POST'])
def search_route():
    from_station = request.form['from_station']
    to_station = request.form['to_station']

    # Ici, vous pouvez ajouter la logique pour rechercher l'itinéraire entre les deux gares
    # Pour cet exemple, je vais simplement renvoyer un itinéraire fictif
    result = {
        'route': f"Itinéraire de {from_station} à {to_station}: {from_station} -> {to_station}"
    }
    
    return jsonify(result)

@app.route('/route')
def route():
    return render_template('route.html')

if __name__ == '__main__':
    app.run(debug=True)
