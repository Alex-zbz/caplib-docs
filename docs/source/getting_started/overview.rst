Overview
========

About CapLib
-----------

CapLib is a comprehensive Python library for financial analytics, providing tools for pricing, risk management, and market data processing across multiple asset classes. The library is designed for finance professionals, quants, and developers working with financial instruments and markets.

Key Features
-----------

* **Multi-asset coverage**: Fixed Income, Credit, FX, Equity, and Commodity markets
* **Unified analytics interface**: Consistent API across all asset classes
* **Market data handling**: Tools for curve construction, volatility surfaces, and time series
* **Risk management**: VaR, CVaR, stress testing, and scenario analysis
* **Modern architecture**: Built on gRPC for efficient client-server communication
* **Extensible design**: Easily add custom models and instruments

Asset Class Modules
------------------

CapLib is organized by asset class, with dedicated analytics modules for each:

**Fixed Income**
  * ``iranalytics``: Interest rate curve building, forward rate calculation, and swap pricing
  * ``irmarket``: Interest rate market data types and conversions
  * ``fianalytics``: Fixed income securities analysis including bonds and structured products

**Credit**
  * ``cranalytics``: CDS pricing, credit curve construction, and credit risk metrics
  * ``crmarket``: Credit market data types and CDS templates

**Foreign Exchange**
  * ``fxanalytics``: FX options pricing, volatility surface construction, and exotic products
  * ``fxmarket``: FX forward and swap templates, market data handling

**Equity**
  * ``eqanalytics``: Equity options, volatility models, and structured products

**Commodity**
  * ``cmanalytics``: Commodity derivatives pricing and analysis
  * ``cmmarket``: Commodity market data handling and templates

Core Utilities
-------------

Several core modules provide essential functionality across all asset classes:

* ``analytics``: Common analytics functions and enumeration conversions
* ``market``: Market data types, conversions, and time series management
* ``datetime``: Date calculations, period handling, and schedule generation
* ``numerics``: Numerical methods, matrix operations, and random number generation
* ``mktrisk``: Market risk metrics, scenario generation, and risk factor analysis
* ``processrequest``: Client-server communication with the caplib backend

Using caplib for Financial Analysis
----------------------------------

caplib is designed to be used in different ways:

1. **For pricing individual instruments**: Quickly value financial instruments with market-standard models
2. **For portfolio analysis**: Analyze risk and return across portfolios of mixed asset classes
3. **For market data processing**: Build curves, surfaces, and other market data constructs
4. **For automating workflows**: Create end-to-end processing pipelines for trading and risk
