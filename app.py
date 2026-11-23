from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    # Mengecek apakah form dikirim menggunakan method POST
    if request.method == "POST":
        # Parsing parameter berdasarkan atribut 'name' pada input HTML
        nama = request.form.get("nama")
        nim = request.form.get("nim")
        prodi = request.form.get("prodi")

        # Menyimpan hasil parsing ke dictionary untuk dikirim balik ke HTML
        hasil = {
            "nama": nama,
            "nim": nim,
            "prodi": prodi
        }

    return render_template("index.html", hasil=hasil)