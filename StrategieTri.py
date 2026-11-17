from abc import ABC, abstractmethod
 
class StrategieTri(ABC):
    """Contrat commun des stratégies de tri du catalogue."""
 
    @abstractmethod
    def trier(self, produits: list) -> list:
        """Retourne une nouvelle liste de produits triée."""


class TrierParNom(StrategieTri):

    def trier(self, produits: list) -> list:
        pass

class TrierParPrix(StrategieTri):

    def trier(self, produits: list) -> list:
        pass
    
class TrierParPopulaire(StrategieTri):

    def trier(self, produits: list) -> list:
        pass