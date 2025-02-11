from flask import Flask, render_template, request

app = Flask(__name__) #Flask app wird erstellt

products = [
    {"name": "Labtop", "preis": 999, "bild": "labtop.jpg"},
    {"name": "Handy", "preis": 599, "bild": "handy.jpg"},
    {"name": "Drucker", "preis": 199, "bild": "drucker.jpg"},
    {"name": "Ipad", "preis": 399, "bild": "ipad.jpg"},
    {"name": "Radio", "preis": 699, "bild": "radio.jpg"},
]

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/about")
def about():
        return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Hier kannst du die Nachricht speichern oder per E-Mail versenden
        print(f"Neue Nachricht von {name} ({email}): {message}")

        return "<h2>Danke für deine Nachricht!</h2><p><a href='/'>Zurück</a></p>"
    return render_template("contact.html")

@app.route("/shop")
def shop():
    return render_template("shop.html", products=products)

@app.route("/reviews")
def reviews():
        return render_template("reviews.html")


if __name__ == "__main__": # Flask startet nur wenn die datei direk
    app.run(debug=True, port=5001)  # Startet lokalen Server
