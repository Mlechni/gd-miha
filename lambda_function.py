import main

def lambda_handler(event, lambda_context):
    return main.test_event() + " -- hello world"