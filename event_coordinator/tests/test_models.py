"""Unit tests for Event Coordinator models."""

import pytest
from event_coordinator.models import Event, Attendee

def test_attendee_creation():
    """Test creating an attendee."""
    attendee = Attendee(name="John Doe", email="john@example.com")
    assert attendee.name == "John Doe"
    assert attendee.email == "john@example.com"
    assert attendee.status == "registered"

def test_event_creation():
    """Test creating an event."""
    event = Event(name="Tech Conference", date="2025-03-15")
    assert event.name == "Tech Conference"
    assert event.date == "2025-03-15"
    assert event.get_attendee_count() == 0

def test_add_attendee():
    """Test adding attendees to an event."""
    event = Event(name="Meetup", date="2025-02-10")
    attendee = Attendee(name="Jane Smith")
    event.add_attendee(attendee)
    assert event.get_attendee_count() == 1

def test_event_string_representation():
    """Test the string representation of an event."""
    event = Event(name="Workshop", date="2025-01-20")
    assert "Workshop" in str(event)
    assert "2025-01-20" in str(event)
