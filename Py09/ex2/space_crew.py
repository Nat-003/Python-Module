from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mission(self) -> 'SpaceMission':
        experienced_crew = 0
        for c in self.crew:
            if c.years_experience >= 5:
                experienced_crew += 1
        exp_crew_percent = experienced_crew / len(self.crew) * 100
        if not self.mission_id.startswith('M'):
            raise ValueError("Error with this mission")
        if not any(member.rank == Rank.captain or member.rank == Rank.commander for member in self.crew):
            raise ValueError("Mission need at least 1 captain or commander")
        if self.duration_days > 365 and exp_crew_percent < 50:
            raise ValueError("Not enough experienced members")
        if not all(member.is_active for member in self.crew):
            raise ValueError("Not all members are active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)
    print("Valid mission created:")

    crew = [
        CrewMember(
            member_id="SC001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=45,
            specialization="Mission Command",
            years_experience=20,
            is_active=True
        ),
        CrewMember(
            member_id="SC002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=10,
            is_active=True
        ),
        CrewMember(
            member_id="SC003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=28,
            specialization="Engineering",
            years_experience=6,
            is_active=True
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-12-01T08:00:00",
        duration_days=900,
        crew=crew,
        budget_millions=2500.0
    )

    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.name}) - {member.specialization}")

    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        bad_crew = [
            CrewMember(
                member_id="BC001",
                name="Bob Cadet",
                rank=Rank.cadet,
                age=22,
                specialization="Cleaning",
                years_experience=1,
                is_active=True
            ),
        ]
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Mission",
            destination="Jupiter",
            launch_date="2024-06-01T00:00:00",
            duration_days=500,
            crew=bad_crew,
            budget_millions=100.0
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
