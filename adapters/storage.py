"""Contains shared classes for storage adapters, including abstract base class."""

import abc


class DoesNotExist(Exception):
    """Exception to be raised when an entity is not found in storage."""
    pass


class Storage(abc.ABC):
    """Base class for storage adapters."""
    DoesNotExist = DoesNotExist

    @abc.abstractmethod
    def save_partenaire(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_partenaire(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def update_partenaire(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_partenaire(self, *args, **kwargs):
        pass
