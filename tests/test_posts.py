import difflib
from collections import defaultdict
import glob

from base import BaseTest

import frontmatter


class TestPosts(BaseTest):
    REQUIRED_KEYS = [
        "author",
        "description",
        "image",
        "layout",
        "title",
        "twitter",
        "tags",
    ]
    ALLOWED_TAGS = {
        "accompagnement",
        "algorithme",
        "collectif",
        "datascience",
        "design",
        "développement",
        "international",
        "méthode",
        "open",
        "outil",
        "partenariat",
        "pérennisation",
        "recrutement",
        "réalisation",
        "témoignage",
        "écosystème",
        "évaluation",
    }

    def test_posts(self):
        tags = []
        for file in glob.glob("_posts/*.md"):
            # Skip drafts
            if file.startswith("_posts/_"):
                continue

            with open(file) as f:
                post = frontmatter.load(f)

            for key in self.REQUIRED_KEYS:
                if key not in post:
                    self.fail(
                        f"La clé `{key}` est absente de `{file}` et est obligatoire"
                    )

            image = post["image"]
            if not (image.startswith("/img/") or image.startswith("http")):
                self.fail(f"L'image de `{file}` semble invalide : {post['image']}")

            self.assertEquals(post["layout"], "post")

            twitter = post["twitter"]
            if twitter is not None and (
                twitter.startswith("https://") or twitter.startswith("@")
            ):
                self.fail(
                    f"Le Twitter `{file}` semble invalide, il faut indiquer uniquement le nom d'utilisateur : {post['twitter']}"
                )

            for tag in post["tags"]:
                self.assertIn(
                    tag, self.ALLOWED_TAGS, f"Le fichier `{file}` a un tag invalide."
                )

            self.assertIn(
                len(post["tags"]),
                range(1, 4 + 1),
                f"Le fichier `{file}` doit comporter entre 1 et 4 tags",
            )
