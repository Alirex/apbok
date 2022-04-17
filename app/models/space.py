from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.object_ import Object_


class Space:
    """
    `Space` is something that contains `objects`.
    """
    content: set['Object_']
