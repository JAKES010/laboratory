from __future__ import annotations

from typing import Any

from campusflow.tickets import Ticket


def generate_report(tickets: list[Ticket]) -> dict[str, Any]:
    status_keys = ['open', 'in_progress', 'resolved']
    priority_keys = ['critical', 'high', 'medium', 'low']

    report = {
        'total_tickets': len(tickets),
        'status_breakdown': {status: 0 for status in status_keys},
        'priority_breakdown': {priority: 0 for priority in priority_keys},
    }

    for ticket in tickets:
        status = ticket.status
        priority = ticket.priority.lower()
        if status in report['status_breakdown']:
            report['status_breakdown'][status] += 1
        if priority in report['priority_breakdown']:
            report['priority_breakdown'][priority] += 1

    return report


def format_report(report: dict[str, Any]) -> str:
    lines = [
        f"Total tickets: {report['total_tickets']}",
        'Status breakdown:',
    ]
    for status, total in report['status_breakdown'].items():
        lines.append(f'  {status}: {total}')
    lines.append('Priority breakdown:')
    for priority, total in report['priority_breakdown'].items():
        lines.append(f'  {priority}: {total}')
    return '\n'.join(lines)
