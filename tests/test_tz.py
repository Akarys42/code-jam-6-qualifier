from tests.test_unit import TestRequirements
from datetime import datetime as dt, timedelta as td, timezone as tz


class TestTimezoneRequirements(TestRequirements):
    cases = (
        ('2017-05-06', dt(2017, 5, 6)),
        ('2017-05-06Z', dt(2017, 5, 6, tzinfo=tz.utc)),
        ('2017-05-06+01:30', dt(2017, 5, 6, tzinfo=tz(td(hours=1, minutes=30)))),
        ('2017-05-06+0130', dt(2017, 5, 6, tzinfo=tz(td(hours=1, minutes=30)))),
        ('2017-05-06+01', dt(2017, 5, 6, tzinfo=tz(td(hours=1)))),
        ('2017-05-06-01:30', dt(2017, 5, 6, tzinfo=tz(-td(hours=1, minutes=30)))),
        ('2017-05-06-0130', dt(2017, 5, 6, tzinfo=tz(-td(hours=1, minutes=30)))),
        ('2017-05-06-01', dt(2017, 5, 6, tzinfo=tz(-td(hours=1))))
    )
