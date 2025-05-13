Date and Time
============

This section covers date and time functionality available in the caplib.datetime module.

.. contents:: Table of Contents
   :local:
   :depth: 2

Conversion Functions
------------------

The module provides several functions to convert string representations to date-related enumerations used throughout the library.

Frequency Conversion
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import to_frequency
    
    # Convert string to Frequency enum
    annual_freq = to_frequency("ANNUAL")
    semi_annual_freq = to_frequency("SEMI_ANNUAL")
    quarterly_freq = to_frequency("QUARTERLY")
    monthly_freq = to_frequency("MONTHLY")
    
    # Default value if None is provided
    default_freq = to_frequency(None)  # Returns INVALID_FREQUENCY

Day Count Convention
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import to_day_count_convention
    
    # Convert string to DayCountConvention enum
    act_365 = to_day_count_convention("ACT_365_FIXED")
    act_360 = to_day_count_convention("ACT_360")
    thirty_360 = to_day_count_convention("THIRTY_360")
    
    # Default value if None is provided
    default_dc = to_day_count_convention(None)  # Returns INVALID_DAY_COUNT_CONVENTION

Business Day Convention
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import to_business_day_convention
    
    # Convert string to BusinessDayConvention enum
    following = to_business_day_convention("FOLLOWING")
    mod_following = to_business_day_convention("MODIFIED_FOLLOWING")
    preceding = to_business_day_convention("PRECEDING")
    
    # Default value if None is provided
    default_bdc = to_business_day_convention(None)  # Returns INVALID_BUSINESS_DAY_CONVENTION

Other Conversion Functions
~~~~~~~~~~~~~~~~~~~~~~

The module also provides conversion functions for other date-related enumerations:

.. code-block:: python

    from caplib.datetime import (
        to_stub_policy,
        to_broken_period_type,
        to_sched_gen_method,
        to_date_roll_convention,
        to_rel_sched_gen_mode,
        to_date_gen_mode,
        to_time_unit,
        to_special_period
    )
    
    # Examples
    stub_policy = to_stub_policy("INITIAL")
    broken_period = to_broken_period_type("LONG")
    schedule_gen = to_sched_gen_method("ABSOLUTE_NORMAL")
    date_roll = to_date_roll_convention("EOM")  # End of Month
    rel_sched = to_rel_sched_gen_mode("BACKWARD_WITHOUT_BROKEN")
    date_gen = to_date_gen_mode("IN_ADVANCE")
    time_unit = to_time_unit("DAYS")
    special_period = to_special_period("OVERNIGHT")

Period Handling
------------

The module provides functions for working with financial periods.

Converting Period Strings
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import to_period
    
    # Convert string representation to Period object
    period_3m = to_period("3M")  # 3 months
    period_1y = to_period("1Y")  # 1 year
    period_2w = to_period("2W")  # 2 weeks
    period_30d = to_period("30D")  # 30 days
    overnight = to_period("ON")  # Overnight
    spot_next = to_period("SN")  # Spot next

Creating Periods
~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import create_period
    
    # Create a period using length and unit
    three_months = create_period(3, "MONTHS")
    one_year = create_period(1, "YEARS")
    two_weeks = create_period(2, "WEEKS")
    thirty_days = create_period(30, "DAYS")
    
    # Create a special period
    overnight_period = create_period(0, "", "OVERNIGHT")
    spot_next_period = create_period(0, "", "SPOT_NEXT")

Date Creation and Manipulation
---------------------------

Creating Date Objects
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import create_date
    from datetime import datetime
    
    # Create a Date object from a Python datetime
    today = datetime.now()
    date_obj = create_date(today)
    
    # Create a Date object from a specific date
    specific_date = datetime(2025, 3, 20)
    specific_date_obj = create_date(specific_date)

Calendar Operations
~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import create_calendar
    from datetime import datetime
    
    # Create a calendar with custom holidays
    holidays = [
        datetime(2025, 1, 1),   # New Year's Day
        datetime(2025, 12, 25)  # Christmas
    ]
    
    # Create a calendar with holidays and special business days
    special_days = [
        datetime(2025, 2, 1)  # A special business day (weekend that is a working day)
    ]
    
    us_calendar = create_calendar(
        cal_name="US",
        holidays=holidays,
        special_business_days=special_days
    )

Year Fraction Calculations
-----------------------

The module provides functions for calculating year fractions between dates, which is essential for interest accrual calculations.

Simple Year Fraction
~~~~~~~~~~~~~~~~

.. code-block:: python

    from caplib.datetime import simple_year_frac_calculator
    from datetime import datetime
    
    # Calculate year fraction between two dates
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2026, 1, 1)
    
    # Using different day count conventions
    act_365_yf = simple_year_frac_calculator(start_date, end_date, "ACT_365_FIXED")
    act_360_yf = simple_year_frac_calculator(start_date, end_date, "ACT_360")
    thirty_360_yf = simple_year_frac_calculator(start_date, end_date, "THIRTY_360")
    
    print(f"ACT/365 year fraction: {act_365_yf}")  # Should be close to 1.0
    print(f"ACT/360 year fraction: {act_360_yf}")  # Should be slightly larger than 1.0
    print(f"30/360 year fraction: {thirty_360_yf}")  # Should be exactly 1.0

Complex Year Fraction
~~~~~~~~~~~~~~~~~

For more complex scenarios, including accrued interest calculations that need reference to period start and end dates:

.. code-block:: python

    from caplib.datetime import year_frac_calculator
    from datetime import datetime
    
    # Calculate year fraction with reference dates for complex instruments
    start_date = datetime(2025, 2, 15)  # Mid-period start date
    end_date = datetime(2025, 5, 15)    # Mid-period end date
    
    # Reference dates for the full period
    ref_start_date = datetime(2025, 2, 1)
    ref_end_date = datetime(2025, 8, 1)
    ref_period_end = datetime(2025, 8, 1)
    
    # Calculate with semi-annual frequency
    yf = year_frac_calculator(
        start_date=start_date,
        end_date=end_date,
        day_count="ACT_365_FIXED",
        ref_start_date=ref_start_date,
        ref_end_date=ref_end_date,
        ref_period_end=ref_period_end,
        frequency="SEMI_ANNUAL",
        is_end_of_month=False
    )
    
    print(f"Complex year fraction: {yf}")

Schedule Generation
----------------

Generate Date
~~~~~~~~~~

Generate a single date based on a reference date and a period:

.. code-block:: python

    from caplib.datetime import date_generator
    from datetime import datetime
    
    # Reference date
    reference_date = datetime(2025, 3, 20)
    
    # Generate a date 3 months forward, adjusted for business days
    future_date = date_generator(
        reference_date=reference_date,
        period="3M",
        calendar="US",
        business_day_convention="FOLLOWING",
        end_of_month=False,
        date_roll_convention="EOM"
    )
    
    print(f"Generated date: {future_date}")

Schedule Generation
~~~~~~~~~~~~~~~

Generate a schedule of dates for financial instruments:

.. code-block:: python

    from caplib.datetime import schedule_generator
    from datetime import datetime
    
    # Generate a quarterly schedule for a 1-year period
    start_date = datetime(2025, 3, 20)
    end_date = datetime(2026, 3, 20)
    
    schedule = schedule_generator(
        start_date=start_date,
        end_date=end_date,
        frequency="QUARTERLY",
        calendars=["US"],
        business_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        date_roll_convention="EOM",
        broken_period_type="SHORT"
    )
    
    # The schedule will contain dates adjusted for business days:
    # - 2025-03-20 (Start date)
    # - 2025-06-22 (First quarterly date, adjusted for weekends)
    # - 2025-09-22 (Second quarterly date, adjusted for weekends)
    # - 2025-12-22 (Third quarterly date, adjusted for weekends)
    # - 2026-03-20 (End date)

Creating Schedule from Dates
~~~~~~~~~~~~~~~~~~~~~~~

Create a schedule object from a list of dates:

.. code-block:: python

    from caplib.datetime import create_schedule
    from datetime import datetime
    
    # List of dates for the schedule
    dates = [
        datetime(2025, 3, 20),
        datetime(2025, 6, 20),
        datetime(2025, 9, 20),
        datetime(2025, 12, 20),
        datetime(2026, 3, 20)
    ]
    
    # Create a schedule from the dates
    schedule = create_schedule(dates)

Integration with Other Modules
---------------------------

The datetime module is used extensively throughout the caplib library for working with dates, periods, and schedules. Here's an example of how it integrates with other modules:

.. code-block:: python

    from caplib.datetime import create_date, to_period, to_business_day_convention
    from caplib.cmanalytics import create_pm_par_rate_curve
    
    # Creating a par rate curve with date handling
    as_of_date = create_date(datetime(2025, 3, 20))
    
    pillars = [
        ["3M", 0.0275],
        ["6M", 0.0280],
        ["1Y", 0.0290],
        ["2Y", 0.0310],
        ["3Y", 0.0325],
        ["5Y", 0.0345],
        ["7Y", 0.0355],
        ["10Y", 0.0365]
    ]
    
    # Using date functions in the context of creating a curve
    curve = create_pm_par_rate_curve(
        as_of_date=as_of_date,
        currency="USD",
        curve_name="PM_USD_CURVE",
        pillars=pillars
    )
