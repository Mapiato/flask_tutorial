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
    prvni_cislo = request.args.get("prvni_cislo")
    druhe_cislo = request.args.get("druhe_cislo")
    operator = request.args.get("operator")

    if prvni_cislo si None or druhe_cislo is None:
        return render 

if __name__ == "__main__":
    app.run()