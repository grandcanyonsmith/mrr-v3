# Market Research Report Generator (MRR v3)

A comprehensive market research report generator that analyzes course ideas and generates detailed market research reports with interactive visualizations.

## Features

- **Deep Market Research**: Uses OpenAI's o3-deep-research model with web search capabilities
- **Interactive Reports**: Generates HTML reports with charts, analytics, and visualizations
- **Audio Generation**: Creates TTS audio explanations for reports
- **S3 Integration**: Automatically uploads reports to S3 with public URLs
- **DynamoDB Tracking**: Stores report metadata with temporary IDs for tracking
- **Cloudflare Workers**: Serves reports via CDN for fast global access

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Test Event    │───▶│  Lambda Function │───▶│  Market Report  │
│   (JSON)        │    │   (config.py)    │    │   (HTML + JS)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   S3 Storage     │
                       │   + DynamoDB     │
                       └──────────────────┘
```

## Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd mrr-v3

# Install dependencies
pip install openai boto3 requests

# Set environment variables
export OPENAI_API_KEY="your-openai-api-key"
export AWS_REGION="us-west-2"
export PAGES_BUCKET="your-s3-bucket"
```

### 2. Test the System

```bash
# Run the mock test to see the API call structure
python test_api_call_structure_fixed.py

# Run the full pipeline test
python test_lambda_mock.py
```

### 3. Create a Test Event

```json
{
  "name": "John Doe",
  "phone": "1234567890",
  "course_description": "Your course idea description here"
}
```

## API Structure

The system uses OpenAI's o3-deep-research model with web search capabilities:

```python
response = client.responses.create(
  model="o3-deep-research",
  input=[
    {
      "role": "developer",
      "content": [{"type": "input_text", "text": prompt}]
    },
    {
      "role": "user", 
      "content": [{"type": "input_text", "text": course_description}]
    }
  ],
  text={},
  tools=[{"type": "web_search_preview"}],
  store=True
)
```

## Output

The system generates:

1. **Market Research Report**: Comprehensive analysis with 7 sections
2. **Interactive HTML**: Visual charts and analytics
3. **JavaScript Data**: Structured courseData object
4. **Audio Explanation**: TTS narration of the report
5. **Public URL**: Accessible via Cloudflare Workers

### Example Object URL
```
https://coursecreator360.com/examples/market-research-reports/
{unique-id}.html?temp_market_research_id={temp-id}
```

## File Structure

```
mrr-v3/
├── config.py                          # Main configuration and prompts
├── lambda_function.py                 # AWS Lambda handler
├── market_research_report_template.html # HTML template
├── test_event.json                    # Sample test event
├── test_*.py                          # Test scripts
└── README.md                          # This file
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Required |
| `AWS_REGION` | AWS region | `us-west-2` |
| `PAGES_BUCKET` | S3 bucket for reports | `cc360-pages` |
| `MODEL_RESEARCH` | OpenAI model for research | `o3-deep-research` |
| `MODEL_COURSEDATA` | OpenAI model for data | `o3-deep-research` |

## Deployment

### AWS Lambda Deployment

1. Package the function:
```bash
zip -r lambda_function.zip . -x "*.pyc" "__pycache__/*" "*.git*"
```

2. Upload to AWS Lambda:
```bash
aws lambda update-function-code \
  --function-name your-function-name \
  --zip-file fileb://lambda_function.zip
```

### Environment Setup

Set the following environment variables in your Lambda function:
- `OPENAI_API_KEY`
- `PAGES_BUCKET`
- `AUDIO_LAMBDA_URL`
- `MARKET_RESEARCH_TABLE`

## Testing

Run the test suite:

```bash
# Test API call structure
python test_api_call_structure_fixed.py

# Test full pipeline (mock)
python test_lambda_mock.py

# Test with real API (requires API key)
python test_runner_fixed.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub. 