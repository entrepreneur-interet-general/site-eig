import difflib
from collections import defaultdict
import glob
import os.path

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
            "skills",
            "description",
            "administration",
            "administration_website",
            "year",
            "promotion",
            "duration_months",
            "eigs",
            "mentors",
        ]
        for defi, content in self.defis.items():
            # Required keys
            for key in required_keys:
                if key not in content:
                    self.fail(
                        f"La clé `{key}` est absente de {defi} et est obligatoire."
                    )

            for key in content.keys():
                # Check promotion
                if key == "promotion":
                    self.assertIn(
                        content[key],
                        [1, 2, 3, 4, "dig"],
                        f"Mauvaise valeur de promotion pour {defi}",
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

                # Check videos
                if key == "end_of_project_videos":
                    for video in content[key]:
                        self.assertEquals(
                            video.keys(),
                            set(["id", "platform", "description", "show"]),
                            f"Clés manquantes pour vidéos du défi {defi}",
                        )
                        self.assertIn(video["show"], [True, False])
                        self.assertIn(video["platform"], ["dailymotion"])

                # Key figures
                if key == "key_figures":
                    self.assertIn(
                        len(content[key]),
                        [2, 3, 4],
                        f"Il faut entre 2 et 4 chiffres clés pour {defi}",
                    )

                    for figure in content[key]:
                        self.assertLessEqual(
                            set(["amount", "description"]),
                            figure.keys(),
                            f"Clés manquantes pour chiffres clés du défi {defi}",
                        )
                        self.assertIsInstance(
                            figure["amount"],
                            int,
                            f"La valeur {figure['amount']} du défi {defi} n'est pas un entier",
                        )

                # Projects
                if key == "projects":
                    self.assertIn(
                        len(content[key]),
                        range(1, 11),
                        f"Il faut entre 1 et 10 réalisations pour {defi}",
                    )

                    for project in content[key]:
                        for key in ["image", "title", "description"]:
                            self.assertIn(
                                key,
                                project.keys(),
                                f"La clé {key} est absente et est obligatoire pour les réalisations du défi {defi}",
                            )
                        image_filepath = project["image"]
                        self.assertTrue(
                            image_filepath.startswith(
                                f"img/realisations/{content['year']}/"
                            ),
                            f"Fichier mal rangé : {image_filepath}. Il doit être dans le dossier `img/realisations/{content['year']}`",
                        )
                        self.assertTrue(
                            os.path.isfile(image_filepath),
                            f"Fichier {image_filepath} est introuvable",
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
