Importing
=========

This section covers how to import and use the caplib analytics modules in your Python code.

Basic Usage
----------

To use caplib in your Python project:

.. code-block:: python

    import caplib
    
    # Core analytics utilities
    from caplib import analytics
    from caplib import market
    from caplib import numerics

Analytics Modules
----------------

caplib offers specialized analytics modules for different asset classes:

.. code-block:: python

    # Fixed Income Analytics
    from caplib import iranalytics    # Interest Rate Analytics
    from caplib import fianalytics    # Fixed Income Products Analytics
    
    # Credit Analytics
    from caplib import cranalytics    # Credit Default Swap Analytics
    from caplib import crmarket       # Credit Market Data
    
    # Foreign Exchange Analytics
    from caplib import fxanalytics    # FX Options and Forward Analytics
    from caplib import fxmarket       # FX Market Data
    
    # Equity Analytics
    from caplib import eqanalytics    # Equity Options and Products
    
    # Commodity Analytics
    from caplib import cmanalytics    # Commodity Options and Products
    from caplib import cmmarket       # Commodity Market Data

Market Data and Utilities
------------------------

For common utilities and data handling:

.. code-block:: python

    # Date and Time utilities
    from caplib import datetime
    
    # Market data handling
    from caplib import market
    from caplib import staticdata
    
    # Risk management
    from caplib import mktrisk

Complete Example
---------------

Here's a simple example showing how to use multiple caplib modules together:

.. code-block:: python

    import pandas as pd
    from caplib import market
    from caplib import iranalytics
    from caplib import datetime
    
    # Create a valuation date
    val_date = datetime.create_date(2025, 3, 20)
    
    # Set up market data
    curve_points = [
        (datetime.create_tenor("1M"), 0.0425),
        (datetime.create_tenor("3M"), 0.0450),
        (datetime.create_tenor("6M"), 0.0475),
        (datetime.create_tenor("1Y"), 0.0500),
        (datetime.create_tenor("2Y"), 0.0525),
        (datetime.create_tenor("5Y"), 0.0550),
        (datetime.create_tenor("10Y"), 0.0575)
    ]
    
    # Build a yield curve
    curve = iranalytics.create_yield_curve(
        val_date, 
        curve_points, 
        analytics.to_curve_building_method("CubicSpline")
    )
    
    # Calculate forward rates
    fwd_rate = iranalytics.get_forward_rate(
        curve, 
        val_date, 
        datetime.create_tenor("1Y"),
        datetime.create_tenor("2Y")
    )
    
    print(f"1Y1Y Forward Rate: {fwd_rate:.4f}")
