import unittest
from agent import review_capacity


class CapacityTests(unittest.TestCase):
    def test_high_occupancy_is_flagged_as_simulated(self):
        result = review_capacity({"occupied_beds": 95, "total_beds": 100})
        self.assertIn("high-simulated-occupancy", result["flags"])
        self.assertEqual(result["data_status"], "fictional-demonstration")


if __name__ == "__main__":
    unittest.main()
