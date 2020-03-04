from pydantic import BaseModel
from typing import Optional


class SampleInResponse(BaseModel):
    pageNumber: Optional[int] = 1
    pageSize: Optional[int] = 20
    totalCount: int
    listings: list
