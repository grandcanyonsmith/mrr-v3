#!/bin/bash

# Market Research Report Generator v3 - Deployment Script
# This script packages and deploys the Lambda function to AWS

set -e

echo "🚀 Starting deployment of MRR v3..."

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI is not installed. Please install it first."
    exit 1
fi

# Check if function name is provided
if [ -z "$1" ]; then
    echo "❌ Please provide the Lambda function name as an argument."
    echo "Usage: ./deploy.sh <function-name>"
    exit 1
fi

FUNCTION_NAME=$1

echo "📦 Creating deployment package..."

# Remove old package if it exists
rm -f lambda_function.zip

# Create new package
zip -r lambda_function.zip . \
    -x "*.pyc" \
    -x "__pycache__/*" \
    -x "*.git*" \
    -x "test_*.py" \
    -x "README.md" \
    -x ".gitignore" \
    -x "requirements.txt" \
    -x "deploy.sh" \
    -x "lambda_function.zip"

echo "✅ Package created: lambda_function.zip"

# Check if function exists
if aws lambda get-function --function-name $FUNCTION_NAME &> /dev/null; then
    echo "🔄 Updating existing function: $FUNCTION_NAME"
    aws lambda update-function-code \
        --function-name $FUNCTION_NAME \
        --zip-file fileb://lambda_function.zip
else
    echo "❌ Function $FUNCTION_NAME does not exist."
    echo "Please create the Lambda function first with the following configuration:"
    echo ""
    echo "Runtime: Python 3.11"
    echo "Handler: lambda_function.lambda_handler"
    echo "Timeout: 15 minutes"
    echo "Memory: 512 MB (recommended)"
    echo ""
    echo "Required environment variables:"
    echo "- OPENAI_API_KEY"
    echo "- PAGES_BUCKET"
    echo "- AUDIO_LAMBDA_URL"
    echo "- MARKET_RESEARCH_TABLE"
    echo ""
    echo "You can create it using:"
    echo "aws lambda create-function \\"
    echo "  --function-name $FUNCTION_NAME \\"
    echo "  --runtime python3.11 \\"
    echo "  --handler lambda_function.lambda_handler \\"
    echo "  --role arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role \\"
    echo "  --zip-file fileb://lambda_function.zip"
    exit 1
fi

echo "✅ Deployment completed successfully!"
echo ""
echo "🔗 Function URL: https://github.com/grandcanyonsmith/mrr-v3"
echo "📋 Test the function with the test_event.json file"
echo ""
echo "To test locally:"
echo "python test_lambda_mock.py" 