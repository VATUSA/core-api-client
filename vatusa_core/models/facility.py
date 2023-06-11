import pydantic
from vatusa_core.models import Controller


class Facility(pydantic.BaseModel):
    id: str
    name: str
    url: str | None
    atm: Controller | None
    datm: Controller | None
    ta: Controller | None
    ec: Controller | None
    fe: Controller | None
    wm: Controller | None
    active: bool

