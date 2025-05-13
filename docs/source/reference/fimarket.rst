Fixed Income Market
=================

This module provides functionality for creating and managing fixed income market instruments, including various types of bonds and other fixed income securities.

.. contents:: Table of Contents
   :local:
   :depth: 2

Enumeration Conversions
--------------------

Functions for converting string representations to enumeration values.

.. code-block:: python

    to_vanilla_bond_type(vanilla_bond_type_str)

Convert a string to a VanillaBondType enumeration value.

Parameters:
  - ``vanilla_bond_type_str`` (str): String representation of a bond type.

Returns:
  - VanillaBondType: Enumeration value representing the bond type.

Example:

.. code-block:: python

    from caplib.fimarket import to_vanilla_bond_type
    
    # Convert string to VanillaBondType enum
    bond_type = to_vanilla_bond_type("FIXED_COUPON_BOND")
    # Other possible values: "FLOATING_COUPON_BOND", "ZERO_COUPON_BOND"

Bond Templates
----------

Functions for creating templates for bond instruments.

.. code-block:: python

    create_bond_template(inst_name, currency, calendar, payment_freq, day_count, broken_period_day_count, payment_delay, coupon_day_convention, ex_div_days, ex_div_convention, accrual_method)

Create a template for bond instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the template.
  - ``currency`` (str): Currency of the bond.
  - ``calendar`` (str): Calendar for business day adjustments.
  - ``payment_freq`` (str): Frequency of coupon payments (e.g., "ANNUAL", "SEMI_ANNUAL").
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``broken_period_day_count`` (str): Day count convention for broken periods.
  - ``payment_delay`` (int): Delay in business days for payments.
  - ``coupon_day_convention`` (str): Business day convention for coupon dates.
  - ``ex_div_days`` (int): Number of ex-dividend days.
  - ``ex_div_convention`` (str): Business day convention for ex-dividend dates.
  - ``accrual_method`` (str): Method for accrual calculation.

Returns:
  - Bond template object.

Example:

.. code-block:: python

    from caplib.fimarket import create_bond_template
    
    # Create a USD bond template
    usd_bond_template = create_bond_template(
        inst_name="USD_BOND",
        currency="USD",
        calendar="US",
        payment_freq="SEMI_ANNUAL",
        day_count="30_360",
        broken_period_day_count="30_360",
        payment_delay=0,
        coupon_day_convention="MODIFIED_FOLLOWING",
        ex_div_days=1,
        ex_div_convention="PRECEDING",
        accrual_method="STREET"
    )
    
    # Create a EUR bond template
    eur_bond_template = create_bond_template(
        inst_name="EUR_BOND",
        currency="EUR",
        calendar="TARGET",
        payment_freq="ANNUAL",
        day_count="ACT_ACT_ICMA",
        broken_period_day_count="ACT_ACT_ICMA",
        payment_delay=0,
        coupon_day_convention="MODIFIED_FOLLOWING",
        ex_div_days=1,
        ex_div_convention="PRECEDING",
        accrual_method="STREET"
    )

Vanilla Bond Template
~~~~~~~~~~~~~~~

.. code-block:: python

    create_vanilla_bond_template(inst_name, bond_template, bond_type, bond_subtype)

Create a template for vanilla bond instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the template.
  - ``bond_template`` (object): Base bond template created by ``create_bond_template``.
  - ``bond_type`` (str): Type of bond (e.g., "FIXED_COUPON_BOND", "FLOATING_COUPON_BOND", "ZERO_COUPON_BOND").
  - ``bond_subtype`` (str): Subtype of bond (e.g., "BULLET", "CALLABLE").

Returns:
  - Vanilla bond template object.

Example:

.. code-block:: python

    from caplib.fimarket import create_vanilla_bond_template
    
    # Create a fixed coupon bond template
    fixed_bond_template = create_vanilla_bond_template(
        inst_name="USD_FIXED_COUPON_BOND",
        bond_template=usd_bond_template,  # From previous example
        bond_type="FIXED_COUPON_BOND",
        bond_subtype="BULLET"
    )
    
    # Create a floating coupon bond template
    floating_bond_template = create_vanilla_bond_template(
        inst_name="USD_FLOATING_COUPON_BOND",
        bond_template=usd_bond_template,
        bond_type="FLOATING_COUPON_BOND",
        bond_subtype="BULLET"
    )
    
    # Create a zero coupon bond template
    zero_bond_template = create_vanilla_bond_template(
        inst_name="USD_ZERO_COUPON_BOND",
        bond_template=usd_bond_template,
        bond_type="ZERO_COUPON_BOND",
        bond_subtype="BULLET"
    )

Zero Coupon Bond
~~~~~~~~~~~~

.. code-block:: python

    create_zero_coupon_bond(maturity_date, issue_date, face_value, redemption_value, vanilla_bond_template)

Create a zero coupon bond instrument.

Parameters:
  - ``maturity_date`` (datetime): Maturity date of the bond.
  - ``issue_date`` (datetime): Issue date of the bond.
  - ``face_value`` (float): Face value of the bond.
  - ``redemption_value`` (float): Redemption value of the bond.
  - ``vanilla_bond_template`` (object): Vanilla bond template created by ``create_vanilla_bond_template``.

Returns:
  - Zero coupon bond instrument object.

Example:

.. code-block:: python

    from caplib.fimarket import create_zero_coupon_bond
    from datetime import datetime
    
    # Create a zero coupon bond
    maturity_date = datetime(2030, 6, 15)
    issue_date = datetime(2020, 6, 15)
    
    zero_bond = create_zero_coupon_bond(
        maturity_date=maturity_date,
        issue_date=issue_date,
        face_value=100.0,
        redemption_value=100.0,
        vanilla_bond_template=zero_bond_template  # From previous example
    )

Floating Coupon Bond
~~~~~~~~~~~~~~~

.. code-block:: python

    create_floating_coupon_bond(maturity_date, issue_date, face_value, ref_index, spread, cap, floor, redemption_value, vanilla_bond_template)

Create a floating coupon bond instrument.

Parameters:
  - ``maturity_date`` (datetime): Maturity date of the bond.
  - ``issue_date`` (datetime): Issue date of the bond.
  - ``face_value`` (float): Face value of the bond.
  - ``ref_index`` (str): Reference index for the floating rate (e.g., "USD_LIBOR_3M").
  - ``spread`` (float): Spread above the reference index (as a decimal, e.g., 0.0025 for 25 bps).
  - ``cap`` (float, optional): Upper limit for the floating rate.
  - ``floor`` (float, optional): Lower limit for the floating rate.
  - ``redemption_value`` (float): Redemption value of the bond.
  - ``vanilla_bond_template`` (object): Vanilla bond template created by ``create_vanilla_bond_template``.

Returns:
  - Floating coupon bond instrument object.

Example:

.. code-block:: python

    from caplib.fimarket import create_floating_coupon_bond
    from datetime import datetime
    
    # Create a floating coupon bond
    maturity_date = datetime(2030, 6, 15)
    issue_date = datetime(2020, 6, 15)
    
    floating_bond = create_floating_coupon_bond(
        maturity_date=maturity_date,
        issue_date=issue_date,
        face_value=100.0,
        ref_index="USD_LIBOR_3M",
        spread=0.0025,  # 25 bps over the reference index
        cap=0.08,       # Maximum rate of 8%
        floor=0.0,      # Minimum rate of 0%
        redemption_value=100.0,
        vanilla_bond_template=floating_bond_template  # From previous example
    )

Fixed Coupon Bond
~~~~~~~~~~~~

.. code-block:: python

    create_fixed_coupon_bond(maturity_date, issue_date, face_value, coupon_rate, redemption_value, vanilla_bond_template)

Create a fixed coupon bond instrument.

Parameters:
  - ``maturity_date`` (datetime): Maturity date of the bond.
  - ``issue_date`` (datetime): Issue date of the bond.
  - ``face_value`` (float): Face value of the bond.
  - ``coupon_rate`` (float): Annual coupon rate (as a decimal, e.g., 0.05 for 5%).
  - ``redemption_value`` (float): Redemption value of the bond.
  - ``vanilla_bond_template`` (object): Vanilla bond template created by ``create_vanilla_bond_template``.

Returns:
  - Fixed coupon bond instrument object.

Example:

.. code-block:: python

    from caplib.fimarket import create_fixed_coupon_bond
    from datetime import datetime
    
    # Create a fixed coupon bond
    maturity_date = datetime(2030, 6, 15)
    issue_date = datetime(2020, 6, 15)
    
    fixed_bond = create_fixed_coupon_bond(
        maturity_date=maturity_date,
        issue_date=issue_date,
        face_value=100.0,
        coupon_rate=0.05,  # 5% annual coupon
        redemption_value=100.0,
        vanilla_bond_template=fixed_bond_template  # From previous example
    )

Standard Bond Templates
------------------

Standard Bond Template
~~~~~~~~~~~~~~~

The ``create_std_bond_template`` function creates a standard bond template with default values for many parameters.

.. code-block:: python

    from caplib.fimarket import create_std_bond_template
    
    # Create a standard bond template
    std_bond = create_std_bond_template(
        inst_name="US_TREASURY_STD",
        bond_type="FIXED_COUPON_BOND",
        issue_date=datetime(2025, 1, 15),
        settlement_days=2,
        maturity="7Y",
        currency="USD",
        day_count="ACT_365_FIXED",
        calendar="US",
        frequency="SEMI_ANNUAL",
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        rate=0.033,  # 3.3% coupon rate
        issue_price=100.0
    )

Standard Zero Coupon Bond Template
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``create_std_zero_cpn_bond_template`` function creates a standard zero coupon bond template with simplified parameters.

.. code-block:: python

    from caplib.fimarket import create_std_zero_cpn_bond_template
    
    # Create a standard zero coupon bond template
    std_zero_bond = create_std_zero_cpn_bond_template(
        inst_name="US_TBILL_STD",
        issue_date=datetime(2025, 1, 15),
        maturity="6M",
        currency="USD",
        calendar="US",
        issue_price=98.0,
        settlement_days=1,
        day_count="ACT_365_FIXED",
        pay_day_convention="MODIFIED_FOLLOWING"
    )

Standard Fixed Coupon Bond Template
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``create_std_fixed_cpn_bond_template`` function creates a standard fixed coupon bond template with simplified parameters.

.. code-block:: python

    from caplib.fimarket import create_std_fixed_cpn_bond_template
    
    # Create a standard fixed coupon bond template
    std_fixed_bond = create_std_fixed_cpn_bond_template(
        inst_name="US_TREASURY_STD_FIXED",
        issue_date=datetime(2025, 1, 15),
        maturity="5Y",
        currency="USD",
        calendar="US",
        rate=0.032,  # 3.2% coupon rate
        issue_price=100.0,
        settlement_days=2,
        day_count="ACT_365_FIXED",
        frequency="SEMI_ANNUAL",
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING"
    )

Building Bond Instruments
--------------------

Building a Vanilla Bond
~~~~~~~~~~~~~~~~

The ``build_vanilla_bond`` function creates a vanilla bond instrument from a template.

.. code-block:: python

    from caplib.fimarket import build_vanilla_bond
    
    # Build a vanilla bond instrument
    # Assuming we have a vanilla_bond_template from earlier example
    
    # For floating bonds, fixings would be a dictionary of date-rate pairs
    fixings = {}  # Empty for fixed rate bonds
    
    # Build the bond with 1 million notional
    bond = build_vanilla_bond(
        nominal=1000000.0,  # 1 million nominal
        vanilla_bond_template=vanilla_bond,  # Template from earlier example
        fixings=fixings
    )

Building a Zero Coupon Bond
~~~~~~~~~~~~~~~~~~~~

The ``build_zero_cpn_bond`` function creates a zero coupon bond instrument from a template.

.. code-block:: python

    from caplib.fimarket import build_zero_cpn_bond
    
    # Build a zero coupon bond instrument
    # Assuming we have a zero_bond template from earlier example
    
    # Build the zero coupon bond with 1 million notional
    zero_coupon_bond = build_zero_cpn_bond(
        nominal=1000000.0,  # 1 million nominal
        zero_cpn_bond_template=zero_bond  # Template from earlier example
    )

Building a Fixed Coupon Bond
~~~~~~~~~~~~~~~~~~~~~~

The ``build_fixed_cpn_bond`` function creates a fixed coupon bond instrument from a template.

.. code-block:: python

    from caplib.fimarket import build_fixed_cpn_bond
    
    # Build a fixed coupon bond instrument
    # Assuming we have a fixed_bond template from earlier example
    
    # Build the fixed coupon bond with 1 million notional
    fixed_coupon_bond = build_fixed_cpn_bond(
        nominal=1000000.0,  # 1 million nominal
        fixed_cpn_bond_template=fixed_bond  # Template from earlier example
    )

Complete Workflow Example
--------------------

Here's a complete workflow that demonstrates creating bond templates and building bond instruments:

.. code-block:: python

    from datetime import datetime
    from caplib.fimarket import (
        create_fixed_cpn_bond_template,
        create_zero_cpn_bond_template,
        build_fixed_cpn_bond,
        build_zero_cpn_bond
    )
    
    # Step 1: Set up dates
    issue_date = datetime(2025, 1, 15)
    start_date = issue_date
    
    # Step 2: Create a fixed coupon bond template
    treasury_template = create_fixed_cpn_bond_template(
        inst_name="US_TREASURY_10Y",
        issue_date=issue_date,
        settlement_days=2,
        start_date=start_date,
        maturity="10Y",
        rate=0.035,  # 3.5% coupon rate
        currency="USD",
        calendar="US",
        frequency="SEMI_ANNUAL",
        day_count="30/360",
        issue_price=100.0
    )
    
    # Step 3: Create a zero coupon bond template
    tbill_template = create_zero_cpn_bond_template(
        inst_name="US_TBILL_1Y",
        issue_date=issue_date,
        settlement_days=1,
        start_date=start_date,
        maturity="1Y",
        currency="USD",
        issue_price=97.0,  # Discount from par
        calendar="US"
    )
    
    # Step 4: Build the fixed coupon bond instrument
    treasury_bond = build_fixed_cpn_bond(
        nominal=1000000.0,  # 1 million nominal
        fixed_cpn_bond_template=treasury_template
    )
    
    # Step 5: Build the zero coupon bond instrument
    tbill = build_zero_cpn_bond(
        nominal=1000000.0,  # 1 million nominal
        zero_cpn_bond_template=tbill_template
    )
    
    # The instruments are now ready for pricing and analysis
    print(f"Created Treasury Bond: {treasury_bond}")
    print(f"Created T-Bill: {tbill}")
