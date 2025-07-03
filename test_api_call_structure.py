#!/usr/bin/env python3
"""
Test script showing the exact OpenAI API call structure with web search tools
"""

import json
from config import course_description_to_market_research_report_prompt


def show_api_call_structure():
    """Show the exact API call structure for the deep research model"""
    
    # Load test event
    with open('test_event.json', 'r') as f:
        test_event = json.load(f)
    
    course_description = test_event["course_description"]
    
    print("=== Test Event ===")
    print(json.dumps(test_event, indent=2))
    print()
    
    print("=== OpenAI API Call Structure ===")
    print("from openai import OpenAI")
    print("client = OpenAI()")
    print()
    print("response = client.responses.create(")
    print('  model="o3-deep-research",')
    print("  input=[")
    print("    {")
    print('      "role": "developer",')
    print('      "content": [')
    print("        {")
    print('          "type": "input_text",')
    print('          "text": """' + course_description_to_market_research_report_prompt + '"""')
    print("        }")
    print("      ]")
    print("    },")
    print("    {")
    print('      "role": "user",')
    print('      "content": [')
    print("        {")
    print('          "type": "input_text",')
    print(f'          "text": "Course Idea: {course_description}"')
    print("        }")
    print("      ]")
    print("    }")
      print("  ],")
  print("  text={},")
  print("  tools=[{")
  print('    "type": "web_search_preview"')
  print("  }],")
  print("  store=True")
    print(")")
    print()
    
    print("=== Expected Object URL Outcome ===")
    print("After successful API call, the system would:")
    print("1. Generate market research report")
    print("2. Create courseData JavaScript object")
    print("3. Upload files to S3")
    print("4. Return URL like:")
    print("   https://coursecreator360.com/examples/market-research-reports/")
    print("   {unique-id}.html?temp_market_research_id={temp-id}")
    print()
    
    print("=== Key Changes Made ===")
    print("✓ Added tools=[{\"type\": \"web_search_preview\"}]")
    print("✓ Set store=True")
    print("✓ Configured for o3-deep-research model")
    print("✓ No reasoning parameter (not supported by o3-deep-research)")
    print()
    
    print("=== Mock Response Structure ===")
    mock_response = {
        "output": [
            {
                "type": "message",
                "content": [
                    {
                        "type": "text",
                        "text": "Market Research Report for 'How to model'..."
                    }
                ]
            }
        ]
    }
    print(json.dumps(mock_response, indent=2))


if __name__ == "__main__":
    show_api_call_structure() 