#!/usr/bin/env python3
"""
Mock lambda test that simulates the full pipeline without external API calls
"""

import json
import uuid
from datetime import datetime


def mock_openai_call(model, prompt, user_input, log):
    """Mock OpenAI call that returns predefined responses"""
    if "market research" in prompt.lower():
        return """Market Research Report for "How to model"

0 · Is It Worth It? (Demand Score: 7.8/10, 82nd percentile)
The modeling industry shows strong demand with growing interest in professional development.

1 · What We're Testing
Course focus: Transform aspiring models into industry-ready professionals
Ideal learner: Aspiring models aged 18-35 seeking professional guidance
Delivery format: 8-week cohort with video modules, live coaching, portfolio reviews
Gap analysis: Current resources lack comprehensive industry navigation guidance
Key content pillars: Portfolio development, industry networking, posing mastery, business skills

2 · Big Trends
Search trajectory: "how to model" searches up 67% in 5 years
Social-media signals: Modeling communities growing 45% annually
Macro forces: Social media democratizing modeling, increasing demand for guidance

3 · Who's Out There (Competitor Landscape)
Top competitors include modeling schools and online courses, but none offer comprehensive industry navigation.

4 · Learner Worries / Pain Points
Primary anxieties: Industry rejection, lack of connections, portfolio quality
Evidence: 75% of aspiring models cite these concerns in surveys

5 · What They'll Pay
Willingness-to-pay: $299-599 for comprehensive programs
Benchmarking: Industry average $450 for similar programs

6 · Should We Build It?
GO - Strong demand, clear differentiation opportunity, positive market indicators

7 · 1-Year Revenue Outlook
Bad scenario: 50 students at $299 = $14,950
Good scenario: 150 students at $399 = $59,850
Excellent scenario: 300 students at $399 = $119,700
Industry average: $45,000
Likely outcome: $60,000 (33% above average)
Scenario drivers: Social media marketing, influencer partnerships, portfolio showcase"""
    else:
        return """window.courseData={brandColors:{background:"#F6F9FC",primary:"#0A2540",text:"#1F2937",textSecondary:"#4B5563",accent:"#3B82F6",border:"#E5E7EB"},meta:{courseTitle:"How to Model Professional",reportTitle:"Modeling Industry Market Research Report 2025"},demand:{score:7.8,percentile:82,question:"Should you create a modeling course?",answer:"Yes—demand is high and growing.",why:"• Modeling searches up 67% in 5 years • Social media democratizing industry access • 75% of aspirants cite guidance needs"},testing:{overview:"Transform aspiring models into industry-ready professionals",targetAudience:"Aspiring models aged 18-35 seeking professional guidance",format:"8-week cohort: 12 modules, video content, live coaching, portfolio reviews",question:"Why this course over free resources?",answer:"Comprehensive industry navigation and professional development",why:"Free resources lack systematic approach and industry connections",contentPillars:["Portfolio development mastery","Industry networking strategies","Professional posing techniques","Business and contract skills"]},trends:{googleSearchChangePct:67,socialMediaGrowthPct:45,macroFactor:"Social media democratizing modeling industry access",question:"Is interest still climbing?",answer:"Yes—searches and social engagement accelerating",why:"• 'How to model' searches +67% in 5 years • Instagram modeling communities growing rapidly • TikTok creating new modeling opportunities"},competitors:{question:"Who else teaches modeling?",answer:"Several options exist, but none offer comprehensive industry navigation",why:"Most focus on specific skills rather than complete career development",list:[{name:"Barbizon Modeling School",strengths:"Established brand, physical locations",weaknesses:"Expensive, outdated methods, limited online presence",priceUSD:2500,websiteUrl:"https://www.barbizonmodeling.com/",logoUrl:"https://www.barbizonmodeling.com/favicon.ico"},{name:"Udemy — Modeling Masterclass",strengths:"Affordable, accessible",weaknesses:"Basic content, no industry connections",priceUSD:29.99,websiteUrl:"https://www.udemy.com/",logoUrl:"https://s.udemycdn.com/meta/default-meta-image-v2.png"},{name:"Modeling Agency Workshops",strengths:"Direct industry access",weaknesses:"Expensive, selective, limited content",priceUSD:800,websiteUrl:"https://www.modelingagency.com/",logoUrl:"https://www.modelingagency.com/favicon.ico"}]},worries:{question:"What keeps learners up at night?",answer:"Industry rejection, lack of connections, portfolio quality",why:"Surveys show 75% citing these as primary concerns",topConcerns:["Will agencies take me seriously?","How do I build industry connections?","Is my portfolio good enough?","Can I make a living modeling?"]},pricing:{question:"What will the market pay?",answer:"$399 list price positions us competitively",why:"Market research shows $299-599 range for comprehensive programs",targetPriceUSD:399},buildDecision:{question:"Based on the data, should we build it?",answer:"GO",why:"Strong demand, clear differentiation, positive market indicators"},revenueOutlook:{launchTimelineDays:60,likelyRevenueUSD:59850,industryAverageUSD:45000,scenarios:[{name:"Lower",students:50,priceUSD:299,revenueUSD:14950},{name:"Mid",students:150,priceUSD:399,revenueUSD:59850},{name:"High",students:300,priceUSD:399,revenueUSD:119700}],question:"What's the 12-month upside?",answer:"Realistically $60k gross on 150-student cohort",why:"Assumes 20% promo rate and 2% conversion from target audience"},opportunityScore:82};"""


def mock_generate_audio(name, report, log):
    """Mock audio generation"""
    audio_id = uuid.uuid4().hex
    return f"https://cc360-audio.s3.us-west-2.amazonaws.com/{audio_id}.mp3"


def mock_upload_public(key, ctype, body, log):
    """Mock S3 upload"""
    bucket = "cc360-pages"
    region = "us-west-2"
    url = f"https://{bucket}.s3.{region}.amazonaws.com/{key}"
    log.info("Mock uploaded %s", url)
    return url


def mock_pipeline(course_desc, narrator, phone, log):
    """Mock pipeline that simulates the full lambda function process"""
    
    # 1. Market research narrative
    log.info("1/5  Generating narrative")
    report = mock_openai_call("o3", "market research prompt", f"Course Idea: {course_desc}", log)
    
    # 2. courseData + TTS in parallel
    log.info("2/5  Spawning courseData + TTS tasks")
    raw_course = mock_openai_call("o3", "course data prompt", f"market research found: {report}", log)
    audio_url = mock_generate_audio(narrator, report, log)
    
    # 3. Upload values.js
    log.info("3/5  Uploading values.js")
    course_js = raw_course
    if not course_js.lstrip().startswith("window."):
        course_js = "window." + course_js
    js_key = f"reports/{uuid.uuid4().hex}-values.js"
    js_url = mock_upload_public(js_key, "application/javascript; charset=utf-8", body=course_js, log=log)
    
    # 4. Build HTML (simplified)
    log.info("4/5  Building HTML")
    html = f"""<!DOCTYPE html>
<html>
<head><title>Market Research Report</title></head>
<body>
<h1>Market Research Report</h1>
<script src="{js_url}"></script>
<script>
// Audio URL: {audio_url}
</script>
</body>
</html>"""
    
    temp_id = uuid.uuid4().hex
    
    # 5. Upload HTML page
    log.info("5/5  Uploading HTML page")
    html_filename = f"{uuid.uuid4().hex}.html"
    page_key = f"reports/{html_filename}"
    mock_upload_public(page_key, "text/html; charset=utf-8", body=html, log=log)
    
    # Construct final URL
    page_url = f"https://coursecreator360.com/examples/market-research-reports/{html_filename}"
    final_url = f"{page_url}?temp_market_research_id={temp_id}"
    
    log.info("Final URL generated: %s", final_url)
    return final_url


def mock_lambda_handler(event, context):
    """Mock lambda handler that simulates the real one"""
    import logging
    
    req_id = getattr(context, "aws_request_id", uuid.uuid4().hex)
    log = logging.getLogger(f"mock_lambda_{req_id}")
    
    try:
        body = json.loads(event.get("body", "{}"))
        narrator = body["name"]
        phone = body["phone"]
        course_desc = body["course_description"]
    except (KeyError, json.JSONDecodeError) as exc:
        log.warning("Bad request: %s", exc)
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Body must include name, phone, course_description"})
        }
    
    try:
        final_url = mock_pipeline(course_desc, narrator, phone, log)
        
        # Mock webhook call
        log.info("Mock webhook sent for %s", narrator)
        
        return {"statusCode": 200, "body": json.dumps({"url": final_url}, ensure_ascii=False)}
    except Exception as exc:
        log.exception("Unhandled error")
        return {"statusCode": 500, "body": json.dumps({"error": str(exc)})}


def main():
    # Load the test event
    with open('test_event.json', 'r') as f:
        test_event = json.load(f)
    
    print("=== Test Event ===")
    print(json.dumps(test_event, indent=2))
    print()
    
    # Create a mock context
    class MockContext:
        def __init__(self):
            self.function_name = "test_function"
            self.function_version = "1"
            self.invoked_function_arn = "arn:aws:lambda:us-west-2:123456789012:function:test_function"
            self.memory_limit_in_mb = 128
            self.remaining_time_in_millis = lambda: 30000
            self.aws_request_id = "test-request-id"
    
    context = MockContext()
    
    # Format the event properly for lambda
    lambda_event = {
        "body": json.dumps(test_event)
    }
    
    print("=== Running Mock Lambda Function ===")
    try:
        # Call the mock lambda handler
        result = mock_lambda_handler(lambda_event, context)
        
        print("=== Lambda Result ===")
        print(json.dumps(result, indent=2))
        
        # Extract the object URL
        if 'body' in result:
            body = json.loads(result['body'])
            if 'url' in body:
                print(f"\n=== Object URL Outcome ===")
                print(f"Generated URL: {body['url']}")
                
                # Parse the URL to show components
                url = body['url']
                if '?' in url:
                    base_url, params = url.split('?', 1)
                    temp_id = params.split('=')[1]
                    print(f"Base URL: {base_url}")
                    print(f"Temp ID: {temp_id}")
                    print(f"Full URL: {url}")
                else:
                    print(f"URL: {url}")
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