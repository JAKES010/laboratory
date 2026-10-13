import unittest

from campusflow.tickets import Ticket, TicketCategory, TicketUrgency
from campusflow.workflow import build_queue, transition_status


class WorkflowTests(unittest.TestCase):
    def test_unassigned_ticket_cannot_move_to_in_progress(self):
        ticket = Ticket('T010', 'Login issue', TicketCategory.Software, TicketUrgency.High, 5, '', 'open', None)
        with self.assertRaises(ValueError):
            transition_status(ticket, 'in_progress')

    def test_assigned_ticket_can_progress_through_lifecycle(self):
        ticket = Ticket('T011', 'Login issue', TicketCategory.Software, TicketUrgency.High, 5, '', 'open', 'Alex')
        transition_status(ticket, 'in_progress')
        self.assertEqual(ticket.status, 'in_progress')
        transition_status(ticket, 'resolved')
        self.assertEqual(ticket.status, 'resolved')

    def test_resolved_ticket_must_be_reopened_before_change(self):
        ticket = Ticket('T012', 'Login issue', TicketCategory.Software, TicketUrgency.High, 5, '', 'resolved', 'Alex')
        with self.assertRaises(ValueError):
            transition_status(ticket, 'in_progress')
        transition_status(ticket, 'open')
        self.assertEqual(ticket.status, 'open')

    def test_queue_sorts_by_priority_then_numeric_ticket_id(self):
        tickets = [
            Ticket('T020', 'Low', TicketCategory.Other, TicketUrgency.Low, 1, 'low', 'open'),
            Ticket('T010', 'High', TicketCategory.Network, TicketUrgency.High, 5, 'high', 'open'),
            Ticket('T015', 'Medium', TicketCategory.Hardware, TicketUrgency.Low, 5, 'medium', 'open'),
            Ticket('T005', 'Critical', TicketCategory.Network, TicketUrgency.High, 12, 'critical', 'open'),
        ]
        ordered = [ticket.id for ticket in build_queue(tickets)]
        self.assertEqual(ordered, ['T005', 'T010', 'T015', 'T020'])


if __name__ == '__main__':
    unittest.main()
