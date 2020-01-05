from tests.unit import TestRequirements
from datetime import datetime as dt


class TestAdvancedRequirements(TestRequirements):
    cases = (
        ('20170506', dt(2017, 5, 6)),
        ('2017-05-06T12:25:30.4', dt(2017, 5, 6, 12, 25, 30, 400)),
        ('2017-05-06T122530.4', dt(2017, 5, 6, 12, 25, 30, 400)),
        ('2017-05-06T122530', dt(2017, 5, 6, 12, 25, 30)),
        ('2017-05-06T1225', dt(2017, 5, 6, 12, 25))
    )
