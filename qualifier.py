import datetime
import re
from decimal import Decimal, InvalidOperation


MAGIC_REGEX_STR = (
    r'^'                             # Beginning of the timestamp
    r'(?P<year>[0-9]{4})'            # Four digit year
    r'(?P<sepd>-?)'                  # Optional `-` separator, saved into the capture group `sepd` (either `-` or empty)
    r'(?P<month>[0-9]{2})'           # Two digit month
    r'(?P=sepd)'                     # Match `sepd`, so we enforce the same separator rule across the timestamp
    r'(?P<day>[0-9]{2})'             # Two digit day
    r'(T'                            # Beginning of the optional time part
        r'(?P<hour>[0-9]{2})'        # Two digit hour
        r'(?P<sept>:?)'              # Optional `:` separator, saved into the capture group `sept` (either `:` or empty)
        r'(?P<minute>[0-9]{2})?'     # Optional two digit minute
        r'((?P=sept)'                # Match `sept` if `minute` match too, so we enforce the same separator rule
        r'(?P<second>[0-9.]{2,}))?'  # Optional second composed of at least 2 numbers and dots (`.`)
        r')?'                        # End of the time part
    r'(?P<timezone>'                 # Beginning of the optional timezone part
            r'Z'                     # Option 1 : literal `Z`
        r'|'                         # OR option 2 :
            r'(\+|-)'                # Either literal `+` OR `-`
            r'[0-9]{2}'              # Two digit hour
            r'(:?'                   # Ignored optional separator
            r'[0-9]{2})?'            # Optional two digit minute
        r')?'                        # End of the timezone part
    r'$'                             # End of the timestamp
)
# 210 chars long :>

MAGIC_REGEX = re.compile(MAGIC_REGEX_STR)

KEYS = ('year', 'month', 'day', 'hour', 'minute')  # List of arguments accepted by the datetime constructor
# `second` and `tzinfo` are manually added, since they need additional steps


def parse_iso8601(timestamp: str) -> datetime.datetime:
    """Parse an ISO-8601 formatted time stamp."""
    match = re.match(MAGIC_REGEX, timestamp)

    if not match:  # The regex didn't match, we just raise an error
        raise ValueError(f"{timestamp} isn't a valid ISO8601 timestamp")

    args = {key: int(match.group(key)) if match.group(key) else 0 for key in KEYS}  # Dict keyword-arg -> value

    if match.group('second'):
        if not match.group('minute'):
            # if `minute` didn't matched, it means that there wasn't enough character in the time part
            raise ValueError('Time definition too short')

        try:
            second = Decimal(match.group('second'))
        except InvalidOperation:
            raise ValueError(f'{match.group("second")} isn\'t a valid number')
        # We need to reprocess it to extract the microseconds
        args['microsecond'] = int((second % 1) * 1_000_000)
        args['second'] = int(second)

    tz = match.group('timezone')
    if tz:
        if tz == 'Z':
            tz = datetime.timezone.utc
        else:
            tz = tz.replace(":", "").ljust(5, '0')
            # Get rid of the separator if there is one, and enforce the size of the string
            tz = datetime.timezone(datetime.timedelta(hours=int(tz[:3]), minutes=int(tz[0] + tz[3:5])))
            # Construct the timezone based on the sign (index 0) and the revelant part
    args['tzinfo'] = tz

    return datetime.datetime(**args)  # Construct the final datetime object

