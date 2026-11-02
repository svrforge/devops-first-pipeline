"""Validate browser asset wiring and navigation hooks without pretending to run a browser."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.assets = []
        self.lang = None

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'script' and 'src' in attrs:
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.assets.append(attrs['href'])


class AcademyTests(unittest.TestCase):
    def test_local_assets_and_unique_controls(self):
        page = Document()
        page.feed(Path('academy/index.html').read_text())
        self.assertEqual(page.lang, 'en')
        self.assertEqual(len(page.ids), len(set(page.ids)))
        for asset in page.assets:
            self.assertTrue((Path('academy') / asset).is_file(), asset)
            self.assertNotIn('://', asset)
        source = Path('academy/app.js').read_text()
        for identifier in re.findall(r"\$\('([^']+)'\)", source):
            self.assertIn(identifier, page.ids)
        self.assertIn('prefers-reduced-motion', source)
        self.assertIn('role="tablist"', Path('academy/index.html').read_text())
