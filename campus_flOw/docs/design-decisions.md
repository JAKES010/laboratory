# Design decisions

## Shared ticket model
- The project stores each ticket as a Python dictionary-like dataclass object called `Ticket`.
- This keeps validation and priority logic close to the data and makes JSON round-tripping straightforward.

## Input validation contract
- `Ticket` validates the title, category, urgency, and affected_users immediately in `__post_init__`.
- Invalid values raise `ValueError`, and the CLI catches those exceptions and shows a user-facing error without writing bad data.

## Workflow ownership
- `campusflow/workflow.py` owns lifecycle transitions and queue ordering.
- `campusflow/reports.py` owns status and priority reporting.
- `campusflow/storage.py` owns loading and writing JSON.

## Persistence contract
- Save operations write all tickets to `data/tickets.json`.
- Load operations return an empty list if the file is absent and raise a clear error if the file contains malformed JSON.
- Ticket IDs are generated using the next numeric suffix after the highest existing `T###` number.
