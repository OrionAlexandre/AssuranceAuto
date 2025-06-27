from main import IncapaciteTemporaire, IncapacitePermanente


def test_incapacite_temporaire():
    class Person:
        def __init__(self):
            self.nom: str = "_"
            self.prenom: str = "_"
            self.sexe: str = "F"  # F pour féminin ou M pour masculin
            self.age: int = 22
            self.age_retraite: int = 60

            # Relativement à la profession et au revenu de la personne
            self.est_salarie: bool = True
            self.revenu_net_mensuel: float = 150_000.0
            self.revenu_net_mensuel_apres_accident: float = 0.0
            self.perte_revenu_net_mensuel: float = self.revenu_net_mensuel - self.revenu_net_mensuel_apres_accident

            # Lorsque la personne n'a aucun emplois
            self.revenu_cumule_deux_derniere_annee: float = 0.0

            # Pour déterminer le SMIG applicable le cas échéant
            self.pays_residence: str = ""
            self.pays_accident: str = ""
            self.smig_pays_residence: float = 52_500.0
            self.smig_pays_accident: float = 52_500.0
            pass

    personne = Person()

    print("*" * 35)
    print("*" * 5, "Incapacité temporaire", "*" * 7)
    print("*" * 35)
    # Cas 1
    indemnite_1 = IncapaciteTemporaire(personne, duree_incapacite=10)
    print("Cas 1, Total : ", indemnite_1.valeur_sans_retour_en_fonction, "FCFA")
    # Cas 2
    indemnite_2 = IncapaciteTemporaire(person=personne, duree_incapacite=4)
    indemnite_3 = IncapaciteTemporaire(person=personne, duree_incapacite=6, taux=0.4)
    print("Case 2, Total :",
          sum([indemnite_2.valeur_sans_retour_en_fonction, indemnite_3.valeur_sans_retour_en_fonction]), "FCFA")


def test_incapacite_permanente_1():
    class Person:
        def __init__(self):
            self.nom: str = "_"
            self.prenom: str = "_"
            self.sexe: str = "F"  # F pour féminin ou M pour masculin
            self.age: int = 40
            self.age_retraite: int = 60

            # Relativement à la profession et au revenu de la personne
            self.est_salarie: bool = True
            self.revenu_net_mensuel: float = 25_000.0
            self.revenu_net_mensuel_apres_accident: float = 0.0
            self.perte_revenu_net_mensuel: float = self.revenu_net_mensuel - self.revenu_net_mensuel_apres_accident

            # Lorsque la personne n'a aucun emplois
            self.revenu_cumule_deux_derniere_annee: float = 0.0

            # Pour déterminer le SMIG applicable le cas échéant
            self.pays_residence: str = ""
            self.pays_accident: str = ""
            self.smig_pays_residence: float = 25_000.0
            self.smig_pays_accident: float = 25_000.0
            pass

    personne = Person()

    print("*" * 35)
    print("*" * 5, "Incapacité Permanente", "*" * 7)
    print("*" * 35)


    ip_1 = IncapacitePermanente(personne, taux_ip=20)
    print("Préjudice physiologique:", ip_1.prejudice_physiologique ,"FCFA")
    print("Préjudice économique:", ip_1.prejudice_economique, "FCFA")
    print("Préjudice moral:", ip_1.prejudice_moral, "FCFA")
    print("Total: " + str(ip_1.valeur_totale), "FCFA")

    pass


def test_incapacite_permanente_2():
    class Person:
        def __init__(self):
            self.nom: str = "_"
            self.prenom: str = "_"
            self.sexe: str = "M"  # F pour féminin ou M pour masculin
            self.age: int = 45 # Âge de consolidation
            self.age_retraite: int = 60 # Âge de la retraite

            # Relativement à la profession et au revenu de la personne
            self.est_salarie: bool = True
            self.revenu_net_mensuel: float = 300_000.0
            self.revenu_net_mensuel_apres_accident: float = 285_000.0
            self.perte_revenu_net_mensuel: float = self.revenu_net_mensuel - self.revenu_net_mensuel_apres_accident

            # Lorsque la personne n'a aucun emplois
            self.revenu_cumule_deux_derniere_annee: float = 0.0

            # Pour déterminer le SMIG applicable le cas échéant
            self.pays_residence: str = ""
            self.pays_accident: str = ""
            self.smig_pays_residence: float = 25_000.0
            self.smig_pays_accident: float = 25_000.0
            pass

    personne = Person()

    print("*" * 35)
    print("*" * 5, "Incapacité Permanente", "*" * 7)
    print("*" * 35)


    ip = IncapacitePermanente(personne, taux_ip=65)
    print("Préjudice physiologique:", ip.prejudice_physiologique ,"FCFA", "| Valeur Point d'IP:", ip.valeur_point_ip, "| Taux d'IP:", ip.taux_ip)
    print("Préjudice économique:", ip.prejudice_economique, "FCFA", "| Perte de salaire:", personne.perte_revenu_net_mensuel, "| Taux de conversion:", ip.taux_conversion)
    print("Préjudice moral:", ip.prejudice_moral, "FCFA")
    print("Total: " + str(ip.valeur_totale), "FCFA")

    pass


if __name__ == '__main__':
    test_incapacite_permanente_2()