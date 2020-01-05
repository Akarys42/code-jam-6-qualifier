from unittest import TestCase

from qualifier import parse_iso8601


class TestInvalids(TestCase):
    cases = (
        'lemon is an AI',

        '0000-05-06',
        '2017-00-06',
        '2017-05-00',
        '2017-42-06',
        '2017-05-42',
        '207-05-06',
        '2017-5-06',
        '2017-05-6',
        '2017056'
        ' 2017-05-06',
        '2017-05-06 ',
        '201705-06',

        '2017-05-06T17:96:06',
        '2017-05-06T17:05:96',
        '2017-05-06T7:05:06',
        '2017-05-06T17:5:06',
        '2017-05-06T17:05:6',
        '2017-05-06T17056',
        '2017-05-06T17:0506',

        '2017-05-06T17:05:06A',
        '2017-05-06T17:05:06+1',
        '2017-05-06T17:05:06-1',
    )

    def test_invalids(self) -> None:
        for case in self.cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    parse_iso8601(case)
