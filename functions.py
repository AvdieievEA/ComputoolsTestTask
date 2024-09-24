import json
from datetime import datetime

from config import DATABASE_NAME, DEBUG
from schemas import BenchmarkingResult, AverageResults


def get_db_data(
    start_time: datetime | None = None,
    end_time: datetime | None = None,
) -> list[BenchmarkingResult]:
    if DEBUG:
        with open(DATABASE_NAME, "r") as file:
            data = json.load(file)
    else:
        raise RuntimeError("Feature is not ready for live yet.")

    return [
        BenchmarkingResult(**result)
        for result in data["benchmarking_results"]
        if (
            start_time is None
            or (
                timestamp := datetime.strptime(result["timestamp"], "%Y-%m-%dT%H:%M:%S")
            )
            >= start_time
        )
        and (end_time is None or timestamp <= end_time)
    ]


def get_average_result(data: list[BenchmarkingResult]) -> AverageResults:
    data_len = len(data)
    time_to_first_token_sum = 0
    time_per_output_token_sum = 0
    total_generation_time_sum = 0

    for b_result in data:
        time_to_first_token_sum += b_result.time_to_first_token
        time_per_output_token_sum += b_result.time_per_output_token
        total_generation_time_sum += b_result.total_generation_time

    average_result = AverageResults(
        average_time_to_first_token=time_to_first_token_sum / data_len,
        average_time_per_output_token=time_per_output_token_sum / data_len,
        average_total_generation_time=total_generation_time_sum / data_len,
    )

    return average_result
