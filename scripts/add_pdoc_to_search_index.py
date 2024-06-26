#!/usr/bin/env python3
# Context: search_index.json is a file used by lunr.js & mkdocs-material builtin search plugin
# ( https://squidfunk.github.io/mkdocs-material/plugins/search/ )
# in order to provide the search feature in our public documentation website.
# This script adds entries to search_index.json for every <dt>/<dd> entry
# in the HTML files generated by pdoc, in order for them to be indexed by lunr.js
import json
from pathlib import Path

from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).parent.parent
SEARCH_INDEX_FILEPATH = REPO_ROOT / "public/search/search_index.json"
PDOC_DIRPATH = REPO_ROOT / "public/fpdf/"


def main():
    with SEARCH_INDEX_FILEPATH.open() as search_index_file:
        search_index = json.load(search_index_file)
    docs = search_index["docs"]
    initial_docs_count = len(docs)
    for html_filepath in PDOC_DIRPATH.glob("*.html"):
        docs.extend(extract_docs(html_filepath))
    with SEARCH_INDEX_FILEPATH.open("w") as search_index_file:
        json.dump(search_index, search_index_file)
    print(
        f"{len(docs) - initial_docs_count} entries successfully added to {SEARCH_INDEX_FILEPATH.name} for pdoc API pages"
    )


def extract_docs(html_filepath):
    soup = BeautifulSoup(html_filepath.read_text(), features="lxml")
    page_title = soup.find("title").get_text().strip()
    for dt in soup.find_all("dt"):
        dt_id = dt.get("id")
        if dt_id:
            dt_label = dt.get_text().strip().split("\n")[0]
            dd = dt.next_sibling.next_sibling
            assert dd.name == "dd"
            yield {
                "location": f"fpdf/{html_filepath.name}#{dt_id}",
                "title": f"{page_title} - {dt_label}",
                "text": str(dd),
            }


if __name__ == "__main__":
    main()
