from __future__ import annotations

from pathlib import Path

from campusflow.reports import generate_report, format_report
from campusflow.storage import load_tickets, save_tickets
from campusflow.tickets import Ticket, generate_ticket_id
from campusflow.workflow import build_queue, transition_status

DATA_FILE = Path(__file__).resolve().parent / 'data' / 'tickets.json'


def prompt_ticket(existing_tickets):
    title = input('Title: ').strip()
    if not title:
        raise ValueError('title must not be blank')

    category = input('Category [Network/Hardware/Software/Other]: ').strip()
    urgency = input('Urgency [low/medium/high]: ').strip().lower()
    affected_users = input('Affected users: ').strip()

    ticket = Ticket(
        id=generate_ticket_id(existing_tickets),
        title=title,
        category=category,
        urgency=urgency,
        affected_users=affected_users,
        priority='',
        status='open',
        assigned_to=None,
    )
    return ticket


def display_all_tickets(tickets):
    if not tickets:
        print('No tickets found.')
        return

    for ticket in tickets:
        print(f"{ticket.id} | {ticket.title} | {ticket.category} | {ticket.urgency} | users={ticket.affected_users} | priority={ticket.priority} | status={ticket.status} | assigned_to={ticket.assigned_to or 'unassigned'}")


def display_queue(tickets):
    queue = build_queue(tickets)
    if not queue:
        print('No open tickets in the queue.')
        return
    print('Work queue:')
    for ticket in queue:
        print(f"{ticket.id} | {ticket.priority} | {ticket.title} | {ticket.status} | assigned_to={ticket.assigned_to or 'unassigned'}")


def display_report(tickets):
    report = generate_report(tickets)
    print(format_report(report))


def assign_ticket(tickets):
    if not tickets:
        print('No tickets available to assign.')
        return

    display_all_tickets(tickets)
    ticket_id = input('Ticket ID to assign: ').strip().upper()
    target = next((ticket for ticket in tickets if ticket.id.upper() == ticket_id), None)
    if target is None:
        raise ValueError(f'Unknown ticket ID: {ticket_id}')

    assignee = input('Assignee name: ').strip()
    if not assignee:
        raise ValueError('assignee name must not be blank')

    target.assigned_to = assignee
    print(f'Assigned {target.id} to {assignee}.')


def update_status(tickets):
    if not tickets:
        print('No tickets available to update.')
        return

    display_all_tickets(tickets)
    ticket_id = input('Ticket ID to update: ').strip().upper()
    target = next((ticket for ticket in tickets if ticket.id.upper() == ticket_id), None)
    if target is None:
        raise ValueError(f'Unknown ticket ID: {ticket_id}')

    status = input('New status [open/in_progress/resolved]: ').strip().lower()
    transition_status(target, status)
    print(f'Status updated to {target.status}.')


def run_cli():
    try:
        tickets = load_tickets(DATA_FILE)
    except ValueError as exc:
        print(f'Error: {exc}')
        return 1

    while True:
        print('\nCampusFlow Menu')
        print('1. Create ticket')
        print('2. List all tickets')
        print('3. Assign ticket')
        print('4. Update ticket status')
        print('5. Show work queue')
        print('6. Show reports')
        print('7. Exit')

        choice = input('Choose an option: ').strip()

        try:
            if choice == '1':
                ticket = prompt_ticket(tickets)
                tickets.append(ticket)
                save_tickets(DATA_FILE, tickets)
                print(f'Created ticket {ticket.id}: {ticket.title}')
            elif choice == '2':
                display_all_tickets(tickets)
            elif choice == '3':
                assign_ticket(tickets)
                save_tickets(DATA_FILE, tickets)
            elif choice == '4':
                update_status(tickets)
                save_tickets(DATA_FILE, tickets)
            elif choice == '5':
                display_queue(tickets)
            elif choice == '6':
                display_report(tickets)
            elif choice == '7':
                print('Goodbye!')
                return 0
            else:
                print('Please choose a valid option.')
        except ValueError as exc:
            print(f'Invalid input: {exc}')


if __name__ == '__main__':
    raise SystemExit(run_cli())
