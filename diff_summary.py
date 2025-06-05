from __future__ import annotations
import html
import logging
import os
from openai import OpenAI, OpenAIError

_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

_PROMPT = """\
Je bent een behulpzame assistent die wijzigingen in vacature­teksten samenvat.
Vergelijk de oude en nieuwe versie hieronder en geef in MAXIMAAL drie korte bullets
(gebruik het teken •) wat er inhoudelijk is veranderd. Negeer cosmetische
of lay-out-wijzigingen.

--- OUDE VERSIE ---
{old}

--- NIEUWE VERSIE ---
{new}
"""

def summarize_change(old: str, new: str) -> str:
    prompt = _PROMPT.format(old=old[:40000], new=new[:40000])
    try:
        response = _client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=180,
        )
        text = response.choices[0].message.content.strip()
    except OpenAIError as exc:
        logging.warning("LLM-samenvatting mislukte: %s", exc)
        text = "• Samenvatting kon niet worden gegenereerd."
    return html.escape(text)
