from ollama import chat
from cv_models import Cv

source_text = """
Léa Morel
Senior AI Engineer
Geneva, Switzerland · lea.morel@example.com · +41 79 000 11 22 · github.com/lmorel-ai
Nationality: Swiss / French · Availability: from January 2027
Languages: French (native), English (C1), German (B1)
PROFILE
AI engineer with 6 years of Python experience, the last 3 focused on production LLM agents. I have built and
operated RAG assistants on self-hosted open-source models in a regulated, high-SLA environment.
PROFESSIONAL EXPERIENCE
Senior AI Engineer — Helvetia Ledger SA (B2B SaaS for private banks)
Lausanne · 2023 – present
• Designed a multi-agent assistant with LangChain and Pydantic-AI used by 4,000 bank employees.
• Built a RAG pipeline on Qdrant with hybrid search and re-ranking (faithfulness 71% -> 89%).
• Deployed Llama 3, Mistral and Qwen with vLLM; cut p95 latency by 42%.
• Set up Langfuse tracing and automated evaluation in GitLab CI.
• Exposed agents via FastAPI on Kubernetes (99.95% SLA), with Prometheus/Grafana and Sentry.
Machine Learning Engineer — DataVaud Sàrl
Lausanne · 2020 – 2023
• Built NLP pipelines with Hugging Face Transformers, served with FastAPI and Docker.
EDUCATION
• MSc Computer Science, EPFL — 2020
• BSc Computer Science, EPFL — 2018
SKILLS
LLM & Agents
LangChain, Pydantic-AI, RAG, Langfuse, Ragas
Model serving
vLLM, TGI, AWQ / GPTQ quantisation
Backend
Python, FastAPI, PostgreSQL, Qdrant, Redis
DevOps
Docker, Kubernetes, GitLab CI, Prometheus, Grafana, Sentry
OPEN SOURCE
• Contributor to Pydantic-AI (3 merged PRs).
• Maintainer of ragbench-lite, a RAG evaluation toolkit.
"""


response = chat(
    model='qwen3.5:2b',
    messages=[
        {
            'role': 'system', 
            'content': 'Extract information from the text into the requested JSON schema.'
        },
        {
            'role': 'user', 
            'content': source_text
        }
              ],
    format=Cv.model_json_schema(),
    options={'temperature': 0}
)
print(response.message.content)
#cv = Cv.model_validate_json(response.message.content)
#print(cv)