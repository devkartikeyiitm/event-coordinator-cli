"""Command-line interface for Event Coordinator."""

import click
from datetime import datetime
from .models import Event, Attendee

@click.group()
@click.version_option()
def main():
    """Event Coordinator CLI - Manage your events efficiently."""
    pass

@main.command()
@click.argument('name')
@click.argument('date')
def create_event(name, date):
    """Create a new event with a name and date."""
    event = Event(name=name, date=date)
    click.echo(f"✓ Event '{name}' created for {date}")

@main.command()
def list_events():
    """List all registered events."""
    click.echo("📋 Events:")
    click.echo("  - Sample Event 1: 2025-01-15")
    click.echo("  - Sample Event 2: 2025-02-20")

@main.command()
@click.argument('event_name')
@click.argument('attendee_name')
def add_attendee(event_name, attendee_name):
    """Add an attendee to an event."""
    attendee = Attendee(name=attendee_name)
    click.echo(f"✓ {attendee_name} added to {event_name}")

if __name__ == '__main__':
    main()
