from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class TicketCategory(str, Enum):
    Network = 'Network'
    Hardware = 'Hardware'
    Software = 'Software'
    Other = 'Other'

    @classmethod
    def normalize(cls, value: Any) -> str:
        if isinstance(value, cls):
            return value.value
        if value is None:
            raise ValueError('category is required')
        text = str(value).strip()
        mapping = {item.name.lower(): item.value for item in cls}
        mapping.update({item.value.lower(): item.value for item in cls})
        if text.lower() not in mapping:
            raise ValueError('category must be one of: Network, Hardware, Software, Other')
        return mapping[text.lower()]


class TicketUrgency(str, Enum):
    Low = 'low'
    Medium = 'medium'
    High = 'high'

    @classmethod
    def normalize(cls, value: Any) -> str:
        if isinstance(value, cls):
            return value.value
        if value is None:
            raise ValueError('urgency is required')
        text = str(value).strip().lower()
        mapping = {item.name.lower(): item.value for item in cls}
        mapping.update({item.value.lower(): item.value for item in cls})
        if text not in mapping:
            raise ValueError('urgency must be one of: low, medium, high')
        return mapping[text]


VALID_STATUSES = {'open', 'in_progress', 'resolved'}


def normalize_status(value: Any) -> str:
    if value is None:
        raise ValueError('status is required')
    text = str(value).strip().lower().replace(' ', '_')
    if text == 'inprogress':
        text = 'in_progress'
    if text not in VALID_STATUSES:
        raise ValueError('status must be one of: open, in_progress, resolved')
    return text


def validate_title(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError('title must be a string')
    title = value.strip()
    if not title:
        raise ValueError('title must not be blank')
    return title


def validate_affected_users(value: Any) -> int:
    if isinstance(value, bool):
        raise ValueError('affected_users must be a positive integer')
    if isinstance(value, int):
        number = value
    elif isinstance(value, str):
        text = value.strip()
        if not text or not text.isdigit():
            raise ValueError('affected_users must be a positive integer')
        number = int(text)
    else:
        raise ValueError('affected_users must be a positive integer')

    if number <= 0:
        raise ValueError('affected_users must be a positive integer')
    return number


def calculate_priority(urgency: Any, affected_users: Any) -> str:
    normalized_urgency = TicketUrgency.normalize(urgency)
    normalized_users = validate_affected_users(affected_users)

    if normalized_urgency == 'high' and normalized_users >= 10:
        return 'critical'
    if normalized_urgency == 'high' or normalized_users >= 10:
        return 'high'
    if normalized_urgency == 'medium' or normalized_users >= 3:
        return 'medium'
    return 'low'


def generate_ticket_id(existing_tickets: list[Any]) -> str:
    highest = 0
    for ticket in existing_tickets:
        if isinstance(ticket, dict):
            ticket_id = str(ticket.get('id', ''))
        else:
            ticket_id = str(ticket.id)
        if ticket_id.startswith('T') and ticket_id[1:].isdigit():
            value = int(ticket_id[1:])
            highest = max(highest, value)
    return f'T{highest + 1:03d}'


@dataclass
class Ticket:
    id: str
    title: str
    category: Any
    urgency: Any
    affected_users: Any
    priority: str
    status: Any
    assigned_to: str | None = None

    def __post_init__(self) -> None:
        self.title = validate_title(self.title)
        self.category = TicketCategory.normalize(self.category)
        self.urgency = TicketUrgency.normalize(self.urgency)
        self.affected_users = validate_affected_users(self.affected_users)
        if self.priority in (None, ''):
            self.priority = calculate_priority(self.urgency, self.affected_users)
        else:
            self.priority = str(self.priority).strip().lower()
        self.status = normalize_status(self.status)
        if self.assigned_to is not None:
            assignee = str(self.assigned_to).strip()
            self.assigned_to = assignee or None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'Ticket':
        if not isinstance(data, dict):
            raise ValueError('ticket data must be a dictionary')
        return cls(
            id=str(data.get('id', '')),
            title=data.get('title', ''),
            category=data.get('category'),
            urgency=data.get('urgency'),
            affected_users=data.get('affected_users'),
            priority=data.get('priority', ''),
            status=data.get('status', 'open'),
            assigned_to=data.get('assigned_to'),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'urgency': self.urgency,
            'affected_users': self.affected_users,
            'priority': self.priority,
            'status': self.status,
            'assigned_to': self.assigned_to,
        }
