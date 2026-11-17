from abc import ABC, abstractmethod
 
class StrategieAffichage(ABC):
    """Contrat commun des stratégies d'affichage du catalogue."""
 
    @abstractmethod
    def formater(self, produit) -> dict:
        """Transforme un produit en dictionnaire prêt pour le gabarit."""


class AffichageCompact(StrategieAffichage):

    def formater(self, produit) -> dict:
        pass

class AffichageDetaille(StrategieAffichage):

    def formater(self, produit) -> dict:
        pass