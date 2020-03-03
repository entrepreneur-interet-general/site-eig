import unittest

import yaml


class BaseTest(unittest.TestCase):
    def setUp(self):
        with open("_data/defis.yml") as f:
            self.defis = yaml.safe_load(f)

        with open("_data/personnes.yml") as f:
            self.personnes = yaml.safe_load(f)

        with open("_data/promos.yml") as f:
            self.promos = yaml.safe_load(f)

    def clean_md_filename(self, filename, prefix):
        file_no_prefix = filename.replace(f"_{prefix}/", "")
        year = file_no_prefix.split("-")[0]
        slug = "-".join(file_no_prefix.split("-")[3:]).replace(".md", "")
        return f"/{prefix}/{year}/{slug}.html"
