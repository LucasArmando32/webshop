import os

from flask import render_template, request, jsonify, Flask
from together import Together

# Flask-App erstellen
app = Flask(__name__)

api_key = "4cc0d80375fbfba2ef6997fedbe92892d746e8475f2a7a21514db4b42ef70f53"  # API-Key
client = Together(api_key=api_key)
#produkt Liste
products = [
    {"name": "Labtop", "preis": 999, "bild": "labtop.jpg"},
    {"name": "Handy", "preis": 599, "bild": "handy.jpg"},
    {"name": "Drucker", "preis": 199, "bild": "drucker.jpg"},
    {"name": "Ipad", "preis": 399, "bild": "ipad.jpg"},
    {"name": "Radio", "preis": 699, "bild": "radio.jpg"},
]

@app.route("/") #Wenn jemand die Startseite aufruft dann führe home aus und home ist als index.html definiert
def home():
        return render_template("index.html")

@app.route("/about")
def about():
        return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"]) #contact route verarbeitet 2https methoden GET sowie POST anfragen
#Post wird verwendet um das kontaktformular abzuschicken GET wenn der Benutzer die kontaktseite aufruft
def contact():
    if request.method == "POST": #ist es eine post anfrage dann wird das formular abgeschickt
        name = request.form["name"] #holt den wert des Eingabefelds name und speichert sie in variablen
        email = request.form["email"]
        message = request.form["message"]

        # Hier kannst du die Nachricht speichern oder per E-Mail versenden
        #print(f"Neue Nachricht von {name} ({email}): {message}")

        return "<h2>Danke für deine Nachricht!</h2><p><a href='/'>Zurück</a></p>" #gibt eine Nachricht zurück wenn die request method POST ist
    return render_template("contact.html") #Die template wird gezeigt

@app.route("/shop")
def shop():
    return render_template("shop.html", products=products) #Eine liste von Produkten wird der template übergeben

@app.route("/reviews")
def reviews():
        return render_template("reviews.html")



@app.route("/customer_service", methods=["GET", "POST"])
def customer_service():
    if request.method == "GET":
        return render_template("customer_service.html")

    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Keine Nachricht erhalten!"}), 400

    user_input = data["message"]
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": user_input}]
    )

    bot_response = response.choices[0].message.content
    return jsonify({"response": bot_response})


if __name__ == "__main__": # Flask startet nur wenn die datei direk
    app.run(debug=True, port=5001)  # Startet lokalen Server
