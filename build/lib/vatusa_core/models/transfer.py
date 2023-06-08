import datetime
from typing import Optional

import pydantic
from .controller import Controller


class CreateTransferRequest(pydantic.BaseModel):
    cid: int
    facility: str
    reason: str
    submitted_by_cid: int
    force: bool = False


class ProcessTransferRequest(pydantic.BaseModel):
    approve: bool
    reason: str
    admin_cid: Optional[int]


class Transfer(pydantic.BaseModel):
    id: int
    controller: Controller
    to_facility: str
    from_facility: str
    reason: str
    created_at: datetime.datetime
    approved: Optional[bool]  # None = Pending, True = Approved, False = Rejected
    approved_by: Optional[int]
    approved_reason: Optional[str]
    approved_at: Optional[datetime.datetime]


class CreateTransferHoldRequest(pydantic.BaseModel):
    cid: int
    hold: str
    start_date: Optional[datetime.datetime]
    end_date: Optional[datetime.datetime]
    created_by_cid: Optional[int]


class UpdateTransferHoldRequest(pydantic.BaseModel):
    end_date: Optional[datetime.datetime] = None
    clear_end_date: Optional[bool] = False
    is_released: Optional[bool] = None
    admin_cid: Optional[int] = None


class TransferHold(pydantic.BaseModel):
    id: int
    controller: Controller
    hold: str
    start_date: Optional[datetime.datetime]
    end_date: Optional[datetime.datetime]
    is_released: bool
    released_by_cid: Optional[int]
    created_by_cid: Optional[int]
