# -*- coding: utf-8 -*-
import unittest
import difflib
import glob
from collections import defaultdict

import yaml
import frontmatter


class TestMain(unittest.TestCase):
    def setUp(self):
        with open("_data/defis.yml") as f:
            self.defis = yaml.safe_load(f)

        with open("_data/personnes.yml") as f:
            self.personnes = yaml.safe_load(f)

    def personnes_par_defi(self):
        res = defaultdict(list)
        for personne, content in self.personnes.items():
            if "defis" in content:
                for defi in content["defis"]:
                    res[defi].append(personne)
        return res

    def clean_filename(self, filename, prefix):
        file_no_prefix = filename.replace(f"_{prefix}/", "")
        year = file_no_prefix.split("-")[0]
        slug = "-".join(file_no_prefix.split("-")[3:]).replace(".md", "")
        return f"/{prefix}/{year}/{slug}.html"

    def test_personnes_yaml(self):
        noms_defis = self.defis.keys()

        for personne, content in self.personnes.items():
            # Vérification du nom du défi
            for defi in content["defis"]:
                suggestion = difflib.get_close_matches(defi, noms_defis)
                self.assertIn(
                    defi,
                    noms_defis,
                    f"Le défi `{defi}` de {personne} n'existe pas. Suggestions : {', '.join(suggestion)}",
                )

            # Réseaux sociaux
            for key in ["github", "gitlab", "twitter"]:
                if (
                    key in content
                    and content[key]
                    and (
                        content[key].startswith("http") or content[key].startswith("@")
                    )
                ):
                    self.fail(
                        f"La clé `{key}` de {personne} est invalide. Elle ne doit contenir que le pseudo."
                    )

            # Clés obligatoires
            for key in ["link_to", "title", "profil", "programme", "class", "annees"]:
                if key not in content:
                    self.fail(
                        f"La clé `{key}` est obligatoire et est absente pour {personne}."
                    )
                if key == "programme":
                    self.assertIn(
                        content[key],
                        ["EIG", "DIG"],
                        f"La clé `programme` de {personne} semble invalide",
                    )

            # Liens vers sites
            for key in ["website", "linkedin"]:
                if (
                    key in content
                    and content[key]
                    and not content[key].startswith("http")
                ):
                    self.fail(
                        f"La clé `{key}` doit commencer par https:// pour {personne}."
                    )

    def test_personnes_fiches(self):
        noms_personnes = self.personnes.keys()

        for file in glob.glob("_communaute/*.md"):
            content = frontmatter.load(file)
            nom = content["nom"]

            # Check name in individual file
            if nom not in noms_personnes:
                suggestions = difflib.get_close_matches(nom, noms_personnes)

                self.fail(
                    f"Fichier {file} invalide. Le nom `{nom}` n'existe pas. Suggestions : {', '.join(suggestions)}"
                )

            # Check link_to
            filepath = self.clean_filename(file, "communaute")
            self.assertEquals(
                filepath,
                self.personnes[nom]["link_to"],
                f"Le lien `link_to` de {nom} semble invalide.",
            )

    def test_defis_yaml(self):
        required_keys = [
            "image",
            "title",
            "link_to",
            "class",
            "skills",
            "description",
            "administration",
            "administration_website",
            "year",
            "promotion",
            "duration_months",
            "colorback",
            "eigs",
            "mentors",
        ]
        for defi, content in self.defis.items():
            for key in required_keys:
                # Required key
                if key not in content:
                    self.fail(
                        f"La clé `{key}` est absente de {defi} et est obligatoire."
                    )
                # Check promotion
                if key == "promotion":
                    self.assertIn(
                        content[key],
                        [1, 2, 3, "dig"],
                        f"Mauvaise valeur de promotion pour {defi}",
                    )

                # Check colorback
                if key == "colorback":
                    self.assertIn(
                        content[key],
                        ["blue", "red"],
                        f"Mauvaise valeur de colorback pour {defi}",
                    )

                # Check people
                if key in ["eigs", "mentors"]:
                    noms_personnes = self.personnes.keys()
                    for personne in content[key]:
                        # TODO: don't skip for EIG 1
                        if personne not in noms_personnes and content["promotion"] != 1:
                            suggestions = difflib.get_close_matches(
                                personne, noms_personnes
                            )

                            self.fail(
                                f"La personne `{personne}` de `{defi}` n'existe pas. Suggestion : {suggestions}"
                            )

            # TODO: don't skip for EIG 1
            if content["promotion"] == 1:
                continue
            personnes_defi = content["eigs"]
            personnes_defi.extend(content["mentors"])
            self.assertSetEqual(
                set(personnes_defi),
                set(self.personnes_par_defi()[defi]),
                f"Les personnes ne sont pas les bonnes pour {defi}.",
            )

    def test_defis_fiches(self):
        noms_defis = self.defis.keys()

        for file in glob.glob("_defis/*.md"):
            content = frontmatter.load(file)
            nom_defi = content["title"]

            # Check name in individual file
            if nom_defi not in noms_defis:
                suggestions = difflib.get_close_matches(nom, noms_defis)

                self.fail(
                    f"Fichier {file} invalide. Le défi `{nom}` n'existe pas. Suggestions : {', '.join(suggestions)}"
                )

            # Check link_to
            filepath = self.clean_filename(file, "defis")
            self.assertEquals(
                filepath,
                self.defis[nom_defi]["link_to"],
                f"Le lien `link_to` de {nom_defi} semble invalide.",
            )
