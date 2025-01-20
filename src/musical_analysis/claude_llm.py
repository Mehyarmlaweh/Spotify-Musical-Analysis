import json
import boto3
import streamlit as st

def call_claude_llm(image_base64, prompt):
    try:
        # Initialize AWS Bedrock client
        bedrock = boto3.client(service_name="bedrock-runtime", region_name="eu-west-3")  

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
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_base64
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 8000,
            "anthropic_version": "bedrock-2023-05-31"
        }

        # Invoke Claude LLM
        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",  
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