from typing import Optional
from vatusa_core import api, models


async def get_pending_transfers(facility_id: Optional[str] = None) -> list[models.Transfer]:
    pass


async def get_controller_transfers(cid: int) -> list[models.Transfer]:
    pass


async def create_transfer(data: models.CreateTransferRequest):
    pass


async def get_controller_active_holds(cid: int) -> list[models.TransferHold]:
    data = await api.get(f'/transfer/hold/controller/{cid}')
    return [models.TransferHold.parse_obj(rec) for rec in data]


async def create_transfer_hold(data: models.CreateTransferHoldRequest):
    await api.post(f'/transfer/hold', data)


async def update_transfer_hold(data: models.UpdateTransferHoldRequest):
    pass



