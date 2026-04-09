import boto3
from config.aws_config import AWS_REGION, KNOWLEDGE_BASE_ID

bedrock_agent = boto3.client("bedrock-agent-runtime", region_name=AWS_REGION)


def retrieve_and_generate(query):
    try:
        response = bedrock_agent.retrieve_and_generate(
            input={
                "text": f"""
You are an HR assistant for Blossom Soaps.

Answer clearly and professionally using ONLY company policies.

Question:
{query}
"""
            },
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",   
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                    "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-lite-v1:0"
                }
            }
        )

        answer = response["output"]["text"]

        sources = []
        seen = set()

        for citation in response.get("citations", []):
            for ref in citation.get("retrievedReferences", []):
                uri = ref["location"]["s3Location"]["uri"]
                filename = uri.split("/")[-1]

                if filename not in seen:
                    seen.add(filename)
                    sources.append({
                        "file": filename,
                        "content": ref["content"]["text"][:200]
                    })

        return answer, sources

    except Exception as e:
        return f"Error: {str(e)}", []
