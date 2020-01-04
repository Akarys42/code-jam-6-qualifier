from unittest import TestCase

from qualifier import parse_iso8601


class TestRequirements(TestCase):
    cases = ()

    def test_requirements(self):
        for case in self.cases:
            with self.subTest(case=case):
                self.assertEqual(parse_iso8601(case[0]), case[1])