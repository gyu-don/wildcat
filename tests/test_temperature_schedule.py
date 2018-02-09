import unittest

from wildcat.annealer.simulated.temperature_schedule import TemperatureSchedule


class TestCase(unittest.TestCase):
    def test_initialize_temperature_schedule(self):
        scheduler = TemperatureSchedule()
        assert not (scheduler is None)

    def test_initialize_temperature_scheduler_with_params(self):
        schedule = TemperatureSchedule(initial_temperature=10, last_temperature=0.1, scale=0.8)
        assert schedule.initial_temperature == 10
        assert schedule.last_temperature == 0.1
        assert schedule.scale == 0.8

    def test_temperature_schedule(self):
        schedule = TemperatureSchedule(initial_temperature=10, last_temperature=0.1, scale=0.8)
        i = 0
        for t in schedule:
            if i == 0:
                self.assertAlmostEqual(t, schedule.initial_temperature)
            elif i == 1:
                self.assertAlmostEqual(t, schedule.initial_temperature * schedule.scale)
            i+=1

        self.assertLess(schedule.current_temperature, schedule.last_temperature)

