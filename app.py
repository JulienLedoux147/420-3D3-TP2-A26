from flask import Flask, render_template, request
from catalogue import Catalogue
from StrategieTri import TrierParNom, TrierParPrix, TrierParPopularite
from StrategieAffichage import AffichageCompact, AffichageDetaille

app = Flask(__name__)
catalogue = Catalogue("data/catalogue.json")

# Dictio avec les différentes strat
#font la traduction texte fournit par l'URL --> objet
STRATEGIES_TRI = {
    "nom": TrierParNom(),
    "prix": TrierParPrix(),
    "popularite": TrierParPopularite(),
}

STRATEGIES_AFFICHAGE = {
    "compact": AffichageCompact(),
    "detaille": AffichageDetaille(),
}

@app.route("/")
def index():
    tri = request.args.get("tri", "nom")
    affichage = request.args.get("affichage", "compact")

    # ===== AJOUTER DU CODE ICI POUR INSTANCIER VOS STRATÉGIES APRÈS LE REFACTORING =====
     # Instanciation des stratégies 
    strategie_tri = STRATEGIES_TRI.get(tri, STRATEGIES_TRI["nom"])
    strategie_affichage = STRATEGIES_AFFICHAGE.get(affichage, STRATEGIES_AFFICHAGE["compact"])

    produits = catalogue.afficher_produits(strategie_tri, strategie_affichage) # Ligne à ajuster après le refactoring

    return render_template(
        "catalogue.html",
        produits=produits,
        tri_actif=tri,
        affichage_actif=affichage,
    )


@app.route("/produit/<int:id>")
def detail(id: int):
    produit = catalogue.obtenir(id)
    if produit is None:
        return "Produit introuvable", 404

    return render_template("produit.html", produit=produit)


if __name__ == "__main__":
    app.run(debug=True)
