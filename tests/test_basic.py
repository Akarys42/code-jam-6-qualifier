from tests.test_unit import TestRequirements
from datetime import datetime as dt


class TestBasicRequirements(TestRequirements):
    cases = (
        ('2017-05-06', dt(2017, 5, 6)),
        ('2017-05-06T12:25:30', dt(2017, 5, 6, 12, 25, 30)),
        ('2017-05-06T12:25', dt(2017, 5, 6, 12, 25)),
        ('2017-05-06T12', dt(2017, 5, 6, 12)),
    )
