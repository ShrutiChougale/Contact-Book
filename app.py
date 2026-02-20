from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

@app.route("/")
def home():
    contacts = load_contacts()
    search_query = request.args.get("search")

    if search_query:
        contacts = {
            k: v for k, v in contacts.items()
            if search_query.lower() in k.lower()
        }

    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add():
    contacts = load_contacts()
    name = request.form["name"].strip()
    phone = request.form["phone"].strip()

    if not phone.isdigit():
        flash("Invalid phone number.")
        return redirect(url_for("home"))

    if name in contacts:
        flash("Contact already exists.")
        return redirect(url_for("home"))

    contacts[name] = phone
    save_contacts(contacts)
    flash("Contact added successfully!")
    return redirect(url_for("home"))

@app.route("/edit/<name>", methods=["GET", "POST"])
def edit(name):
    contacts = load_contacts()

    if request.method == "POST":
        new_phone = request.form["phone"].strip()

        if not new_phone.isdigit():
            flash("Invalid phone number.")
            return redirect(url_for("edit", name=name))

        contacts[name] = new_phone
        save_contacts(contacts)
        flash("Contact updated successfully!")
        return redirect(url_for("home"))

    return render_template("edit.html", name=name, phone=contacts.get(name))

@app.route("/delete/<name>")
def delete(name):
    contacts = load_contacts()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        flash("Contact deleted successfully!")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)