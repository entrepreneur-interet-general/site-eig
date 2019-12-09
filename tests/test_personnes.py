import difflib
import glob
import os.path

from base import BaseTest

import frontmatter
from PIL import Image


class TestPersonnes(BaseTest):
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
            for key in [
                "link_to",
                "title",
                "profil",
                "programme",
                "class",
                "annees",
                "image_url",
            ]:
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
            filepath = self.clean_md_filename(file, "communaute")
            self.assertEquals(
                filepath,
                self.personnes[nom]["link_to"],
                f"Le lien `link_to` de {nom} semble invalide.",
            )

    def test_avatars(self):
        for personne, content in self.personnes.items():
            filepath = content["image_url"].replace("/img/", "img/")
            if not os.path.isfile(filepath):
                self.fail(f"Fichier `{filepath}` de {personne} n'existe pas")

            with Image.open(filepath) as img:
                width, height = img.size
                if width < 250:
                    self.fail(
                        f"L'image `{filepath}` de {personne} n'est pas assez grande. Dimensions : {width}x{height}"
                    )
                if width != height:
                    self.fail(
                        f"L'image `{filepath}` de {personne} n'est pas carrée. Dimensions : {width}x{height}"
                    )
