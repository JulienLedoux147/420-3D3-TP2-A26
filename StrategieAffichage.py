from abc import ABC, abstractmethod
 
class StrategieAffichage(ABC):
    """Contrat commun des stratégies d'affichage du catalogue."""
 
    @abstractmethod
    def formater(self, produit) -> dict:
        """Transforme un produit en dictionnaire prêt pour le gabarit."""


class AffichageCompact(StrategieAffichage):

    def formater(self, produit) -> dict:
        return {
            "id": produit.id,
            "nom": produit.nom,
            "prix_total": produit.prix_total(),
            "image_url": produit.image_url,
            "est_bundle": produit.est_bundle(),
        }

class AffichageDetaille(StrategieAffichage):

    def formater(self, produit) -> dict:
        donnees = {
            "id": produit.id,
            "nom": produit.nom,
            "prix_total": produit.prix_total(),
            "image_url": produit.image_url,
            "description": produit.description,
            "nb_ventes": produit.nb_ventes,
            "est_bundle": produit.est_bundle(),
        }
        if produit.est_bundle():
            donnees["nb_items"] = produit.nb_items()
        return donnees