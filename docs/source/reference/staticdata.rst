Static Data
===========

The staticdata module provides functions for creating and managing static data objects that are stored in the object cache of the backend service. Static data objects represent various financial instruments, indices, and other reference data used in financial calculations.

Type Conversion Functions
------------------------

These functions convert string representations to their corresponding enumeration types in the protocol buffer definitions.

Static Data Type
~~~~~~~~~~~~~~~

.. code-block:: python

    to_static_data_type(src)

Convert a string to ``StaticDataType``.

Parameters:
  - ``src`` (str): String representing the static data type, e.g., 'SDT_IBOR_INDEX'.

Returns:
  - ``StaticDataType``

Example:

.. code-block:: python

    from caplib.staticdata import to_static_data_type
    
    data_type = to_static_data_type('SDT_IBOR_INDEX')

Static Data Creation and Management
----------------------------------

These functions allow you to create, retrieve, and manage static data objects in the backend service's object cache.

Create Static Data
~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_static_data(data_type, pb_data)

Create a static data object and store it in the backend service's object cache.

Parameters:
  - ``data_type`` (str or StaticDataType): Type of static data to create, e.g., 'SDT_IBOR_INDEX'.
  - ``pb_data`` (bytes): Serialized protocol buffer message containing the static data.

Returns:
  - ``bool``: True if the static data was successfully created and stored, False otherwise.

Raises:
  - ``Exception``: If the creation operation fails.

Example:

.. code-block:: python

    from caplib.staticdata import create_static_data
    
    # Create static data object
    # pb_data should be a serialized protocol buffer message
    success = create_static_data(
        data_type="SDT_IBOR_INDEX",
        pb_data=serialized_data
    )
    
    if success:
        print("Static data created successfully")
    else:
        print("Failed to create static data")

Get Static Data
~~~~~~~~~~~~~~

.. code-block:: python

    get_static_data(data_type, key, as_of_date=None)

Retrieve a static data object from the backend service's object cache.

Parameters:
  - ``data_type`` (str or StaticDataType): Type of static data to retrieve, e.g., 'SDT_IBOR_INDEX'.
  - ``key`` (str): Unique identifier for the static data object.
  - ``as_of_date`` (datetime, optional): Date for which to retrieve the static data.

Returns:
  - ``bytes``: Serialized protocol buffer message containing the static data.

Raises:
  - ``ValueError``: If the static data object doesn't exist or cannot be retrieved.

Example:

.. code-block:: python

    from caplib.staticdata import get_static_data
    from datetime import datetime
    
    # Retrieve static data for a specific index as of a specific date
    pb_data = get_static_data(
        data_type="SDT_IBOR_INDEX",
        key="USD_LIBOR_3M",
        as_of_date=datetime(2025, 3, 20)
    )
    
    # Parse the protocol buffer message to use the data
    # The parsing logic depends on the specific static data type

Delete Static Data
~~~~~~~~~~~~~~~~

.. code-block:: python

    delete_static_data(data_type, key)

Delete a static data object from the backend service's object cache.

Parameters:
  - ``data_type`` (str or StaticDataType): Type of static data to delete, e.g., 'SDT_IBOR_INDEX'.
  - ``key`` (str): Unique identifier for the static data object.

Returns:
  - ``bool``: True if the static data was successfully deleted, False otherwise.

Example:

.. code-block:: python

    from caplib.staticdata import delete_static_data
    
    # Delete a static data object
    success = delete_static_data(
        data_type="SDT_IBOR_INDEX",
        key="USD_LIBOR_3M"
    )
    
    if success:
        print("Static data deleted successfully")
    else:
        print("Failed to delete static data")

List Static Data
~~~~~~~~~~~~~~

.. code-block:: python

    list_static_data(data_type=None)

List all static data objects of a specific type or all types.

Parameters:
  - ``data_type`` (str or StaticDataType, optional): Type of static data to list, or None to list all types.

Returns:
  - ``dict``: Dictionary mapping static data types to lists of keys.

Example:

.. code-block:: python

    from caplib.staticdata import list_static_data
    
    # List all IBOR indices
    indices = list_static_data("SDT_IBOR_INDEX")
    print(indices)  # Output: {"SDT_IBOR_INDEX": ["USD_LIBOR_3M", "EUR_EURIBOR_6M", ...]}
    
    # List all static data
    all_data = list_static_data()
    for data_type, keys in all_data.items():
        print(f"{data_type}: {keys}")

Static Data Types
----------------

The module supports various types of static data, represented by the StaticDataType enumeration:

* ``SDT_IBOR_INDEX`` - IBOR (Interbank Offered Rate) index data
* ``SDT_CALENDAR`` - Calendar data for holiday schedules
* ``SDT_DAY_COUNT`` - Day count convention data
* ``SDT_INSTRUMENT_TEMPLATE`` - Template for financial instruments
* ``SDT_YIELD_CURVE`` - Yield curve data
* ``SDT_VOLATILITY_SURFACE`` - Volatility surface data

Common Use Cases
--------------

Creating and Using an IBOR Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to create an IBOR index which internally uses the static data functionality:

.. code-block:: python

    from caplib.irmarket import create_ibor_index
    
    # Create an IBOR index, which internally uses static data
    index = create_ibor_index(
        index_name="USD_LIBOR",
        index_tenor="3M",
        index_ccy="USD",
        calendar_list=["US"],
        start_delay="2D",
        day_count="ACT_360",
        interest_day_convention="MODIFIED_FOLLOWING"
    )
    
    # Behind the scenes, the create_ibor_index function:
    # 1. Creates an IBOR index protocol buffer
    # 2. Serializes it to binary data
    # 3. Calls create_static_data with data_type="SDT_IBOR_INDEX" and the serialized data
    # 4. The backend service stores the IBOR index in its object cache for later use

Creating and Using a Bond Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a bond template which internally uses the static data functionality:

.. code-block:: python

    from datetime import datetime
    from caplib.fimarket import create_vanilla_bond_template
    
    # Create a vanilla bond template, which internally uses static data
    bond_template = create_vanilla_bond_template(
        inst_name="US_TREASURY_5Y",
        bond_type="FIXED_COUPON_BOND",
        issue_date=datetime(2025, 1, 15),
        settlement_days=1,
        start_date=datetime(2025, 1, 15),
        maturity=datetime(2030, 1, 15),
        rate=0.025,  # 2.5%
        currency="USD",
        issue_price=1.0,
        day_count="ACT_360",
        calendar="US",
        frequency="SEMI_ANNUAL",
        interest_day_convention="MODIFIED_FOLLOWING"
    )

Building a Yield Curve
~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to create multiple static data objects and use them together to build a yield curve:

.. code-block:: python

    from datetime import datetime
    from caplib.irmarket import create_ibor_index
    from caplib.iranalytics import create_ir_market_data_set, create_ir_curve_build_settings, build_yield_curve
    
    # Set up the as-of date
    as_of_date = datetime(2025, 3, 20)
    
    # Create an IBOR index (uses static data)
    create_ibor_index(
        index_name="USD_LIBOR",
        index_tenor="3M",
        index_ccy="USD",
        calendar_list=["US"],
        start_delay="2D",
        day_count="ACT_360",
        interest_day_convention="MODIFIED_FOLLOWING"
    )
    
    # Create yield curve build settings
    settings = create_ir_curve_build_settings(
        curve_name="USD_LIBOR_3M",
        discount_curves=[],
        forward_curves=[]
    )
    
    # Create market data set with quotes
    quotes = [
        ("USD_LIBOR_3M_1M", 0.0255),
        ("USD_LIBOR_3M_3M", 0.0265),
        ("USD_LIBOR_3M_6M", 0.0275),
        ("USD_LIBOR_3M_1Y", 0.0285)
    ]
    
    mkt_data = create_ir_market_data_set(
        as_of_date=as_of_date,
        quotes=quotes
    )
    
    # Build yield curve (creates and stores a yield curve as static data)
    curve = build_yield_curve(
        settings=settings,
        mkt_data=mkt_data
    )
    
    # Now the yield curve is available in the object cache for pricing and other calculations
