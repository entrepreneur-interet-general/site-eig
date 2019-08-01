# -*- coding: utf-8 -*-
import unittest
import difflib
import glob

import yaml
import frontmatter


class TestMain(unittest.TestCase):
    def setUp(self):
        with open("_data/defis.yml") as f:
            self.defis = yaml.safe_load(f)

        with open("_data/personnes.yml") as f:
            self.personnes = yaml.safe_load(f)

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
