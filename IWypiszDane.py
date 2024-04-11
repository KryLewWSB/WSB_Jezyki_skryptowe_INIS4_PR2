from abc import ABC, abstractmethod

class IWypiszDane(ABC):
  """Definiuje interfejs dla modułów."""
  @abstractmethod
  def wypiszPersonalia(self):
    """Metoda 1, która musi być zaimplementowana przez klasy implementujące interfejs."""
    pass
