from flask import Flask

app = Flask(__name__)

def secti(a, b):
    return float(a) + float(b)

def odecti(a, b):
    return float(a) - float(b)

def podil(a, b):
    return float(a) / float(b)

def soucin(a, b):
    return float(a) * float(b)


@app.route("/", methods = ['GET', 'POST'])
def kalkulacka():
    prvni_cislo = request.form.get("prvni_cislo")
    druhe_cislo = request.form.get("druhe_cislo")
    operator = request.form.get("operator")

    if prvni_cislo is None or druhe_cislo is None:
        return render template("template.html", vysledek="Vyplň formulář")
    if float(druhe_cislo) ==0 and operator == "/":
        vysledek="Nelze dělit nulou"
        return render template("template.html", vysledek=vysledek)
    if (operator=="+"):
        vysledek = secti(prvni_cislo, druhe_cislo)
    elif (operator=="-"):
        vysledek = odecti(prvni_cislo, druhe_cislo)
    elif (operator=="/"):
        vysledek = podil(prvni_cislo, druhe_cislo)
    elif (operator=="*"):
        vysledek = soucin(prvni_cislo, druhe_cislo)
    else:
        vysledek = "Chyba!"

    return render template("kalkulacka.html", vysledek = vysledek)

if __name__ == "__main__":
    app.run(debug=True)