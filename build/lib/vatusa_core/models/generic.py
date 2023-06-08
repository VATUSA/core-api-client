from typing import Optional

import pydantic


class GenericResponse(pydantic.BaseModel):
    id: Optional[int]
    success: bool

