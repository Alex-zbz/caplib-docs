Utility
=======

This section covers the utility functions available in the caplib.utility module.

.. contents:: Table of Contents
   :local:
   :depth: 2

Byte Conversion Functions
----------------------

The module provides utility functions for converting data between different formats.

.. code-block:: python

    from caplib.utility import num_to_bytes
    
    # Convert a list of integers to a byte string
    integers = [65, 66, 67, 68]  # ASCII values for 'ABCD'
    byte_string = num_to_bytes(integers)
    
    print(byte_string)  # b'ABCD'

Use Cases
-------

The utility functions are primarily used for internal data conversion operations within the caplib library, particularly when working with binary protocols and serialization.

Example: Working with Binary Data
-----------------------------

Here's an example showing how the utility functions might be used when working with binary data:

.. code-block:: python

    from caplib.utility import num_to_bytes
    
    # Create a list of integers representing data
    data = [1, 2, 3, 4, 5]
    
    # Convert to byte string
    byte_data = num_to_bytes(data)
    
    # The byte string can now be used for operations like:
    # - Writing to a binary file
    # - Sending over a network
    # - Passing to a function that expects binary data
    
    # Example: Writing binary data to a file
    with open("data.bin", "wb") as f:
        f.write(byte_data)
    
    # Example: Reading the data back
    with open("data.bin", "rb") as f:
        read_data = f.read()
        
    print(read_data)  # Should match byte_data

Working with Protocol Buffers
--------------------------

The utility functions can be helpful when working with protocol buffer messages that require binary data:

.. code-block:: python

    from caplib.utility import num_to_bytes
    from caplibproto.dqproto import SomeMessage  # Hypothetical message type
    
    # Create binary data
    data_values = [10, 20, 30, 40, 50]
    binary_data = num_to_bytes(data_values)
    
    # Create a protocol buffer message with binary data
    message = SomeMessage()
    message.binary_field = binary_data
    
    # Serialize the message
    serialized_message = message.SerializeToString()
    
    # This could then be sent to a service using process_request
    from caplib.processrequest import process_request
    
    response = process_request(
        service_name="SOME_SERVICE",
        pb_input_bin=serialized_message
    )
