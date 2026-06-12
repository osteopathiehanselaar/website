#!/usr/bin/env python3
"""Static site assembler: combines layout.html + per-page content fragments
into final HTML files for NL (root) and EN (/en/)."""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BUILD_DIR, "content")
LAYOUT_PATH = os.path.join(BUILD_DIR, "layout.html")

# key -> {nl: {...}, en: {...}}
PAGES = [
    {
        "key": "home",
        "nl": {"slug": "index.html", "title": "Osteopathie Hanselaar | Osteopaat in Bemelen", "desc": "Osteopathie Hanselaar in Bemelen helpt je lichaam herstellen en in balans komen. Persoonlijke, rustige zorg voor jong en oud.", "nav": "Home"},
        "en": {"slug": "index.html", "title": "Osteopathie Hanselaar | Osteopath in Bemelen", "desc": "Osteopathie Hanselaar in Bemelen helps your body recover and find balance. Personal, calm care for all ages.", "nav": "Home"},
    },
    {
        "key": "treatments",
        "nl": {"slug": "behandelingen.html", "title": "Behandelingen | Osteopathie Hanselaar", "desc": "Ontdek onze osteopathische behandelingen: van rug- en nekklachten tot baby's, sport en zwangerschap.", "nav": "Behandelingen"},
        "en": {"slug": "treatments.html", "title": "Treatments | Osteopathie Hanselaar", "desc": "Discover our osteopathic treatments: from back and neck complaints to babies, sports and pregnancy.", "nav": "Treatments"},
    },
    {
        "key": "about",
        "nl": {"slug": "over-ons.html", "title": "Over ons | Osteopathie Hanselaar", "desc": "Maak kennis met het team van Osteopathie Hanselaar en onze kijk op gezondheid en beweging.", "nav": "Over ons"},
        "en": {"slug": "about.html", "title": "About us | Osteopathie Hanselaar", "desc": "Meet the team at Osteopathie Hanselaar and our approach to health and movement.", "nav": "About"},
    },
    {
        "key": "rates",
        "nl": {"slug": "tarieven.html", "title": "Tarieven & vergoeding | Osteopathie Hanselaar", "desc": "Bekijk onze tarieven en de vergoeding van osteopathie via je zorgverzekering.", "nav": "Tarieven"},
        "en": {"slug": "rates.html", "title": "Rates & insurance | Osteopathie Hanselaar", "desc": "View our rates and how osteopathy is reimbursed through your health insurance.", "nav": "Rates"},
    },
    {
        "key": "appointment",
        "nl": {"slug": "afspraak.html", "title": "Afspraak maken | Osteopathie Hanselaar", "desc": "Plan eenvoudig online je afspraak bij Osteopathie Hanselaar in Bemelen.", "nav": "Afspraak maken"},
        "en": {"slug": "appointment.html", "title": "Book an appointment | Osteopathie Hanselaar", "desc": "Easily book your appointment online at Osteopathie Hanselaar in Bemelen.", "nav": "Book appointment"},
    },
    {
        "key": "contact",
        "nl": {"slug": "contact.html", "title": "Contact | Osteopathie Hanselaar", "desc": "Vragen of contact opnemen met Osteopathie Hanselaar in Bemelen? Hier vind je al onze gegevens.", "nav": "Contact"},
        "en": {"slug": "contact.html", "title": "Contact | Osteopathie Hanselaar", "desc": "Questions or want to contact Osteopathie Hanselaar in Bemelen? Find all our details here.", "nav": "Contact"},
    },
    {
        "key": "privacy",
        "nl": {"slug": "privacybeleid.html", "title": "Privacybeleid | Osteopathie Hanselaar", "desc": "Lees hoe Osteopathie Hanselaar omgaat met je persoonsgegevens.", "nav": None},
        "en": {"slug": "privacy.html", "title": "Privacy policy | Osteopathie Hanselaar", "desc": "Read how Osteopathie Hanselaar handles your personal data.", "nav": None},
    },
    {
        "key": "terms",
        "nl": {"slug": "voorwaarden.html", "title": "Algemene voorwaarden | Osteopathie Hanselaar", "desc": "De algemene voorwaarden en het annuleringsbeleid van Osteopathie Hanselaar.", "nav": None},
        "en": {"slug": "terms.html", "title": "Terms & conditions | Osteopathie Hanselaar", "desc": "The terms, conditions and cancellation policy of Osteopathie Hanselaar.", "nav": None},
    },
]

NAV_KEYS = ["home", "treatments", "about", "rates", "appointment", "contact"]

STRINGS = {
    "nl": {
        "skip_link": "Direct naar inhoud",
        "nav_label": "Hoofdnavigatie",
        "nav_cta": "Maak een afspraak",
        "menu_label": "Menu openen",
        "lang_switch_label": "EN",
        "footer_tagline": "Persoonlijke osteopathische zorg in Bemelen — voor herstel, balans en meer bewegingsvrijheid in je dagelijks leven.",
        "footer_nav_title": "Navigatie",
        "footer_contact_title": "Contact & openingstijden",
        "rights": "Alle rechten voorbehouden.",
        "privacy_label": "Privacybeleid",
        "terms_label": "Algemene voorwaarden",
        "booking_href": "afspraak.html",
        "home_href": "index.html",
    },
    "en": {
        "skip_link": "Skip to content",
        "nav_label": "Main navigation",
        "nav_cta": "Book an appointment",
        "menu_label": "Open menu",
        "lang_switch_label": "NL",
        "footer_tagline": "Personal osteopathic care in Bemelen — for recovery, balance and more freedom of movement in everyday life.",
        "footer_nav_title": "Navigation",
        "footer_contact_title": "Contact & opening hours",
        "rights": "All rights reserved.",
        "privacy_label": "Privacy policy",
        "terms_label": "Terms & conditions",
        "booking_href": "appointment.html",
        "home_href": "index.html",
    },
}


def page_by_key(key):
    return next(p for p in PAGES if p["key"] == key)


def build_nav(lang, current_key, root, mobile=False):
    items = []
    for key in NAV_KEYS:
        page = page_by_key(key)
        info = page[lang]
        href = root + (info["slug"] if lang == "nl" else f"en/{info['slug']}")
        active = " is-active" if key == current_key else ""
        if mobile:
            items.append(
                f'        <a href="{href}" class="nav-link{active} rounded-xl px-3 py-3 text-base hover:bg-sage-50">{info["nav"]}</a>'
            )
        else:
            items.append(f'        <a href="{href}" class="nav-link{active}">{info["nav"]}</a>')
    return "\n".join(items)


def build_footer_nav(lang, root):
    items = []
    for key in NAV_KEYS:
        page = page_by_key(key)
        info = page[lang]
        href = root + (info["slug"] if lang == "nl" else f"en/{info['slug']}")
        items.append(f'            <li><a href="{href}" class="transition-colors hover:text-clay-300">{info["nav"]}</a></li>')
    return "\n".join(items)


def render_page(layout, page, lang):
    info = page[lang]
    s = STRINGS[lang]
    root = "" if lang == "nl" else "../"

    content_path = os.path.join(CONTENT_DIR, lang, f"{page['key']}.html")
    with open(content_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("{{ROOT}}", root)

    privacy = page_by_key("privacy")[lang]
    terms = page_by_key("terms")[lang]
    privacy_href = root + (privacy["slug"] if lang == "nl" else f"en/{privacy['slug']}")
    terms_href = root + (terms["slug"] if lang == "nl" else f"en/{terms['slug']}")

    if lang == "nl":
        lang_switch_href = "en/" + page["en"]["slug"]
    else:
        lang_switch_href = "../" + page["nl"]["slug"]

    home_href = s["home_href"]

    replacements = {
        "{{LANG}}": lang,
        "{{TITLE}}": info["title"],
        "{{DESC}}": info["desc"],
        "{{ROOT}}": root,
        "{{HOME_HREF}}": home_href,
        "{{NAV_LABEL}}": s["nav_label"],
        "{{NAV_ITEMS}}": build_nav(lang, page["key"], root, mobile=False),
        "{{NAV_ITEMS_MOBILE}}": build_nav(lang, page["key"], root, mobile=True),
        "{{LANG_SWITCH_HREF}}": lang_switch_href,
        "{{LANG_SWITCH_LABEL}}": s["lang_switch_label"],
        "{{BOOKING_HREF}}": s["booking_href"],
        "{{NAV_CTA}}": s["nav_cta"],
        "{{MENU_LABEL}}": s["menu_label"],
        "{{SKIP_LINK}}": s["skip_link"],
        "{{CONTENT}}": content,
        "{{FOOTER_TAGLINE}}": s["footer_tagline"],
        "{{FOOTER_NAV_TITLE}}": s["footer_nav_title"],
        "{{FOOTER_NAV_ITEMS}}": build_footer_nav(lang, root),
        "{{FOOTER_CONTACT_TITLE}}": s["footer_contact_title"],
        "{{RIGHTS}}": s["rights"],
        "{{PRIVACY_HREF}}": privacy_href,
        "{{PRIVACY_LABEL}}": s["privacy_label"],
        "{{TERMS_HREF}}": terms_href,
        "{{TERMS_LABEL}}": s["terms_label"],
    }

    html = layout
    for key, value in replacements.items():
        html = html.replace(key, value)
    return html


def main():
    with open(LAYOUT_PATH, "r", encoding="utf-8") as f:
        layout = f.read()

    for page in PAGES:
        for lang in ("nl", "en"):
            html = render_page(layout, page, lang)
            if lang == "nl":
                out_path = os.path.join(ROOT_DIR, page["nl"]["slug"])
            else:
                out_path = os.path.join(ROOT_DIR, "en", page["en"]["slug"])
            os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"wrote {os.path.relpath(out_path, ROOT_DIR)}")


if __name__ == "__main__":
    main()
