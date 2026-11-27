from composite import Composite
from feuille import Feuille


class ProduitNumerique(Feuille):
    """Un jeu ou un DLC individuel."""

    #pas besoin de __init__ car on ajoute aucun attribut

    def prix_total(self) -> float:
        return self.prix

    def nb_items(self) -> int:
        return 1

    def est_bundle(self) -> bool:
        return False


class Bundle(Composite):
    """Un regroupement de produits numériques ou d'autres bundles."""

    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str, rabais: float = 0.0):
        super().__init__(id, nom, description, prix, nb_ventes, image_url)
        self.rabais = rabais

    #Le prix exact calculé avec tout les enfants et le rabais
    def prix_exact(self) -> float:
        total = sum(enfant.prix_exact() for enfant in self.enfants)
        return total * (1 - self.rabais)

    #le prix exact arrondit a la deuxieme déciamle (prxi affiché dans l'app)
    def prix_total(self) -> float:
        return round(self.prix_exact(), 2)

    def nb_items(self) -> int:
        return sum(enfant.nb_items() for enfant in self.enfants)

    def est_bundle(self) -> bool:
        return True
