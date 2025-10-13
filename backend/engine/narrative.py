import os
from openai import OpenAI

SYSTEM_PROMPT = (
    "Você é psicólogo organizacional e coach executivo. Gere um relatório de desenvolvimento em português, com seções: "
    "'Seu Arquétipo', 'Seu Estilo de Atuação', 'Forças e Superpoderes', 'Pontos de Atenção', 'Plano de Desenvolvimento Acionável'. "
    "Linguagem acessível, empática e baseada em evidências. Inclua exemplos observáveis e recomendações concretas."
)

def generate_individual_report(payload: dict) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "[Dev] OPENAI_API_KEY não configurada. Placeholder de relatório."
    client = OpenAI(api_key=api_key)
    user_prompt = f"Dados psicométricos:\n{payload}\nGere o relatório."
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),
        messages=[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":user_prompt}],
        temperature=0.4,
        max_tokens=1200,
    )
    return resp.choices[0].message.content.strip()
