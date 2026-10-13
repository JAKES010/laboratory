# AI learning log

## Fellow: Student

### Interaction #1 — JSON persistence
Problem: I needed to understand how JSON round-tripping works in Python without corrupting ticket data.

My initial understanding: JSON files are just text, so I can write a list of dictionaries and load them later.

Prompt to AI: "Explain how json.dump() and json.load() behave in Python, and what happens when the file is missing or malformed. Give a short example unrelated to CampusFlow."

Useful AI guidance: The explanation clarified that missing files should be treated as an empty state, while malformed files should raise an exception so the program can display a clear error instead of silently deleting data.

My independent experiment/test: I wrote a tiny Python example to save and reload a list of dictionaries and then intentionally broke the JSON to confirm `json.JSONDecodeError` is raised.

Verification source or result: The test produced a `JSONDecodeError`, matching the expected Python behavior.

Decision: I accepted the guidance and used it to implement a strict validation rule for malformed JSON in the project.

Related file/commit: `campusflow/storage.py`

What I can now explain without AI: I know that JSON persistence works best when data is converted to a plain Python structure, saved with `json.dump`, and validated on load before use.

### Interaction #2 — Priority logic
Problem: I needed to make sure the priority rules were applied in the correct order and that the first matching rule wins.

My initial understanding: I could just check the conditions in a single if/elif chain and return the first match.

Prompt to AI: "Help me reason through the exact priority rule ordering for a ticketing system. I do not want a final implementation; I want the business logic explained and key edge cases identified."

Useful AI guidance: The AI explained that business rules should be evaluated strictly in order and that high urgency with 10+ users outranks all other high/medium cases.

My independent experiment/test: I checked the boundary cases manually in Python and confirmed that `p = high, users=10` returns `critical` while `p = high, users=9` returns `high`.

Verification source or result: The boundary values matched the requirement.

Decision: I accepted the rule ordering and encoded it directly in the `calculate_priority` function.

Related file/commit: `campusflow/tickets.py`

What I can now explain without AI: I can explain why the priority engine must check the most specific rule first and must never skip to a broader rule.

### Interaction #3 — Status lifecycle validation
Problem: I needed to enforce open -> in_progress -> resolved and reject invalid progressions cleanly.

My initial understanding: A ticket status can change whenever the code says so, but the business rules require a stricter lifecycle.

Prompt to AI: "Explain how to enforce a status workflow in Python so invalid transitions fail clearly without silently mutating data. Give the edge cases to test."

Useful AI guidance: The guidance emphasized checking the current status, validating the new target, and allowing only the required transition path while refusing status changes from a resolved ticket without a reopen.

My independent experiment/test: I tested `open -> in_progress -> resolved` and then `resolved -> in_progress` in a small example table before implementing the workflow functions.

Verification source or result: The workflow rejected the invalid transition and accepted the valid path.

Decision: I improved the first draft by adding explicit validation and using `ValueError` for invalid transitions.

Related file/commit: `campusflow/workflow.py`

What I can now explain without AI: I can describe why resolved tickets must reopen before changing, and how to keep the workflow safe and predictable.
