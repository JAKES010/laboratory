from __future__ import annotations

from typing import Any

from campusflow.tickets import Ticket, normalize_status

PRIORITY_RANK = {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}


def transition_status(ticket: Ticket, new_status: Any) -> Ticket:
    current_status = normalize_status(ticket.status)
    target_status = normalize_status(new_status)

    if current_status == 'resolved' and target_status != 'open':
        raise ValueError('resolved tickets must be reopened before any other status change')
    if current_status == 'resolved' and target_status == 'open':
        ticket.status = 'open'
        return ticket
    if current_status == 'open' and target_status == 'in_progress':
        if not ticket.assigned_to or not ticket.assigned_to.strip():
            raise ValueError('unassigned tickets cannot move to in_progress')
        ticket.status = 'in_progress'
        return ticket
    if current_status == 'in_progress' and target_status == 'resolved':
        ticket.status = 'resolved'
        return ticket

    raise ValueError(f'invalid status transition from {current_status} to {target_status}')


def build_queue(tickets: list[Ticket]) -> list[Ticket]:
    return sorted(
        [ticket for ticket in tickets if ticket.status != 'resolved'],
        key=lambda ticket: (-PRIORITY_RANK.get(ticket.priority.lower(), 0), int(ticket.id[1:])),
    )
