from typing import Optional
from vatusa_core import api, models


async def get_controller(cid: int) -> models.Controller:
    data = await api.get(f'/controller/{cid}')
    return models.Controller.parse_obj(data)
