import difflib
from collections import defaultdict
import glob

from base import BaseTest

import frontmatter


class TestDefis(BaseTest):
    def personnes_par_defi(self):
        res = defaultdict(list)
        for personne, content in self.personnes.items():
            if "defis" in content:
                for defi in content["defis"]:
                    res[defi].append(personne)
        return res

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
                suggestions = difflib.get_close_matches(nom_defi, noms_defis)

                self.fail(
                    f"Fichier {file} invalide. Le défi `{nom_defi}` n'existe pas. Suggestions : {', '.join(suggestions)}"
                )

            # Check link_to
            filepath = self.clean_md_filename(file, "defis")
            self.assertEquals(
                filepath,
                self.defis[nom_defi]["link_to"],
                f"Le lien `link_to` de {nom_defi} semble invalide.",
            )
