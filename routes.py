from datetime import datetime

from fastapi import APIRouter

from functions import get_db_data, get_average_result
from schemas import AverageResults

prefix = "/results"
router = APIRouter(prefix=prefix)


@router.get(
    "/average",
    response_description="Returns the average performance statistics across "
    "all benchmarking results.",
    response_model=AverageResults,
)
def get_average_results() -> AverageResults:
    try:
        db_data = get_db_data()
        return get_average_result(db_data)
    except RuntimeError as e:
        print(e)


@router.get(
    "/average/{start_time}/{end_time}",
    response_description="Returns the average performance statistics for "
    "benchmarking results within a specified time window.",
    response_model=AverageResults,
)
def get_average_results_by_time(
    start_time: datetime,
    end_time: datetime,
) -> AverageResults:
    try:
        db_data = get_db_data(start_time, end_time)
        return get_average_result(db_data)
    except RuntimeError as e:
        print(e)
