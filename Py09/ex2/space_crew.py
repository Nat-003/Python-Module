from pidantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class SpaceCrew(Enum):
    cadet = 1
    officier = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=3, max_length=10)
    rank: Enum
    age: int = Field(ge=18, le=50)
    specialization: str = Field(min_length=3, max_length=30)
    years_experiance: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    lauch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list = Field(ge=1, le=12)
    mission_status: str = Field(default="planned")
    budget_million: float = Field(ge=1.0, le=1000.0)

    @model_validator(mode='after')
    def check_mission(self) -> SpaceMission:
        if not self.mission_name.startswith('M'):
            raise ValueError("Error with this mission")
        if not for x in 
