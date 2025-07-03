#!/usr/bin/env python3
"""
Test script to demonstrate config.py functionality and object URL generation
"""

import json
import uuid
from datetime import datetime


def generate_mock_course_data(course_description):
    """Generate mock course data based on the course description"""
    
    # Extract course topic from description
    course_topic = course_description.split(" - ")[0] if " - " in course_description else course_description
    
    return {
        "brandColors": {
            "background": "#F6F9FC",
            "primary": "#0A2540", 
            "text": "#1F2937",
            "textSecondary": "#4B5563",
            "accent": "#3B82F6",
            "border": "#E5E7EB"
        },
        "meta": {
            "courseTitle": course_topic,
            "reportTitle": f"{course_topic} Market Research Report 2025"
        },
        "demand": {
            "score": 7.5,
            "percentile": 78,
            "question": f"Should you create a {course_topic.lower()} course?",
            "answer": "Yes—demand is strong and growing.",
            "why": f"• {course_topic} searches are up 45% vs 2020 • Growing interest in skill development • Limited comprehensive resources available"
        },
        "testing": {
            "overview": f"Master {course_topic.lower()} fundamentals and advanced techniques",
            "targetAudience": "Aspiring professionals and career changers",
            "format": "6-week cohort: 12 modules, video content, live Q&A, community access",
            "question": f"Why this {course_topic.lower()} course over free resources?",
            "answer": "Comprehensive, structured learning with expert guidance",
            "why": "Free resources are scattered and lack systematic approach",
            "contentPillars": [
                f"Core {course_topic.lower()} principles",
                "Practical application techniques", 
                "Industry best practices",
                "Career development strategies"
            ]
        },
        "trends": {
            "googleSearchChangePct": 45,
            "socialMediaGrowthPct": 32,
            "macroFactor": "Growing demand for skill-based education",
            "question": "Is interest still climbing?",
            "answer": "Yes—searches and social engagement are accelerating",
            "why": f"• '{course_topic}' searches +45% in 5 years • Social media communities growing rapidly • Economic shifts driving skill development"
        },
        "competitors": {
            "question": f"Who else teaches {course_topic.lower()}?",
            "answer": "Several options exist, but none offer our comprehensive approach",
            "why": "Most competitors focus on specific aspects rather than complete education",
            "list": [
                {
                    "name": f"Udemy — {course_topic} Masterclass",
                    "strengths": "Affordable, basic coverage",
                    "weaknesses": "Limited depth, no community",
                    "priceUSD": 29.99,
                    "websiteUrl": "https://www.udemy.com/",
                    "logoUrl": "https://s.udemycdn.com/meta/default-meta-image-v2.png"
                },
                {
                    "name": f"Skillshare — {course_topic} Essentials",
                    "strengths": "Creative approach, good production",
                    "weaknesses": "Short format, limited interaction",
                    "priceUSD": 99,
                    "websiteUrl": "https://www.skillshare.com/",
                    "logoUrl": "https://www.skillshare.com/favicon.ico"
                },
                {
                    "name": f"LinkedIn Learning — {course_topic} Professional",
                    "strengths": "Professional focus, certification",
                    "weaknesses": "Corporate-centric, expensive",
                    "priceUSD": 299,
                    "websiteUrl": "https://www.linkedin.com/learning/",
                    "logoUrl": "https://www.linkedin.com/favicon.ico"
                }
            ]
        },
        "worries": {
            "question": "What keeps learners up at night?",
            "answer": "Career uncertainty, skill gaps, and market competition",
            "why": "Surveys show 70%+ citing career advancement as primary concern",
            "topConcerns": [
                "Will this actually help me advance my career?",
                "Is the content up-to-date with industry standards?",
                "Can I apply this knowledge immediately?",
                "Is the investment worth the return?"
            ]
        },
        "pricing": {
            "question": "What will the market pay?",
            "answer": "$199 list price positions us competitively in the market",
            "why": "Market research shows learners willing to pay $150-300 for comprehensive courses",
            "targetPriceUSD": 199
        },
        "buildDecision": {
            "question": "Based on the data, should we build it?",
            "answer": "GO",
            "why": "Strong demand, clear differentiation opportunity, and positive market indicators"
        },
        "revenueOutlook": {
            "launchTimelineDays": 60,
            "likelyRevenueUSD": 45000,
            "industryAverageUSD": 52000,
            "scenarios": [
                {"name": "Lower", "students": 100, "priceUSD": 149, "revenueUSD": 14900},
                {"name": "Mid", "students": 300, "priceUSD": 149, "revenueUSD": 44700},
                {"name": "High", "students": 800, "priceUSD": 149, "revenueUSD": 119200}
            ],
            "question": "What's the 12-month upside?",
            "answer": "Realistically $45k gross on a 300-student year-one cohort",
            "why": "Assumes 25% promo rate and 2% conversion from target audience"
        },
        "opportunityScore": 78
    }


def generate_object_url(course_data, temp_id):
    """Generate the S3 object URL for the market research report"""
    
    # This would normally be uploaded to S3
    # For testing, we'll simulate the URL structure
    bucket = "cc360-pages"
    region = "us-west-2"
    folder = "reports"
    
    # Generate filename based on course title and timestamp
    course_title = course_data["meta"]["courseTitle"].replace(" ", "-").lower()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{course_title}-market-research-{timestamp}.html"
    
    # Construct S3 URL
    s3_url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}/{filename}"
    
    # Add temp ID parameter for tracking
    final_url = f"{s3_url}?temp_market_research_id={temp_id}"
    
    return final_url


def main():
    # Load test event
    with open('test_event.json', 'r') as f:
        test_event = json.load(f)
    
    print("=== Test Event ===")
    print(json.dumps(test_event, indent=2))
    print()
    
    # Generate mock course data
    course_data = generate_mock_course_data(test_event["course_description"])
    
    print("=== Generated Course Data ===")
    print(json.dumps(course_data, indent=2))
    print()
    
    # Generate temp ID
    temp_id = str(uuid.uuid4())
    
    # Generate object URL
    object_url = generate_object_url(course_data, temp_id)
    
    print("=== Object URL Outcome ===")
    print(f"Generated URL: {object_url}")
    print()
    print(f"Temp ID: {temp_id}")
    print(f"Course: {course_data['meta']['courseTitle']}")
    print(f"Opportunity Score: {course_data['opportunityScore']}/100")
    print(f"Demand Score: {course_data['demand']['score']}/10")
    print(f"Target Price: ${course_data['pricing']['targetPriceUSD']}")
    print(f"Likely Revenue: ${course_data['revenueOutlook']['likelyRevenueUSD']:,}")


if __name__ == "__main__":
    main() 