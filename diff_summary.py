# diff_summary.py
"""
Genereert een beknopte, Nederlandstalige samenvatting van de verschillen
tussen twee HTML-snippets (oude vs. nieuwe vacaturepagina).
Compatibel met openai-python >= 1.0.
"""

from __future__ import annotations

import html
import logging
import os

from openai import OpenAI, OpenAIError

# Eén client object hergebruiken (thread-safe)
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
    """
    Roept GPT-4.1 aan en geeft een HTML-geëscapeerde samenvatting terug
    die direct in een Telegram-bericht kan worden gezet.
    """
    prompt = _PROMPT.format(old=old[:4000], new=new[:4000])  # token-veilig trunceren
    try:
        response = _client.chat.completions.create(          # nieuwe 1.x syntaxis
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=180,
        )
        text = response.choices[0].message.content.strip()
    except OpenAIError as exc:
        logging.warning("LLM-samenvatting mislukte: %s", exc)
        text = "• Samenvatting kon niet worden gegenereerd."

    # Telegram gebruikt HTML-parse-mode → escapen
    return html.escape(text)
