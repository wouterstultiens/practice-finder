from pathlib import Path

CSV_PATH = Path("data/content.csv")

# TODO: ADD https://careers.dentalvacancies.eu/colosseum-dental/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_shifttype=&optionsFacetsDD_customfield1=&optionsFacetsDD_city=&optionsFacetsDD_state=
# TODO: ADD https://www.facebook.com/100067850752335/posts/1003611035243912/?_rdr
# TODO: ADD veluwe tandartsen apeldoorn vacature linkedin
# TODO: ADD https://www.tandartskleinnagelvoort.nl/
# TODO: ADD Apeldoornse Kliniek voor Parodontologie en Implantologie indeed?
# TODO: ADD dentalcareprofessionals
# TODO: ADD KNMT, Indeed, ...
# TODO: ADD https://www.mondhoek.nl/vacatures/ (javascript thingy)

# No vacancy page:
# https://www.tandartsencentrumhattem.nl/
# https://www.bdtandartsen.nl/ons-team/
# https://tandartspraktijk-waterkwartier.nl/
# https://www.tandartsagvandenakker.nl/
# https://mzcrijssen.nl/
# https://www.tandartsvandooren.nl/
# https://doedental.nl/
# https://thehappydentist.tandartsennet.nl/
# https://www.tandartsenpraktijksanderink-daalmans.nl/
# https://tandartspraktijkmark.nl/
# https://www.mondzorgbrummen.nl/
# https://www.laboesjkiri.nl/
# https://telande.nl/
# https://www.kindertandheelkundedeventer.nl/
# https://www.jelsmaruskamptandartsen.nl/
# https://www.tandartsenpraktijkfreriksanema.nl/
# https://www.dvanhouten.nl/home
# https://www.thvtandartsen.nl/
# https://mondzorgvorden.nl/
# http://www.tandartsenpraktijkoverijssel.nl/
# https://www.hagenbeektandartsen.nl/
# https://breukersendegruijter.nl/
# https://tandartspraktijkmarkelo.tandartsennet.nl/
# https://mondzorgcentrumtwello.nl
# https://tandartsdegen.nl/
# https://tandzorgarnhemseweg.nl/
# https://www.tandartsbosma.nl/
# https://www.tandartsenpraktijkzaadmarkt.nl/
# https://www.praktijkbraam.nl/
# https://bto.nu/
# https://smiledent-apeldoorn.nl/

# Closed
# https://www.tandartsugchelen.nl/
# https://tandartsvanheijst.nl/

# Colosseum Dental
# https://www.tandarts-apeldoorn-maten.nl/vacatures/
# https://www.tandartsrijssen.nl/vacatures/
# https://www.tandarts-apeldoorn-parken.nl/vacatures/


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
        "selector": "div.section-element.section-element-vacancies-archive",
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
        "selector": "div.section-element.section-element-vacancies-archive",
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
    {
        "name": "Tandartspraktijk Emanuel",
        "url": "https://tandartsemanuel.nl/vacature.htm",
        "selector": "td[style='border-style: solid; border-width: 0; padding-left: 4; padding-right: 4; padding-top: 1; padding-bottom: 1; margin-top:-2; margin-bottom:-2']",
        "get_full_html": False
    },
    {
        "name": "Tandartsen Groepspraktijk Vrijheid",
        "url": "https://www.vrijheidtandartsen.nl/vacatures/",
        "selector": "div.elementor-302",
        "get_full_html": False
    },
    {
        "name": "Tandheelkunde Polman",
        "url": "https://www.tandheelkundepolman.nl/vacatures",
        "selector": "div.content.col-sm-8.col-sm-offset-1",
        "get_full_html": False
    },
    {
        "name": "Topclass Mondzorg",
        "url": "https://topclassmondzorg.nl/over-ons/careers/",
        "selector": "section.bt_bb_section.bt_bb_layout_boxed_1200.bt_bb_top_spacing_small.bt_bb_bottom_spacing_normal",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk M.J.T. Kooij",
        "url": "https://www.tandartskooij.nl/vacatures-2/",
        "selector": "div.contentMain",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk R.C.L. Raalte",
        "url": "https://www.tandartspraktijkrclraalte.nl/vacatures",
        "selector": "main#PAGES_CONTAINER",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Laren",
        "url": "https://tandartsenpraktijklaren.nl/vacatures/",
        "selector": "div#main",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Kamphuis",
        "url": "https://www.tandartskamphuis.nl/vacatures/",
        "selector": "div.mainContent",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Loenenseweg",
        "url": "https://www.tandartsenpraktijkloenenseweg.nl/vacatures/",
        "selector": "div#main",
        "get_full_html": False
    },
    {
        "name": "Hartman & Mulder Tandartsen",
        "url": "https://www.hmtandartsen.nl/vacatures",
        "selector": "article#post-864",
        "selector": "article#post-864",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Emami",
        "url": "https://dr-emami.nl/vacatures/",
        "selector": "div.et_pb_column.et_pb_column_4_4.et_pb_column_1.et_pb_css_mix_blend_mode_passthrough.et-last-child",
        "get_full_html": False
    },
    {
        "name": "Dental Clinics Hengelo",
        "url": "https://www.werkenbijdentalclinics.nl/vacatures/?_locatie=Hengelo",
        "selector": "div.section-element.section-element-vacancies-archive",
        "get_full_html": False
    },
    {
        "name": "Dental Clinics Enschede",
        "url": "https://www.werkenbijdentalclinics.nl/vacatures/?_locatie=Enschede",
        "selector": "div.section-element.section-element-vacancies-archive",
        "get_full_html": False
    },
    {
        "name": "Mondzorg van As",
        "url": "https://www.mondzorgvanas.nl/vacatures/",
        "selector": "div.elementor-element-d60545f",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Wilhelminaweg",
        "url": "https://tandartsenpraktijkwilhelminaweg.nl/vacatures/",
        "selector": "div#main",
        "get_full_html": False
    },
    {
        "name": "Beekpark Tandartsen",
        "url": "https://www.beekparktandartsen.nl/over-ons/vacatures/",
        "selector": "div.post-404",
        "get_full_html": False
    },
#     { TODO: vacancies in javascript
#         "name": "Vogellanden Centrum Bijzondere Tandheelkunde",
#         "url": "https://www.werkenbijvogellanden.nl/vacatures",
#         "selector": "div#P_C_W_ZoneLayout",
#         "get_full_html": False
#     },
    {
        "name": "Breuklander Mondzorg",
        "url": "https://www.breuklander.nl/vacatures-stage-breuklander-mondzorg-putten/",
        "selector": "div.content",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk de Tandhoek",
        "url": "https://www.detandhoek.nl/?page_id=29",
        "selector": "div.lijeva_rubrika_wide",
        "get_full_html": False
    },
    # { # TODO: weird (javascript?)
    #     "name": "Tandarts Today",
    #     "url": "https://tandartstoday.nl/vacatures/",
    #     "selector": "div.wpb-content-wrapper > div.vc_row.wpb_row.vc_row-fluid",
    #     "get_full_html": False
    # },
    {
        "name": "Tandartspraktijk A. Todea",
        "url": "https://www.tandartstodea.nl/vacatures/",
        "selector": "div.elementor-element-14d056b",
        "get_full_html": False
    },
    {
        "name": "Parodontologie Epe",
        "url": "https://www.parodontologieepe.nl/werken-bij/",
        "selector": "div#content",
        "get_full_html": False
    },
    {
        "name": "Vaadent Tandartsenpraktijk",
        "url": "https://www.vaadent.nl/vacatures/",
        "selector": "div.contentMain",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Loenen",
        "url": "https://www.tploenen.nl/werken-bij/",
        "selector": "div.elementor-column.elementor-col-50.elementor-top-column.elementor-element.elementor-element-432b620",
        "get_full_html": False
    },
    {
        "name": "Veenstra Tandartspraktijk & Implantologie",
        "url": "https://www.tandartspraktijkveenstra.nl/vacatures/",
        "selector": "div.elementor-302",
        "get_full_html": False
    },
    {
        "name": "MP3 Tandartsen",
        "url": "https://mp3tandartsen.nl/tandarts-apeldoorn-en-kliniek-uit-apeldoorn/vacatures/",
        "selector": "article#post-274",
        "get_full_html": False
    },
    {
        "name": "Tandzorg Twello",
        "url": "https://www.tandzorgtwello.nl/vacatures/",
        "selector": "div.elementor-element-d60545f",
        "get_full_html": False
    },
    {
        "name": "Salland Dental",
        "url": "https://www.salland.dental/vacature/",
        "selector": "div.elementor-element-12ebcec",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Diepenveen",
        "url": "https://www.tandartspraktijkdiepenveen.nl/vacatures/",
        "selector": "article#post-137",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Vorden",
        "url": "https://tandartsenpraktijkvorden.nl/vacatures/",
        "selector": "div#main",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk H. Koning",
        "url": "https://www.tandartskoning.nl/vacatures/",
        "selector": "div.elementor-location-single.post-346",
        "get_full_html": False
    },
    {
        "name": "Dental Clinics Nijverdal",
        "url": "https://www.werkenbijdentalclinics.nl/vacatures/?_locatie=Nijverdal",
        "selector": "div.section-element.section-element-vacancies-archive",
        "get_full_html": False
    },
    {
        "name": "Jack & Wijnberg Mondzorg Ulft",
        "url": "https://www.jackwijnberg.nl/vacature/",
        "selector": "div#main-content",
        "get_full_html": False
    },
    {
        "name": "Heeldemond Tandartsen",
        "url": "https://www.heeldemond.nl/vacatures/",
        "selector": "div.main_color.container_wrap_first.container_wrap.fullsize",
        "get_full_html": False
    },
    {
        "name": "Het Praktijkhuis",
        "url": "https://www.hetpraktijkhuis.nl/vacatures/",
        "selector": "div.post-346",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Bathmen",
        "url": "https://www.tandartspraktijkbathmen.nl/vacatures",
        "selector": "div.main",
        "get_full_html": False
    },
    {
        "name": "Mondzorgcentrum Nijverdal",
        "url": "https://www.mondzorgcentrumnijverdal.nl/vacatures/",
        "selector": "div.elementor-element-2a85a09",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk de Schutse",
        "url": "https://www.tandartspraktijkdeschutse.nl/vacatures/",
        "selector": "main#main",
        "get_full_html": False
    },
    {
        "name": "Mondzorg Steenderen",
        "url": "https://www.mondzorgsteenderen.nl/vacatures",
        "selector": "div.col-md-9",
        "get_full_html": False
    },
    {
        "name": "Colosseum Dental Apeldoorn",
        "url": "https://careers.dentalvacancies.eu/colosseum-dental/search/?optionsFacetsDD_city=Apeldoorn",
        "selector": "div#content",
        "get_full_html": False
    },
    {
        "name": "Colosseum Dental Arnhem",
        "url": "https://careers.dentalvacancies.eu/colosseum-dental/search/?optionsFacetsDD_city=Arnhem",
        "selector": "div#content",
        "get_full_html": False
    },
    {
        "name": "Colosseum Dental Dalfsen",
        "url": "https://careers.dentalvacancies.eu/colosseum-dental/search/?optionsFacetsDD_city=Dalfsen",
        "selector": "div#content",
        "get_full_html": False
    },
    {
        "name": "Colosseum Dental Rijssen",
        "url": "https://careers.dentalvacancies.eu/colosseum-dental/search/?optionsFacetsDD_city=Rijssen",
        "selector": "div#content",
        "get_full_html": False
    },
    {
        "name": "Colosseum Dental Zwolle",
        "url": "https://careers.dentalvacancies.eu/colosseum-dental/search/?optionsFacetsDD_city=Zwolle",
        "selector": "div#content",
        "get_full_html": False
    },
]