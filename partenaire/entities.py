import attr
from core.entities import Entity


@attr.s(frozen=True)
class PartenaireEntity(Entity):
    """Partenaire are where users put the useful knowledge they need to save & share."""
    id = attr.ib(default=None)
    name = attr.ib(default=None)
    email = attr.ib(default=None)
    website = attr.ib(default=None)
    description = attr.ib(default=None)
    phone_number = attr.ib(default=None)
    is_suspend = attr.ib(default=False)

