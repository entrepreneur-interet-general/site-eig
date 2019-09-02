from base import BaseTest


class TestPromos(BaseTest):
    def test_promos(self):
        noms_defis = self.defis.keys()
        for promo_name, promo in self.promos.items():
            self.assertIn(
                promo["defi"],
                noms_defis,
                f"La promotion `{promo_name}` comporte un nom de défi invalide dans le fichier `_data/promos.yml`.",
            )
