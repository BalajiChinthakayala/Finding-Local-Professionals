from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for professionals
professionals = [
    {"name": "John Doe", "location": "New York", "domain": "Plumber"},
    {"name": "Jane Smith", "location": "Los Angeles", "domain": "Electrician"},
    {"name": "Michael Johnson", "location": "Chicago", "domain": "Carpenter"},
    {"name": "Emily Brown", "location": "Houston", "domain": "Painter"},
    {"name": "David Wilson", "location": "Miami", "domain": "Handyman"},
]

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for search results
@app.route('/results', methods=['POST'])
def results():
    location = request.form.get('location')
    domain = request.form.get('domain')
    
    # Filter professionals based on location and domain
    filtered_professionals = [prof for prof in professionals if prof['location'].lower() == location.lower() and prof['domain'].lower() == domain.lower()]
    
    return render_template('results.html', professionals=filtered_professionals, location=location, domain=domain)

if __name__ == '_main_':
    app.run(debug=True)