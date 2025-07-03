#!/usr/bin/env python3
"""
Test runner for the market research lambda function
"""

import json
import os
from lambda_function import lambda_handler


def main():
    # Load the test event
    with open('test_event.json', 'r') as f:
        test_event = json.load(f)
    
    print("=== Test Event ===")
    print(json.dumps(test_event, indent=2))
    print()
    
    # Set up environment variables for testing
    os.environ.setdefault('AWS_REGION', 'us-west-2')
    os.environ.setdefault('PAGES_BUCKET', 'cc360-pages')
    os.environ.setdefault('FOLDER_VALUES', 'reports')
    os.environ.setdefault('FOLDER_HTML', 'reports')
    os.environ.setdefault('MODEL_RESEARCH', 'o3')
    os.environ.setdefault('MODEL_COURSEDATA', 'o3')
    audio_url = ('https://rqs4p4vd3boceuneltib5kjc3e0pccoo.lambda-url.'
                'us-west-2.on.aws/')
    os.environ.setdefault('AUDIO_LAMBDA_URL', audio_url)
    os.environ.setdefault('MARKET_RESEARCH_TABLE', 'CourseMarketResearchReports')
    
    print("=== Running Lambda Function ===")
    try:
        # Create a mock context
        class MockContext:
            def __init__(self):
                self.function_name = "test_function"
                self.function_version = "1"
                arn = "arn:aws:lambda:us-west-2:123456789012:function:test_function"
                self.invoked_function_arn = arn
                self.memory_limit_in_mb = 128
                self.remaining_time_in_millis = lambda: 30000
                self.aws_request_id = "test-request-id"

        context = MockContext()
        
        # Format the event properly for lambda
        lambda_event = {
            "body": json.dumps(test_event)
        }
        
        # Call the lambda handler
        result = lambda_handler(lambda_event, context)
        
        print("=== Lambda Result ===")
        print(json.dumps(result, indent=2))
        
        # Extract the object URL
        if 'body' in result:
            body = json.loads(result['body'])
            if 'url' in body:
                print(f"\n=== Object URL ===")
                print(f"Generated URL: {body['url']}")
            else:
                print(f"\n=== No URL in response ===")
                print(f"Response body: {body}")
        else:
            print(f"\n=== No body in response ===")
            print(f"Response: {result}")
            
    except Exception as e:
        print(f"Error running lambda function: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 