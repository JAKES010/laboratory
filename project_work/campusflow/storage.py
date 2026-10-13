from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from campusflow.tickets import Ticket


def load_tickets(path: str | Path) -> list[Ticket]:
    file_path = Path(path)
    if not file_path.exists():
        return []

    content = file_path.read_text(encoding='utf-8')
    if not content.strip():
        return []

    try:
        raw_data = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError(f'malformed JSON in {file_path}: {exc.msg}') from exc

    if not isinstance(raw_data, list):
        raise ValueError('ticket data must be stored as a JSON array')

    tickets: list[Ticket] = []
    seen_ids: set[str] = set()
    for item in raw_data:
        ticket = Ticket.from_dict(item)
        if ticket.id in seen_ids:
            raise ValueError(f'duplicate ticket ID detected: {ticket.id}')
        seen_ids.add(ticket.id)
        tickets.append(ticket)
    return tickets


def save_tickets(path: str | Path, tickets: list[Ticket | dict[str, Any]]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    serialised = []
    for ticket in tickets:
        if isinstance(ticket, Ticket):
            serialised.append(ticket.to_dict())
        elif isinstance(ticket, dict):
            serialised.append(Ticket.from_dict(ticket).to_dict())
        else:
            raise ValueError('tickets must be Ticket instances or dictionaries')

    file_path.write_text(json.dumps(serialised, indent=2), encoding='utf-8')
