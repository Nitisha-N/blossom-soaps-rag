Blossom Soaps: Employee FAQs (RAG System)

Overview
This project implements a Retrieval-Augmented Generation (RAG) based Question-Answering system using Amazon Bedrock Knowledge Bases. It allows employees to ask natural language questions about internal company documents and receive accurate, citation-backed responses.

Features

* Natural language question answering
* Responses grounded in internal documents
* Citation-based answers
* Clean chat interface using Streamlit
* AWS-native architecture
* Uses Amazon Nova model

Tech Stack
Frontend: Streamlit
Backend: Python (boto3)
LLM: Amazon Nova (Bedrock)
RAG: Bedrock Knowledge Base
Storage: Amazon S3
Vector Store: OpenSearch Serverless
Deployment: AWS EC2

Architecture
User Query → Streamlit → Bedrock KB → Retrieve → Nova → Response with citations

Project Structure
AMAZON BEDROCK/
app/
streamlit\_app.py
backend/
rag\_service.py
config/
aws\_config.py

Setup

1. Install dependencies:
pip install -r requirements.txt
2. Configure AWS:
aws configure
3. Update config/aws\_config.py:
AWS\_REGION = "us-east-1"
KNOWLEDGE\_BASE\_ID = "YOUR\_KB\_ID"
4. Run:
streamlit run app/streamlit\_app.py

Sample Queries

* What is maternity leave policy?
* Do employees get WFH?
* What are employee benefits?

Notes

* Sync Knowledge Base before use
* Use IAM user, not root
* Keep region consistent

Future Improvements

* Role-based access
* Document upload integration
* Voice input
* API layer

Author
Nitisha Naigaonkar | Innomatics Research Lab Intern

