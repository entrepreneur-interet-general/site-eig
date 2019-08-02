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

            # Check name in individual file
            if content["nom"] not in noms_personnes:
                nom = content["nom"]
                suggestions = difflib.get_close_matches(nom, noms_personnes)

                self.fail(
                    f"Fichier {file} invalide. Le nom `{nom} n'existe pas. Suggestions : {', '.join(suggestions)}"
                )

            # Check link_to
            year = file.replace("_communaute/", "").split("-")[0]
            slug = "-".join(file.replace("_communaute/", "").split("-")[3:]).replace(
                ".md", ""
            )
            filepath = f"/communaute/{year}/{slug}.html"
            self.assertEquals(
                filepath,
                self.personnes[content["nom"]]["link_to"],
                f"Le lien `link_to` de {content['nom']} semble invalide.",
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
                if key not in content:
                    self.fail(
                        f"La clé `{key}` est absente de {defi} et est obligatoire."
                    )

                if key == "promotion":
                    self.assertIn(
                        content[key],
                        [1, 2, 3, "dig"],
                        f"Mauvaise valeur de promotion pour {defi}",
                    )

                if key == "colorback":
                    self.assertIn(
                        content[key],
                        ["blue", "red"],
                        f"Mauvaise valeur de colorback pour {defi}",
                    )

                if key in ["eigs", "mentors"]:
                    noms_personnes = self.personnes.keys()
                    for personne in content[key]:
                        if personne not in noms_personnes:
                            suggestions = difflib.get_close_matches(
                                personne, noms_personnes
                            )

                            self.fail(
                                f"La personne `{personne}` de `{defi}` n'existe pas. Suggestion : {suggestions}"
                            )

            personnes_defi = content["eigs"]
            personnes_defi.extend(content["mentors"])
            self.assertSetEqual(
                set(personnes_defi),
                set(self.personnes_par_defi()[defi]),
                f"Les personnes ne sont pas les bonnes pour {defi}.",
            )
