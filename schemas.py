from datetime import datetime

from pydantic import BaseModel


class BenchmarkingResult(BaseModel):
    request_id: str
    prompt_text: str
    generated_text: str
    token_count: int
    time_to_first_token: int
    time_per_output_token: int
    total_generation_time: int
    timestamp: datetime


class AverageResults(BaseModel):
    average_time_to_first_token: int | float
    average_time_per_output_token: int | float
    average_total_generation_time: int | float
