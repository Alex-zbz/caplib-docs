Process Request
==============

This section covers the functionality available in the caplib.processrequest module, which handles communication with the backend service.

.. contents:: Table of Contents
   :local:
   :depth: 2

Overview
-------

The processrequest module provides a bridge between the Python client and the backend service through gRPC (Google Remote Procedure Call). It enables sending serialized protocol buffer requests to the service and receiving serialized responses.

Service Connection
--------------

The module sets up a connection to the gRPC service using the following default settings:

* Host: localhost
* Port: 50051

Basic Usage
---------

.. code-block:: python

    from caplib.processrequest import process_request
    
    # Example: Send a serialized protocol buffer request to the service
    # The request should be a binary serialized protocol buffer message
    response_bin = process_request(
        service_name="SERVICE_NAME",
        pb_input_bin=serialized_request
    )
    
    # The response is also a binary serialized protocol buffer message
    # It needs to be parsed using the appropriate protocol buffer class
    from caplibproto.dqproto import SomeResponseType
    
    response = SomeResponseType()
    response.ParseFromString(response_bin)

Example with a Complete Workflow
----------------------------

Here's a complete example showing how the process_request function is used in the context of other caplib modules:

.. code-block:: python

    from caplib.processrequest import process_request
    from caplibproto.dqproto import (
        RiskFactorChangeCalculationInput,
        RiskFactorChangeType,
        RiskFactorChangeCalculationOutput
    )
    from caplib.mktrisk import calculate_risk_factor_change
    
    # Step 1: Prepare risk factor values
    risk_factor_values = [100.0, 101.2, 99.8, 102.5, 103.1]
    
    # Step 2: Calculate risk factor changes using a function that internally uses process_request
    changes = calculate_risk_factor_change(
        risk_factor_values=risk_factor_values,
        change_type="LOG_RETURN"
    )
    
    # Behind the scenes, this is what's happening:
    # 1. Create a protocol buffer input message
    pb_input = RiskFactorChangeCalculationInput()
    pb_input.type = RiskFactorChangeType.LOG_RETURN
    pb_input.samples.extend(risk_factor_values)
    
    # 2. Serialize the message
    serialized_request = pb_input.SerializeToString()
    
    # 3. Send the request to the service
    response_bin = process_request(
        service_name="RISK_FACTOR_CHANGE_CALCULATOR",
        pb_input_bin=serialized_request
    )
    
    # 4. Parse the response
    pb_output = RiskFactorChangeCalculationOutput()
    pb_output.ParseFromString(response_bin)
    
    # 5. Check for errors and return the result
    if not pb_output.success:
        raise Exception(pb_output.err_msg)
    
    result = pb_output.result
    
    # (The calculate_risk_factor_change function handles all these steps for you)

Error Handling
-----------

The process_request function will raise an exception if the gRPC call fails, or if the service returns an empty response. Additionally, many caplib functions that use process_request will check the success field in the response and raise an exception with the error message if the service reports an error.

.. code-block:: python

    from caplib.processrequest import process_request
    
    try:
        response_bin = process_request(
            service_name="SERVICE_NAME",
            pb_input_bin=serialized_request
        )
        
        # Parse response
        response = SomeResponseType()
        response.ParseFromString(response_bin)
        
        # Check for service-reported errors
        if not response.success:
            raise Exception(f"Service error: {response.err_msg}")
            
        # Process successful response
        result = response.result
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

Advanced Usage
-----------

For advanced use cases, you might need to create custom requests to the backend service. Here's a template for doing so:

.. code-block:: python

    import grpc
    from caplibproto.dqlib_pb2 import DqlibRequest
    from caplibproto.dqlib_pb2_grpc import DqlibServiceStub
    
    # Custom connection parameters
    host = 'localhost'
    port = '50051'
    
    # Create a gRPC channel
    channel = grpc.insecure_channel(f"{host}:{port}")
    
    # Create a client stub
    client = DqlibServiceStub(channel=channel)
    
    # Create and serialize a request message
    from caplibproto.dqproto import CustomRequestType
    
    request = CustomRequestType()
    request.field1 = value1
    request.field2 = value2
    
    serialized_request = request.SerializeToString()
    
    # Send the request
    response = client.RemoteCall(DqlibRequest(
        name="CUSTOM_SERVICE_NAME",
        serialized_request=serialized_request
    ))
    
    # Parse the response
    from caplibproto.dqproto import CustomResponseType
    
    parsed_response = CustomResponseType()
    parsed_response.ParseFromString(response.serialized_response)
    
    # Process the result
    result = parsed_response.result
