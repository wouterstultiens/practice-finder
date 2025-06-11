import html
import logging
import os

from openai import AsyncOpenAI, OpenAIError

# --- OpenAI Configuration ---
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    logging.warning("OPENAI_API_KEY not set. LLM functionality will be disabled.")
    client = None
else:
    client = AsyncOpenAI(api_key=API_KEY)

# This prompt is optimized for summarizing job vacancy changes concisely in Dutch.
PROMPT_TEMPLATE = """
Je bent een behulpzame assistent die wijzigingen in vacatureteksten samenvat voor een monitoringssysteem.
Jouw taak is om de OUDE en NIEUWE versie van een webpaginafragment te vergelijken en de belangrijkste inhoudelijke verschillen te identificeren.

- Focus op toegevoegde, verwijderde of gewijzigde vacatures.
- Geef een samenvatting in **maximaal 3 korte, duidelijke bullet points** (gebruik •).
- Rapporteer alleen **inhoudelijke** wijzigingen. Negeer kleine tekstuele aanpassingen, datumwijzigingen, of layoutveranderingen.
- Als er geen duidelijke wijziging is, zeg dan: "Er is geen inhoudelijke wijziging gevonden."
- Als een van de versies leeg is, meld dit dan (bijv. "Nieuwe vacature(s) toegevoegd." of "Alle vacatures zijn verwijderd.").
- Je antwoord moet direct beginnen met een bullet point, zonder inleidende tekst.

--- OUDE VERSIE ---
{old}

--- NIEUWE VERSIE ---
{new}
"""

# Limit content size to avoid excessive token usage
MAX_CONTENT_LENGTH = 300000

async def summarize_change(old_content: str, new_content: str) -> str:
    """
    Generates a summary of the difference between old and new content using an LLM.

    Args:
        old_content: The previous version of the content.
        new_content: The new version of the content.

    Returns:
        A human-readable, HTML-escaped summary of the changes.
    """
    if not client:
        return "• LLM-samenvatting is uitgeschakeld (API-sleutel ontbreekt)."

    prompt = PROMPT_TEMPLATE.format(
        old=old_content[:MAX_CONTENT_LENGTH],
        new=new_content[:MAX_CONTENT_LENGTH]
    )

    try:
        response = await client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,  # Low temperature for deterministic, factual summaries
            max_tokens=200,
            timeout=30,
        )
        summary = response.choices[0].message.content or "• Geen samenvatting ontvangen van LLM."
    except OpenAIError as e:
        logging.warning(f"LLM summary generation failed: {e}")
        summary = "• Samenvatting kon niet worden gegenereerd door een technische fout."

    return html.escape(summary.strip())