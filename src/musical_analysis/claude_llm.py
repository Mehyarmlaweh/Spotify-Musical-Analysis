import os
from dotenv import load_dotenv
import json
import boto3
import streamlit as st

load_dotenv()
INFERENCE_PROFILE_ID = os.getenv("INFERENCE_PROFILE_ID")
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

def call_claude_llm(prompt):
    try:
        # Initialize AWS Bedrock client
        bedrock = boto3.client(service_name="bedrock-runtime",
                                aws_access_key_id=ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                region_name="eu-west-3")  

        # Prepare the payload
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                    ]
                }
            ],
            "max_tokens": 8000,
            "anthropic_version": "bedrock-2023-05-31"
        }

        # Invoke Claude LLM
        response = bedrock.invoke_model(
            modelId=INFERENCE_PROFILE_ID,  
            contentType="application/json",
            body=json.dumps(payload),
        )

        # Parse the response
        output_binary = response["body"].read()
        output_json = json.loads(output_binary)
        output = output_json["content"][0]["text"]
        return output
    except Exception as e:
        st.error(f"Error calling Claude LLM: {e}")
        return None