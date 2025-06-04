from pathlib import Path

CSV_PATH = Path("data/content.csv")

# TODO: ADD https://careers.dentalvacancies.eu/colosseum-dental/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_shifttype=&optionsFacetsDD_customfield1=&optionsFacetsDD_city=&optionsFacetsDD_state=
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
    },
    {
        "name": "Tandartsen Hoge Hond",
        "url": "https://tandartsenhogehond.nl/vacatures",
        "selector": "div#main",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk de Leeuwenbrug",
        "url": "https://deleeuwenbrug.tandartsennet.nl/vacature",
        "selector": "div.contentMain",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Harskamp",
        "url": "https://harskamp.tandartsennet.nl/vacature",
        "selector": "div.mainContent",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Slot",
        "url": "https://mondengezondheid.nl/vacature",
        "selector": "div.l-content",
        "get_full_html": False
    },
    # { TODO: NEEDS JAVASCRIPT TO RUN VACANCY BOX
    #     "name": "Tandartsenpraktijk de Gelder",
    #     "url": "https://www.tandartspraktijkdegelder.nl/vacatures",
    #     "selector": "body",
    #     "get_full_html": False
    # }
    {
        "name": "Tandartspraktijk Overbeek",
        "url": "https://tandartspraktijkoverbeek.tandartsennet.nl/vacatures",
        "selector": "div.mainContent",
        "get_full_html": False
    },
    {
        "name": "Weijler & Weijler Mondzorg Gorssel",
        "url": "https://www.weijler.nl/vacatures",
        "selector": "body",
        "get_full_html": False
    },
    {
        "name": "Sanadens",
        "url": "https://www.sanadens.nl/nl/wie-zijn-wij/",
        "selector": "section.content.clear > div.col-2.last",
        "get_full_html": False
    },
    # { # TODO
    #     "name": "Tandheelkundig Centrum Eerbeek",
    #     "url": "https://www.sanadens.nl/nl/wie-zijn-wij/",
    #     "selector": "section.content.clear > div.col-2.last",
    #     "get_full_html": False
    # },
    {
        "name": "Tandartsenpraktijk Epe",
        "url": "https://www.tandartsenpraktijkepe.nl/vacatures/",
        "selector": "body",
        "get_full_html": False
    },
    {
        "name": "Dental Clinics Apeldoorn",
        "url": "https://www.werkenbijdentalclinics.nl/vacatures/?_locatie=Apeldoorn",
        "selector": "div.section-element.section-element-vacancies-archive.\@container\/element-vacancies-archive",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk de Hanze",
        "url": "https://www.dehanze.nl/vacature/",
        "selector": "div#content",
        "get_full_html": False
    },
    {
        "name": "De Overwelving Tandartsen",
        "url": "https://www.deoverwelving.nl/vacatures/",
        "selector": "div.mainContent__text",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Zuidbroek",
        "url": "https://tandartszuidbroek.nl/vacatures/",
        "selector": "div#Content",
        "get_full_html": False
    },
    # { TODO
    #     "name": "Tandartsen Noordereiland",
    #     "url": "https://gaevdental.recruitee.com/",
    #     "selector": "div#Content",
    #     "get_full_html": False
    # },
    {
        "name": "IJsselstate Tandartsen",
        "url": "https://www.ijsselstate.nl/vacatures/",
        "selector": "div.elementor-element-76250f1",
        "get_full_html": False
    },
    {
        "name": "Centrum voor Tandheelkunde Beekbergen",
        "url": "https://www.ctbeekbergen.nl/vacature/",
        "selector": "div.container.page > div.row",
        "get_full_html": False
    },
    # { # TODO: vacancy in blog posts?
    #     "name": "Tandartspraktijk de Wayenburg",
    #     "url": "https://www.tandartspraktijkvanwayenburg.nl/",
    #     "selector": "div.container.page > div.row",
    #     "get_full_html": False
    # },
    {
        "name": "Tandartspraktijk de Tandarts",
        "url": "https://www.detandartsheerde.nl/vacatures/",
        "selector": "main#main",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Fabels",
        "url": "https://www.tandartspraktijkfabels.nl/vacatures/",
        "selector": "div.elementor-element-ea8dc42",
        "get_full_html": False
    },
    # { TODO: NEEDS JAVASCRIPT TO RUN VACANCY BOX
    #     "name": "Centrum Mondzorg Epe",
    #     "url": "https://www.tandartsepe.nl/vacatures/",
    #     "selector": "div.elementor-302",
    #     "get_full_html": False
    # },
    {
        "name": "Tandartspraktijk Fabels",
        "url": "https://www.tandartspraktijkfabels.nl/vacatures/",
        "selector": "div.elementor-element-ea8dc42",
        "get_full_html": False
    },
    {
        "name": "Tandheelkunde Hattem",
        "url": "https://www.tandheelkundehattem.nl/vacatures/",
        "selector": "section.elementor-element-e0e7409",
        "get_full_html": False
    },
    {
        "name": "Tandpark",
        "url": "https://www.tandpark.nl/werken-bij/",
        "selector": "div.wf-container-main",
        "get_full_html": False
    },
    {
        "name": "Tandheelkundig Centrum Arnhem Noord",
        "url": "https://www.tcan.nl/vacatures-overzicht/",
        "selector": "div.wpb-content-wrapper",
        "get_full_html": False
    },
    {
        "name": "Mondzorg Kuijl & Den Ambtman",
        "url": "https://mondzorgkuijl.nl/vacatures",
        "selector": "div.container.single-container.single-page",
        "get_full_html": False
    },
    {
        "name": "Tandheelkundig Centrum Holten",
        "url": "https://tandartsenholten.tandartsennet.nl/vacatures/",
        "selector": "main#main",
        "get_full_html": False
    },
]