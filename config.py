from pathlib import Path

CSV_PATH = Path("data/content.csv")

PRACTICES = [
    {
        "name": "De Deventer Tandartspraktijk",
        "url": "https://www.dedeventertandartspraktijk.nl/vacatures",
        "selector": "article#post-131",
        "get_full_html": False
    },
    {
        "name": "Dental Clinics Colmschate",
        "url": "https://www.werkenbijdentalclinics.nl/vacatures/?_locatie=Colmschate",
        "selector": "div.section-element.section-element-vacancies-archive.\@container\/element-vacancies-archive",
        "get_full_html": False
    },
    {
        "name": "De Watersnip",
        "url": "https://dewatersnip.com/vacatures",
        "selector": "div#vacature-overzichtje",
        "get_full_html": False
    },
    {
        "name": "Tandartsen Centrum Deventer",
        "url": "https://www.stcdeventer.nl/vacatures",
        "selector": "div.elementor.elementor-302.post-346",
        "get_full_html": True
    }
    # … add up to 100
]