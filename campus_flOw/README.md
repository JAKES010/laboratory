# CampusFlow

CampusFlow is a lightweight command-line helpdesk app for recording and tracking campus IT support tickets.

## Team
- Engineer A: ticket creation, validation, and priority logic
- Engineer B: assignment, lifecycle workflow, queue, and reporting

## Python setup
This project uses Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Run the CLI
```bash
python main.py
```

Available menu options:
1. Create ticket
2. List all tickets
3. Assign ticket
4. Update ticket status
5. Show work queue
6. Show reports
7. Exit

## Priority rules
The priority engine applies the first matching rule in order:
1. high urgency and 10+ affected users -> critical
2. high urgency or 10+ affected users -> high
3. medium urgency or 3+ affected users -> medium
4. otherwise -> low

## Persistence
Tickets are stored in `data/tickets.json`. If the file does not exist, CampusFlow starts with an empty list. Malformed JSON raises a clear error instead of silently deleting data.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Known limitations
- The app is a terminal CLI and does not provide a web or GUI interface.
- The workflow enforces the required status lifecycle: open -> in_progress -> resolved, with reopen required before status changes from resolved.
