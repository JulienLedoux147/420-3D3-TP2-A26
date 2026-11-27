from abc import ABC, abstractmethod
from models import ProduitNumerique, Bundle
 
class StrategieTri(ABC):
    """Contrat commun des stratégies de tri du catalogue."""
 
    @abstractmethod
    def trier(self, produits: list) -> list:
        """Retourne une nouvelle liste de produits triée."""


class TrierParNom(StrategieTri):

    def trier(self, produits: list) -> list:
        produits_trie = sorted(produits, key=lambda p: p.prix_total())
        return produits_trie

class TrierParPrix(StrategieTri):

    def trier(self, produits: list) -> list:
        produits_trie = sorted(produits, key=lambda p: p.nb_ventes, reverse=True)
        return produits_trie
    
class TrierParPopularite(StrategieTri):

    def trier(self, produits: list) -> list:
        produits_trie = sorted(produits, key=lambda p: p.nom.lower())
        return produits_trie