import pywikibot
import datetime

site = pywikibot.Site('wikidata', 'wikidata')

month_names = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

archive_root = "Wikidata:Requests for deletions/Archive"

year_template = """
{{Archive subindex|category=Archived requests for deletion|hideredirect=yes}}

== Properties ==
{{Special:Prefixindex/Wikidata:Requests for deletions/Archive/%(year)d/P}}

== Bulk Requests ==
{{Special:Prefixindex/Wikidata:Requests for deletions/Archive/%(year)d/B}}

"""

month_template = """
#REDIRECT [[Wikidata:Requests for deletions/Archive/%(year)d#%(monthname)s]]
"""

def main():
    cur_time = datetime.datetime.utcnow()
    cur_month_num = cur_time.month
    cur_year = cur_time.year
    year_page = pywikibot.Page(site, f"{archive_root}/{cur_year}")
    if not year_page.exists():
        year_page.text = year_template % {'year': cur_year}
        year_page.save("Creating new archive year page ([[User:RPI2026F1Bot/Task6|info]])", botflag=True)
    for month in range(1, cur_month_num + 1):
        month_page = pywikibot.Page(site, f"{archive_root}/{cur_year}/{month:02d}")
        if not month_page.exists():
            month_page.text = month_template % {'year': cur_year, 'monthname': month_names[month]}
            month_page.save("Creating new archive month page ([[User:RPI2026F1Bot/Task6|info]])", botflag=True)

if __name__ == "__main__":
    main()