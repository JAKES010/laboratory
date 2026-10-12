import unittest

from campusflow.tickets import Ticket, TicketCategory, TicketUrgency, calculate_priority


class TicketTests(unittest.TestCase):
    def test_priority_high_urgency_ten_users_is_critical(self):
        ticket = Ticket('T001', 'Wi-Fi outage', TicketCategory.Network, TicketUrgency.High, 10, '', 'open')
        self.assertEqual(ticket.priority, 'critical')

    def test_priority_high_urgency_two_users_is_high(self):
        self.assertEqual(calculate_priority(TicketUrgency.High, 2), 'high')

    def test_priority_low_urgency_four_users_is_medium(self):
        self.assertEqual(calculate_priority(TicketUrgency.Low, 4), 'medium')

    def test_priority_low_urgency_one_user_is_low(self):
        self.assertEqual(calculate_priority(TicketUrgency.Low, 1), 'low')

    def test_zero_affected_users_rejected(self):
        with self.assertRaises(ValueError):
            Ticket('T002', 'Broken laptop', TicketCategory.Hardware, TicketUrgency.Medium, 0, '', 'open')

    def test_blank_title_rejected(self):
        with self.assertRaises(ValueError):
            Ticket('T003', '   ', TicketCategory.Other, TicketUrgency.Low, 1, '', 'open')

    def test_case_variations_are_normalized(self):
        ticket = Ticket('T004', 'Printer issue', 'network', 'HIGH', 12, '', 'open')
        self.assertEqual(ticket.category, 'Network')
        self.assertEqual(ticket.urgency, 'high')
        self.assertEqual(ticket.priority, 'critical')


if __name__ == '__main__':
    unittest.main()
