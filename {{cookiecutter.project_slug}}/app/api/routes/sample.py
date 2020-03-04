from fastapi import APIRouter

from app.core.paginator import pagenation
from app.models.sample import SampleInResponse
from app.services.sample import get_sample
import requests

router = APIRouter()


@router.get("/sample", response_model=SampleInResponse, name="sample:get-data")
async def sample(
    page_number: int = 1, page_size: int = 20, start_page_as_1: bool = True
):
    dataset = requests.get("https://api.punkapi.com/v2/beers?brewed_before=11-2012&abv_gt=6")
    data_json = dataset.json()
    data = get_sample(data_json)

    total_count = len(data)
    result = pagenation(page_number, page_size, total_count, data, start_page_as_1)

    return SampleInResponse(
        pageNumber=page_number,
        pageSize=page_size,
        totalCount=total_count,
        listings=result["listings"],
    )

