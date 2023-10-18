from pydantic import BaseModel


class Test_data(BaseModel):
    name: str
    description: str | None = None