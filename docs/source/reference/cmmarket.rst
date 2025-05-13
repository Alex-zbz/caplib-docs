Commodity Market
===============

The cmmarket module provides templates and market data structures for commodity market instruments and pricing.

.. contents:: Table of Contents
   :local:
   :depth: 2

Template Functions
----------------

These functions create instrument templates for commodity market products.

Create PM Cash Template
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_pm_cash_template(inst_name, start_delay, delivery_day_convention, calendars, day_count)

Create a Physical Metals (PM) cash template.

Parameters:
  - ``inst_name`` (str): The name of the instrument.
  - ``start_delay`` (int): The start delay in days.
  - ``delivery_day_convention`` (str): The delivery day convention.
  - ``calendars`` (list): List of calendars.
  - ``day_count`` (str): The day count convention.

Returns:
  - ``PmCashTemplate``

Example:

.. code-block:: python

    import caplib.cmmarket as cmmarket
    
    pm_cash_template = cmmarket.create_pm_cash_template(
        inst_name="PM_GOLD_CASH",
        start_delay=2,
        delivery_day_convention="FOLLOWING",
        calendars=["USA", "UK"],
        day_count="ACT_360"
    )

Create CM Futures Template
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cm_futures_template(inst_name, start_delay, delivery_day_convention, calendars, day_count)

Create a Commodity (CM) futures template.

Parameters:
  - ``inst_name`` (str): The name of the instrument.
  - ``start_delay`` (int): The start delay in days.
  - ``delivery_day_convention`` (str): The delivery day convention.
  - ``calendars`` (list): List of calendars.
  - ``day_count`` (str): The day count convention.

Returns:
  - ``CmFuturesTemplate``

Example:

.. code-block:: python

    import caplib.cmmarket as cmmarket
    
    cm_futures_template = cmmarket.create_cm_futures_template(
        inst_name="WTI_CRUDE_FUTURES",
        start_delay=2,
        delivery_day_convention="FOLLOWING",
        calendars=["USA"],
        day_count="ACT_360"
    )

Create CM Option Template
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cm_option_template(inst_name, start_delay, delivery_day_convention, calendars, day_count)

Create a Commodity (CM) option template.

Parameters:
  - ``inst_name`` (str): The name of the instrument.
  - ``start_delay`` (int): The start delay in days.
  - ``delivery_day_convention`` (str): The delivery day convention.
  - ``calendars`` (list): List of calendars.
  - ``day_count`` (str): The day count convention.

Returns:
  - ``CmOptionTemplate``

Example:

.. code-block:: python

    import caplib.cmmarket as cmmarket
    
    cm_option_template = cmmarket.create_cm_option_template(
        inst_name="WTI_CRUDE_OPTION",
        start_delay=2,
        delivery_day_convention="FOLLOWING",
        calendars=["USA"],
        day_count="ACT_360"
    )

Integration with Other Modules
---------------------------

The cmmarket module integrates with other caplib modules:

* **cmanalytics**: For pricing commodity derivatives using the templates created with cmmarket
* **market**: For general market data structures and curve operations
* **datetime**: For date calculations and calendar adjustments for settlement and delivery dates
* **staticdata**: For storing and retrieving the templates as static data
