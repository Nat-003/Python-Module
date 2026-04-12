from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def id_check(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("ID does not start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telpathic contact reauire at leat 3 witness")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Signal above 7 should have a message")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)
    print("Valid contact report:")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-03-15T14:30:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.name}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_TEL_009",
            timestamp="2024-05-20T03:00:00",
            location="Sedona, Arizona",
            contact_type=ContactType.telepathic,
            signal_strength=4.2,
            duration_minutes=120,
            witness_count=1,
            is_verified=False
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()