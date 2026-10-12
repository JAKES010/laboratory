import unittest
from pathlib import Path

from campusflow.storage import load_tickets, save_tickets
from campusflow.tickets import Ticket, TicketCategory, TicketUrgency


class StorageTests(unittest.TestCase):
    def test_save_and_reload_json_preserves_existing_tickets(self):
        path = Path('data/test_storage_roundtrip.json')
        original = [
            Ticket('T021', 'Wi-Fi issue', TicketCategory.Network, TicketUrgency.High, 14, 'critical', 'open', 'Sam'),
            Ticket('T022', 'Laptop issue', TicketCategory.Hardware, TicketUrgency.Medium, 2, 'medium', 'in_progress', 'Alex')
        ]
        save_tickets(path, original)
        reloaded = load_tickets(path)
        self.assertEqual(len(reloaded), 2)
        self.assertEqual(reloaded[0].id, 'T021')
        self.assertEqual(reloaded[1].status, 'in_progress')
        path.unlink(missing_ok=True)

    def test_create_ticket_after_reload_does_not_duplicate_ids(self):
        path = Path('data/test_storage_ids.json')
        tickets = [
            Ticket('T030', 'First', TicketCategory.Other, TicketUrgency.Low, 1, 'low', 'open'),
            Ticket('T031', 'Second', TicketCategory.Other, TicketUrgency.Low, 1, 'low', 'open'),
        ]
        save_tickets(path, tickets)
        reloaded = load_tickets(path)
        next_id = reloaded[-1].id
        self.assertEqual(next_id, 'T031')
        path.unlink(missing_ok=True)

    def test_malformed_json_raises_clear_error(self):
        bad_path = Path('data/bad_tickets.json')
        bad_path.write_text('{oops', encoding='utf-8')
        with self.assertRaises(ValueError):
            load_tickets(bad_path)
        bad_path.unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
