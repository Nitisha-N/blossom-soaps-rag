# 📚 Enterprise RAG System with Amazon Bedrock

## 📌 Introduction

Traditional enterprise search systems often fail to deliver accurate and relevant results due to their reliance on keyword-based matching. At the same time, Large Language Models (LLMs) can generate fluent answers but may hallucinate when dealing with proprietary or recent data.

This project solves both challenges using **Retrieval-Augmented Generation (RAG)** powered by **Amazon Bedrock Knowledge Bases**, enabling accurate, context-aware, and citation-backed responses from internal enterprise data.

---

## 📑 Table of Contents

* [Problem Statement](#-problem-statement)
* [Solution Overview](#-solution-overview)
* [Features](#-features)
* [Architecture](#-architecture)
* [Technologies Used](#-technologies-used)
* [Installation](#-installation)
* [Usage](#-usage)
* [Examples](#-examples)
* [Deployment](#-deployment)
* [Troubleshooting](#-troubleshooting)
* [Contributors](#-contributors)
* [License](#-license)

---

## 🔴 Problem Statement

### Traditional Enterprise Systems

* Depend on keyword-based search
* Lack understanding of natural language queries
* Often return irrelevant or incomplete results

### Limitations of LLMs

* Can generate fluent responses
* But may hallucinate when data is:

  * Proprietary
  * Recent
  * Not included in training data

---

## 🟢 Solution Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system using **Amazon Bedrock Knowledge Bases** to combine semantic search with grounded LLM responses.

---

## ✨ Features

### 🧠 1. Semantic Understanding

* Uses **vector embeddings (Titan Embeddings)**
* Performs **semantic search instead of keyword matching**
* Understands **user intent**

✅ **Result:**
Users can ask natural questions like:

> “Do we get maternity leave?”
> Instead of searching exact keywords.

---

### 🤖 2. Eliminating Hallucinations

* Retrieves relevant document chunks from **Amazon S3**
* Passes context to **Amazon Nova LLM**
* Generates grounded responses

✅ **Result:**

* No guessing
* No hallucinations
* Fact-based answers

---

### 📄 3. Citation-Backed Responses

* Each answer includes:

  * Source document reference
  * Extracted supporting content

✅ **Result:**

* Transparency
* Verifiable answers
* Increased trust

---

### 🔐 4. Enterprise Data Integration

* Uses **private internal documents**
* Stored securely in **Amazon S3**
* Indexed via **Bedrock Knowledge Base**

✅ **Result:**

* Works with proprietary data
* No dependency on public internet

---

### ⚙️ 5. Managed RAG with Amazon Bedrock

* **Amazon Bedrock Knowledge Bases**
* **OpenSearch Serverless (vector store)**
* **Titan Embeddings + Nova LLM**

✅ **Result:**

* No manual vector DB setup
* Scalable & production-ready

---

### 💻 6. Streamlit Web Interface

* Chat-based UI
* Natural language input
* Displays responses with sources

✅ **Result:**

* User-friendly
* Accessible for non-technical users

---

### ☁️ 7. AWS Deployment

* Hosted on **EC2**
* Secure access using **IAM**

✅ **Result:**

* Real-world deployment
* Secure and scalable infrastructure

---

## 🏗️ Architecture

```
User Query (Streamlit UI)
        ↓
Semantic Search (Titan Embeddings)
        ↓
Bedrock Knowledge Base
        ↓
Retrieve Relevant Chunks (S3)
        ↓
Amazon Nova LLM
        ↓
Response + Citations
```

---

## 🧰 Technologies Used

* **AWS Services**

  * Amazon Bedrock
  * Bedrock Knowledge Bases
  * OpenSearch Serverless
  * Amazon S3
  * EC2
  * IAM

* **AI Models**

  * Titan Embeddings
  * Amazon Nova LLM

* **Frontend**

  * Streamlit

---

## ⚙️ Installation

```bash
# Clone repository
git clone <your-repo-url>
cd <project-folder>

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

* Open browser at `http://localhost:8501`
* Ask questions in natural language
* View responses with citations

---

## 💡 Examples

**User Query:**

```
Do we get maternity leave?
```

**System Behavior:**

* Searches internal HR documents
* Retrieves relevant sections
* Generates grounded response with source

---

## 🚀 Deployment

* Deploy on **AWS EC2**
* Configure IAM credentials for Bedrock access
* Ensure:

  * S3 bucket is connected
  * Knowledge Base is indexed
  * OpenSearch is active

---

## 🛠️ Troubleshooting

| Issue              | Possible Cause         | Solution              |
| ------------------ | ---------------------- | --------------------- |
| No response        | Bedrock not configured | Check IAM permissions |
| Irrelevant answers | Poor document chunking | Improve preprocessing |
| Slow responses     | Large dataset          | Optimize indexing     |

---

## 👥 Contributors

* Nitisha Naigaonkar | IRL Intern

---
