from pathlib import Path

CSV_PATH = Path("data/content.csv")

# TODO: ADD https://www.facebook.com/100067850752335/posts/1003611035243912/?_rdr
# TODO: ADD veluwe tandartsen apeldoorn vacature linkedin
# TODO: ADD https://www.tandartskleinnagelvoort.nl/
# TODO: ADD Apeldoornse Kliniek voor Parodontologie en Implantologie indeed?
# TODO: ADD Indeed, ...
# TODO: ADD https://www.mondhoek.nl/vacatures/ (javascript thingy)
# TODO: ADD alle grote plaatsen nog een keer langsgaan, die hebben >10 praktijken waarschijnlijk (Apeldoorn vooral)
# TODO: ADD https://gaevdental.recruitee.com/
# TODO: ADD https://vacatures.tandartspraktijk.nl/
# TODO: ADD https://delievetandarts.nl/
# TODO: ADD tandarts putten FB (and other via FB)

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
# https://tandartspraktijkexcellentia.tandartsennet.nl/
# https://www.tandartspraktijkvandewerken.nl/
# https://www.tandartsdenotter.nl/
# https://tandartspraktijkholtenbroek.tandartsennet.nl/
# https://adtandartsen.tandartsennet.nl/
# https://www.tandartspraktijkstadshagen.nl/
# https://tandartspraktijkrosendaal.nl/
# https://www.tandartsenpraktijkforelkolk.nl/
# http://tandartspraktijkevers.nl/
# http://www.tandartstongeren.be/
# https://www.alldentalcosmetics.nl/
# https://www.dentalzorgapeldoorn.nl/
# https://www.tandartswijhe.nl/
# https://www.mondzorgkliniekolst.nl/
# https://www.jungletandartsen.nl
# https://tandartspraktijkapeldoornzuid.nl/
# https://mondzorgexcellent.nl/
# https://www.mondzorgloenen.nl/
# https://mondzorgwekerom.nl/
# https://otterlo.tandartsennet.nl/
# https://spto.nl/
# https://tandartspraktijk-manokian.tandartsennet.nl/
# https://www.tandartsenpraktijksanderink-daalmans.nl/
# https://tandartsenpraktijkstjozef.nl/
# https://tandartsheeten.nl/
# https://www.tandartsholten.nl/
# https://www.tandartskleinnagelvoort.nl/
# https://www.tandartspraktijkschalkhaar.nl/
# https://www.tandartsvanegdom.nl/
# https://tandenrijkzutphenzuid.nl/

# Closed
# https://www.tandartsugchelen.nl/
# https://tandartsvanheijst.nl/


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
    {
        "name": "KNMT Overijssel",
        "url": "https://knmt.nl/vacatures?vacatures%5B0%5D=work_area%3AOverijssel",
        "selector": "div.views-infinite-scroll-content-wrapper.clearfix",
        "get_full_html": False
    },
    {
        "name": "KNMT Gelderland",
        "url": "https://knmt.nl/vacatures?vacatures%5B0%5D=work_area%3AGelderland",
        "selector": "div.views-infinite-scroll-content-wrapper.clearfix",
        "get_full_html": False
    },
    {
        "name": "Boersma & Boersma",
        "url": "https://boersma-tandheelkunde.nl/vacatures/",
        "selector": "main#main",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk La Roi",
        "url": "https://www.tandartslaroi.nl/werken-bij/",
        "selector": "main.wrapper-main",
        "get_full_html": False
    },
    {
        "name": "Mondzorg Centrum Overtoom",
        "url": "https://www.mondzorgcentrumovertoom.nl/vacatures/",
        "selector": "div.wpb_column.vc_column_container.vc_col-sm-8",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Over De Brug",
        "url": "https://www.tandartsoverdebrug.nl/",
        "selector": "div.row_col_wrap_12.col.span_12.dark.left > div.vc_col-sm-6.wpb_column.column_container.vc_column_container.col.padding-10-percent.inherit_tablet.inherit_phone ",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Postema",
        "url": "https://tandartsenpraktijkpostema.nl/over-ons/vacatures/",
        "selector": "div.site-main",
        "get_full_html": False
    },
    {
        "name": "Albers & Borgeld Tandartsen",
        "url": "https://www.albersenborgeldtandartsen.nl/vacatures/",
        "selector": "article#post-772",
        "get_full_html": False
    },
    {
        "name": "Breuklander Mondzorg",
        "url": "https://www.breuklander.nl/vacatures/",
        "selector": "div.content",
        "get_full_html": False
    },
    {
        "name": "Mondzorg Rhienderen",
        "url": "https://www.mondzorgrhienderen.nl/vacatures/",
        "selector": "section.elementor-element-3c12f82",
        "get_full_html": False
    },
    {
        "name": "De Nieuwe Mondzorg",
        "url": "https://denieuwemondzorg.nl/vacature/",
        "selector": "div.elementor.elementor-162",
        "get_full_html": False
    },
    {
        "name": "Dental365",
        "url": "https://dental365.nl/vacatures/",
        "selector": "article#post-9236",
        "get_full_html": False
    },
    {
        "name": "Mondzorg Dalfsen",
        "url": "https://mondzorgdalfsen.nl/vacatures.html",
        "selector": "div#Section1",
        "get_full_html": False
    },
    {
        "name": "Mondzorgpraktijk Garderen",
        "url": "https://www.mondzorgpraktijkgarderen.nl/praktijkinformatie/vacatures-en-stage",
        "selector": "div.container.container-white.container-overlying.container-shadow",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Alberga",
        "url": "https://www.tandarts-zutphen.nl/vacature/",
        "selector": "div#main",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Elspeet",
        "url": "https://www.tandartselspeet.nl/vacatures/",
        "selector": "div.elementor.elementor-346",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Apeldoornseweg",
        "url": "https://www.tandartsenapeldoornseweg.nl/vacatures/",
        "selector": "div.mainContent",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Het Centrum",
        "url": "https://tandartsenpraktijkhetcentrum.nl/",
        "selector": "div#team",
        "get_full_html": False
    },
    {
        "name": "Tandarts Lochem",
        "url": "https://www.tandartslochem.nl/vacatures/",
        "selector": "div.elementor-element-14d056b",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk Nelis",
        "url": "https://tandartspraktijknelis.nl/vacatures/",
        "selector": "div#fl-main-content",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Pronk",
        "url": "https://www.tandartspronk.nl/vacatures/",
        "selector": "div.elementor-302",
        "get_full_html": False
    },
    {
        "name": "Tandartsenpraktijk Vermeulen",
        "url": "https://tandartsvermeulen.nl/over-ons/vacatures/",
        "selector": "div#contentwrapper",
        "get_full_html": False
    },
    {
        "name": "Tandartspraktijk in de Vijfhoek",
        "url": "https://www.trotsopjetanden.nl/vacatures/",
        "selector": "div.contentMain",
        "get_full_html": False
    },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # },
    # {
    #     "name": "",
    #     "url": "",
    #     "selector": "",
    #     "get_full_html": False
    # }
]