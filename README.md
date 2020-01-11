# Code Jam 6: Qualifier
My solution to the @python-discord Code Jam 6 qualifier. 

## Requirements
Here is the requirements to complete the qualifier. Advanced requirements were optionals, but I decided to try to complete them. 

### Basic Requirements
  - Must return an instance of `datetime.datetime` that is equivalent to the given ISO-8601 timestamp
  - Must be able to parse date strings in the format `YYYY-MM-DD`
  - Must also be able to parse combined datetime strings in the format `<date>T<time>`, where `<time>` can be one of:
     - `hh:mm:ss`  (e.g. `2017-05-05T12:00:00`)
     - `hh:mm`     (e.g. `2017-05-05T12:00`)
     - `hh`        (e.g. `2017-05-05T12`)
  - If given invalid input, raise a `ValueError` explaining what went wrong.

### Advanced Requirements (optional, for extra points)
  - Support the truncated date format `YYYYMMDD`
  - Support fractional seconds `hh:mm:ss.sss`
  - Support the truncated time formats `hhmmss.ssss`, `hhmmss`, `hhmm`
  - [Support time zones](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators)
    - Timestamps without a timezone are local time
    - Timestamps with a timezone are relative to the UTC
      - Supported formats are `Z`, `±hh:mm`, `±hhmm` and `±hh`

### Run the test suite
I included a testsuite to make sure my solution was working correctly. In order to run it, you need to have [pipenv](https://github.com/pypa/pipenv) installed an run
```
pipenv run test
```

### Development environment
In order to ensure a good code quality for my submission, I added a precommit, a little script that run before every commit and make sure my code follow the quality standards. If my code fail it, the commit is aborted. In order to setup it, you need to have [pipenv](https://github.com/pypa/pipenv) installed and run
```
pipenv sync --dev
pipenv run precommit
```
