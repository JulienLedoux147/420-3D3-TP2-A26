from abc import ABC, abstractmethod
from composant import Composant

@abstractmethod
class Composite(Composant, ABC):
    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str):
        super().__init__(id, nom, description, prix, nb_ventes, image_url)
        self._enfants: list[Composant] = []

    #appeler la méthode comme si c'était un attribut (sans parenthèses)
    #, car on utilise enfants et pas _enfants dans models.py
    @property
    def enfants(self) -> list[Composant]:
        return self._enfants

    def ajouter(self, enfant: Composant) -> None:
        self._enfants.append(enfant)

    def retirer(self, enfant: Composant) -> None:
        self._enfants.remove(enfant)
