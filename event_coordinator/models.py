"""Data models for Event Coordinator."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import uuid4

@dataclass
class Attendee:
    """Represents an event attendee."""
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))
    email: Optional[str] = None
    phone: Optional[str] = None
    status: str = "registered"
    
    def __str__(self) -> str:
        return f"{self.name} ({self.status})"

@dataclass
class Event:
    """Represents an event."""
    name: str
    date: str
    id: str = field(default_factory=lambda: str(uuid4()))
    location: Optional[str] = None
    attendees: List[Attendee] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    
    def add_attendee(self, attendee: Attendee) -> None:
        """Add an attendee to the event."""
        self.attendees.append(attendee)
    
    def get_attendee_count(self) -> int:
        """Get the total number of attendees."""
        return len(self.attendees)
    
    def __str__(self) -> str:
        return f"{self.name} on {self.date} ({self.get_attendee_count()} attendees)"
