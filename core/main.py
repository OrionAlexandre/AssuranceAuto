"""
Ce fichier servira à la logique de calcul dans l'interface graphique, les logiques métier fondé sur le code CIMA dans
le cas d'une personne bléssée.
S'y trouve : \n
- l'incapacité temporaire
- l'incapacité permanente

Les préjudices extrapatrimoniaux : \n
- le pretium doloris
- le préjudice esthétique
- le préjudice d'agrément
- le préjudice moral
- le préjudice scolaire
- l'assistance d'une tierce personne
"""

class Person:
    def __init__(self):
        self.nom: str = "_"
        self.prenom: str = "_"
        self.sexe: str = "F"  # F pour féminin ou M pour masculin
        self.age: int = 22
        self.age_retraite: int = 60
        self.est_vivante: bool = True # Si la personne est encore en vie.

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

        # Situation matrimoniale
        self.est_mariee: bool = True # Si la personne justifie d'un mariage
        self.est_parent: bool = True # Si la personne a des enfants.
        pass


class IncapaciteTemporaire:
    def __init__(self, person: Person, duree_incapacite: int, taux: float = 1.0):
        """

        :param person: il s'agit de la victime.
        :param duree_incapacite: Elle est fixée par expertise médicale.
        :param taux: 0 - 1, il s'agit du taux d'incapacité temporaire fixée par expertise médicale.
        """
        self.person: Person = person
        self.duree_incapacite: int = duree_incapacite
        self.taux: float = taux
        pass

    def smig(self) -> float:
        """
        Le SMIG s'entend pour le pays sur le territoire duquel s'est produit l'accident, ou, s'il est plus élevé, pour
        le pays de l'espace CIMA où la victime a sa résidence habituelle.
        :return:
        """
        return max(self.person.smig_pays_accident, self.person.smig_pays_residence)

    def maximum(self) -> float:
        """
        Pour les personnes justifiant d'un revenu mensuel ou sur les deux dernières années dans le cas où elles ne sont
        pas salariées, le maximum est six fois le SMIG annuel.
        :return:
        """
        valeur: float = 0.0
        if self.person.est_salarie or self.person.revenu_cumule_deux_derniere_annee != 0 :
            valeur = 6 * self.smig()
            return valeur

        valeur = 12 * self.smig()
        return valeur

    # Fonctions dédiées au calcul de l'indemnité au titre de l'incapacité temporaire
    @property
    def valeur_sans_retour_en_fonction(self) -> float:
        """
        La victime est en période de convalescence, elle ne peut donc se rendre au travail ou exercé afin d'être
        payée. La victime pert ainsi temporairement ses revenus proportionnellement à la périon de l'incapacité.
        :return: Le montant de l'indemnité, plafonné si nécessaire
        """
        valeur: float = 0.0
        salaire_journalier_moyen: float = 0.0

        maximum_valeur: float = self.maximum() # le maximum à ne pas dépasser selon le code CIMA.
        salaire_journalier_moyen = self.person.revenu_net_mensuel / 30 # trentes jours dans l'année.

        # Montant de l'indemnité en considération du niveau ou du taux d'incapacité
        valeur = salaire_journalier_moyen * self.duree_incapacite * self.taux

        # Dans le cas où la personne n'est pas salariée, mais justifie d'un revenu.
        if not self.person.est_salarie:
            valeur = 0 # N'ayant pas encore de méthode de calcul pour un cas pareil.
            pass

        # Cette ligne retourne la plus petite valeur entre la valeur de l'indemnité et la limite fixée par le code CIMA.
        return min(valeur, maximum_valeur)

    @property
    def valeur_avec_perte_de_revenu(self) -> float:
        """"
        Dans le cas présent, on prend juste la différence de revenu ou la perte de revenu.
        :returns: Le montant de l'indemnité, plafonné si nécessaire
        """
        valeur: float = 0.0

        # le maximum à ne pas dépasser selon le code CIMA.
        maximum_valeur: float = self.maximum()

        valeur = self.person.perte_revenu_net_mensuel

        # Cette ligne retourne le maximum si la valeur de l'indemnité est supérieure à la limite fixée par le code CIMA.
        # Sinon, on prend juste la valeur.
        return min(valeur, maximum_valeur)


class ValeurPointIP:
    def __init__(self, person: Person, taux_ip: float):
        """

        :param person: La victime
        :param taux_ip: Le taux d'IP
        """
        self.person: Person = person
        self.taux_ip: float = taux_ip

        self.age: int = self.person.age

    @property
    def valeur(self):

        if self.person.age <= 0:
            return 0

        if self.taux_ip <= 5:
            if self.person.age <= 59:
                return 6
            else:
                return 5

        if self.taux_ip <= 10:
            if self.person.age <= 59:
                return 12
            else:
                return 10

        if self.taux_ip <= 15:
            if self.person.age <= 39:
                return 14
            elif self.person.age <= 59:
                return 12
            else:
                return 10

        if self.taux_ip <= 20:
            if self.person.age <= 19:
                return 16
            elif self.person.age <= 39:
                return 14
            else:
                return 12

        if self.taux_ip <= 30:
            if self.person.age <= 19:
                return 17
            elif self.person.age <= 39:
                return 17
            elif self.person.age <= 69:
                return 17
            else:
                return 12

        if self.taux_ip <= 40:
            if self.person.age <= 19:
                return 18
            elif self.person.age <= 29:
                return 17
            elif self.person.age <= 39:
                return 16
            elif self.person.age <= 69:
                return 14
            else:
                return 13

        if self.taux_ip <= 50:
            if self.person.age <= 24:
                return 18
            elif self.person.age <= 39:
                return 17
            elif self.person.age <= 59:
                return 16
            elif self.person.age <= 69:
                return 15
            else:
                return 13

        if self.taux_ip <= 70:
            if self.person.age <= 24:
                return 19
            elif self.person.age <= 39:
                return 18
            elif self.person.age <= 59:
                return 17
            elif self.person.age <= 69:
                return 16
            else:
                return 14

        if self.taux_ip <= 90:
            if self.person.age <= 15:
                return 25
            elif self.person.age <= 24:
                return 20
            elif self.person.age <= 39:
                return 19
            elif self.person.age <= 59:
                return 18
            elif self.person.age <= 69:
                return 17
            else:
                return 15

        if self.taux_ip <= 100:
            if self.person.age <= 15:
                return 29
            elif self.person.age <= 24:
                return 24
            elif self.person.age <= 39:
                return 22
            elif self.person.age <= 59:
                return 20
            elif self.person.age <= 69:
                return 19
            else:
                return 18

        return -1

    pass


class TableViagere100:
    def __init__(self, person: Person):
        """

        :param person: La victime
        """
        self.person = person

        self.__baremes_masculin: list[float] = \
            [14.576, 14.910, 14.915, 14.903, 14.884, 14.861, 14.835, 14.807, 14.777, 14.744,
            14.709, 14.671, 14.631, 14.588, 14.543, 14.497, 14.450, 14.401, 14.353, 14.304,
            14.253, 14.200, 14.144, 14.086, 14.025, 13.959, 13.891, 13.818, 13.740, 13.658,
            13.571, 13.480, 13.384, 13.284, 13.180, 13.071, 12.958, 12.839, 12.716, 12.588,
            12.455, 12.316, 12.172, 12.023, 11.869, 11.709, 11.544, 11.373, 11.197, 11.016,
            10.829, 10.637, 10.440, 10.237, 10.030, 9.818, 9.602, 9.381, 9.156, 8.928,
            8.696, 8.461, 8.223, 7.983, 7.741, 7.498, 7.254, 7.010, 6.766, 6.523,
            6.282, 6.043, 5.808, 5.577, 5.351, 5.132, 4.921, 4.720, 4.531, 4.356,
            2.707, 3.582, 3.371, 3.167, 2.969, 2.778, 2.593, 2.415, 2.244, 2.081,
            1.924, 1.775, 1.633, 1.498, 1.371, 1.250, 1.136, 1.030, 0.930, 0.836,
            0.748] # Les barêmes

        self.__baremes_feminin: list[float] = \
            [14.806, 15.065, 15.077, 15.072, 15.061, 15.048, 15.033, 15.016, 14.997, 14.976,
             14.953, 14.929, 14.904, 14.876, 14.848, 14.818, 14.787, 14.755, 14.721, 14.686,
             14.650, 14.612, 14.572, 14.529, 14.485, 14.438, 14.388, 14.336, 14.281, 14.223,
             14.163, 14.099, 14.032, 13.961, 13.886, 13.807, 13.724, 13.636, 13.544, 13.448,
             13.346, 13.240, 13.128, 13.011, 12.888, 12.760, 12.625, 12.485, 12.339, 12.186,
             12.026, 11.861, 11.688, 11.509, 11.323, 11.130, 10.931, 10.725, 10.512, 10.293,
             10.067, 9.835, 9.597, 9.352, 9.103, 8.848, 8.588, 8.324, 8.056, 7.784,
             7.509, 7.232, 6.953, 6.672, 6.391, 6.110, 5.830, 5.551, 5.275, 5.001,
             4.731, 4.466, 4.205, 3.950, 3.701, 3.459, 3.224, 2.997, 2.778, 2.567,
             2.365, 2.173, 1.989, 1.815, 1.650, 1.494, 1.348, 1.210, 1.082, 0.963,
             0.851]  # Les barêmes

    def taux_de_conversion(self) -> float:
        """
        Par coïncidence les indexe de la liste des barêmes vont de 0 à 100, il suffit juste de retourner le barême situé
        à indexer équivalent en âge à l'âge de la personne.
        :param age_person:
        :return : Le barême correspondant à l'âge de la personne
        """
        baremes: list[float] = self.__baremes_feminin if self.person.sexe == "F" else self.__baremes_masculin
        return baremes[self.person.age] if 0 <= self.person.age <= 100 else 0.0


class TableTemporaire65:
    def __init__(self, person: Person):
        """

        :param person: La victime
        """
        self.person = person

        self.__baremes_masculin: list[float] = \
            [14.492, 14.819, 14.818, 14.799, 14.773, 14.743, 14.710, 14.674, 14.634, 14.592,
             14.547, 14.499, 14.447, 14.392, 14.335, 14.276, 14.213, 14.149, 14.084, 14.017,
             13.947, 13.873, 13.796, 13.715, 13.628, 13.537, 13.440, 13.337, 13.228, 13.111,
             12.988, 12.857, 12.720, 12.575, 12.423, 12.263, 12.095, 11.918, 11.731, 11.536,
             11.330, 11.114, 10.886, 10.647, 10.396, 10.132, 9.855, 9.563, 9.255, 8.932,
             8.591, 8.232, 7.854, 7.454, 7.031, 6.583, 6.109, 5.604, 5.068, 4.495,
             3.881, 3.223, 2.513, 1.745, 0.911, 0.000]  # Les barêmes

        self.__baremes_feminin: list[float] = \
            [14.685, 14.935, 14.938, 14.923, 14.903, 14.880, 14.853, 14.824, 14.793, 14.759,
             14.722, 14.683, 14.641, 14.597, 14.550, 14.500, 14.449, 14.394, 14.337, 14.277,
             14.214, 14.148, 14.077, 14.002, 13.923, 13.839, 13.750, 13.655, 13.556, 13.450,
             13.338, 13.220, 13.094, 12.961, 12.820, 12.671, 12.512, 12.344, 12.166, 11.978,
             11.778, 11.567, 11.343, 11.105, 10.854, 10.588, 10.306, 10.008, 9.692, 9.358,
             9.003, 8.628, 8.230, 7.808, 7.360, 6.885, 6.380, 5.844, 5.272, 4.664,
             4.015, 3.321, 2.578, 1.781, 0.924, 0.000]  # Les barêmes

    def taux_de_conversion(self) -> float:
        """
        Par coïncidence les indexe de la liste des barêmes vont de 0 à 100, il suffit juste de retourner le barême situé
        à indexer équivalent en âge à l'âge de la personne.
        :param age_person:
        :return : Le barême correspondant à l'âge de la personne
        """
        baremes: list[float] = self.__baremes_feminin if self.person.sexe == "F" else self.__baremes_masculin
        return baremes[self.person.age] if 0 <= self.person.age <= 65 else 0.0

    pass


class TableTemporaire60:
    def __init__(self, person: Person):
        """

        :param person: La victime
        """
        self.person = person

        self.__baremes_masculin: list[float] = \
            [14.425, 14.745, 14.739, 14.715, 14.684, 14.648, 14.609, 14.566, 14.519, 14.470,
             14.417, 14.360, 14.299, 14.235, 14.167, 14.095, 14.022, 13.945, 13.867, 13.785,
             13.700, 13.610, 13.515, 13.415, 13.309, 13.196, 13.077, 12.950, 12.814, 12.670,
             12.517, 12.355, 12.184, 12.004, 11.813, 11.612, 11.399, 11.175, 10.938, 10.688,
             10.423, 10.144, 9.850, 9.538, 9.209, 8.861, 8.493, 8.103, 7.690, 7.252,
             6.787, 6.294, 5.769, 5.210, 4.613, 3.975, 3.293, 2.560, 1.772, 0.921,
             0.000]  # Les barêmes

        self.__baremes_feminin: list[float] = \
            [14.606, 14.848, 14.845, 14.825, 14.798, 14.768, 14.734, 14.697, 14.658, 14.615,
             14.569, 14.519, 14.467, 14.411, 14.352, 14.290, 14.224, 14.155, 14.083, 14.006,
             13.925, 13.840, 13.749, 13.652, 13.550, 13.441, 13.326, 13.204, 13.074, 12.937,
             12.791, 12.637, 12.473, 12.299, 12.113, 11.917, 11.709, 11.487, 11.252, 11.003,
             10.738, 10.457, 10.158, 9.841, 9.505, 9.148, 8.768, 8.365, 7.937, 7.482,
             6.998, 6.483, 5.936, 5.353, 4.731, 4.069, 3.361, 2.605, 1.797, 0.930,
             0.000]  # Les barêmes

    def taux_de_conversion(self) -> float:
        """
        Par coïncidence les indexe de la liste des barêmes vont de 0 à 100, il suffit juste de retourner le barême situé
        à indexer équivalent en âge à l'âge de la personne.
        :param age_person:
        :return : Le barême correspondant à l'âge de la personne
        """
        baremes: list[float] = self.__baremes_feminin if self.person.sexe == "F" else self.__baremes_masculin
        return baremes[self.person.age] if 0 <= self.person.age <= 60 else 0.0
    pass


class TableTemporaire55:
    def __init__(self, person: Person):
        """

        :param person: La victime
        """
        self.person = person

        self.__baremes_masculin: list[float] = \
            [14.322, 14.633, 14.620, 14.588, 14.548, 14.503, 14.454, 14.401, 14.344, 14.283,
             14.218, 14.148, 14.073, 13.994, 13.910, 13.822, 13.730, 13.635, 13.536 ,13.432,
             13.324, 13.209, 13.088, 12.959, 12.822, 12.677, 12.523, 12.359, 12.184, 11.998,
             11.800, 11.590, 11.368, 11.132, 10.883, 10.618, 10.338, 10.042, 9.728, 9.394,
             9.041, 8.667, 8.269, 7.847, 7.399, 6.923, 6.417, 5.878, 5.303, 4.691,
             4.037, 3.339, 2.591, 1.789, 0.927, 0.000]  # Les barêmes

        self.__baremes_feminin: list[float] = \
            [14.490, 14.723, 14.712, 14.683, 14.647, 14.606, 14.562, 14.514, 14.462, 14.407,
             14.347, 14.283, 14.215, 14.143, 14.067, 13.986, 13.900, 13.810, 13.715, 13.614,
             13.508, 13.394, 13.274, 13.146, 13.011, 12.867, 12.714, 12.551, 12.379, 12.196,
             12.001, 11.794, 11.575, 11.341, 11.092, 10.828, 10.547, 10.249, 9.931, 9.594,
             9.235, 8.853, 8.447, 8.015, 7.555, 7.066, 6.546, 5.991, 5.401, 4.772,
             4.101, 3.385, 2.622, 1.806, 0.933, 0.000]  # Les barêmes

    def taux_de_conversion(self) -> float:
        """
        Par coïncidence les indexe de la liste des barêmes vont de 0 à 100, il suffit juste de retourner le barême situé
        à indexer équivalent en âge à l'âge de la personne.
        :param age_person:
        :return : Le barême correspondant à l'âge de la personne
        """
        baremes: list[float] = self.__baremes_feminin if self.person.sexe == "F" else self.__baremes_masculin
        return baremes[self.person.age] if 0 <= self.person.age <= 55 else 0.0
    pass


class TableTemporaire25:
    def __init__(self, person: Person):
        """

        :param person: La victime
        """
        self.person = person

        self.__baremes_masculin: list[float] = \
            [11.815, 11.896, 11.698, 11.473, 11.228, 10.965, 10.684, 10.384, 10.064, 9.723,
             9.359, 8.971, 8.558, 8.118, 7.650, 7.151, 6.621, 6.057, 5.457, 4.819,
             4.139, 3.414, 2.641, 1.816, 0.938, 0.000]  # Les barêmes

        self.__baremes_feminin: list[float] = \
            [11.908, 11.920, 11.721, 11.495, 11.249, 10.986, 10.705, 10.405, 10.085, 9.743,
             9.379, 8.991, 8.578, 8.138, 7.670, 7.171, 6.640, 6.074, 5.472, 4.831,
             4.148, 3.420, 2.645, 1.819, 0.938, 0.000]  # Les barêmes

    def taux_de_conversion(self) -> float:
        """
        Par coïncidence les indexe de la liste des barêmes vont de 0 à 100, il suffit juste de retourner le barême situé
        à indexer équivalent en âge à l'âge de la personne.
        :param age_person:
        :return : Le barême correspondant à l'âge de la personne
        """
        baremes: list[float] = self.__baremes_feminin if self.person.sexe == "F" else self.__baremes_masculin
        return baremes[self.person.age] if 0 <= self.person.age <= 25 else 0.0
    pass


class TableTemporaire21:
    def __init__(self, person: Person):
        """

        :param person: La victime
        """
        self.person = person

        self.__baremes_masculin: list[float] = \
            [10.941, 10.942, 10.680, 10.387, 10.071, 9.732, 9.370, 8.984, 8.573, 8.134,
             7.666, 7.167, 6.636, 6.070, 5.468, 4.826, 4.143, 3.416, 2.642, 1.817,
             0.938, 0.000]  # Les barêmes

        self.__baremes_feminin: list[float] = \
            [11.022, 10.959, 10.696, 10.401, 10.084, 9.745, 9.383, 8.996, 8.584, 8.144,
             7.676, 7.177, 6.645, 6.079, 5.476, 4.834, 4.150, 3.421, 2.646, 1.819,
             0.938, 0.000]  # Les barêmes

    def taux_de_conversion(self) -> float:
        """
        Par coïncidence les indexe de la liste des barêmes vont de 0 à 100, il suffit juste de retourner le barême situé
        à indexer équivalent en âge à l'âge de la personne.
        :param age_person:
        :return : Le barême correspondant à l'âge de la personne
        """
        baremes: list[float] = self.__baremes_feminin if self.person.sexe == "F" else self.__baremes_masculin
        return baremes[self.person.age] if 0 <= self.person.age <= 21 else 0.0
    pass


class IncapacitePermanente:
    def __init__(self, person: Person, taux_ip: float, accord_prejudice_physiologique: float = 0.0):
        """

        :param person: La victime
        :param taux_ip: De 0 à 100, fixé par exeprtise médicale, il s'agit du taux d'incapacité permanente.
        :param accord_prejudice_physiologique: Le montant fixé par accord entre la victime et l'assureur.
        """
        self.person: Person = person
        self.taux_ip: float = taux_ip
        self.valeur_point_ip: int = ValeurPointIP(self.person, self.taux_ip).valeur
        self.accord_prejudice_physiologique: float = accord_prejudice_physiologique
        pass

    def smig(self) -> float:
        return max(self.person.smig_pays_accident, self.person.smig_pays_residence)

    @property
    def prejudice_physiologique(self) -> float:
        # En cas d'accord, l'on s'en tient à la valeur convenue par les deux parties. Sinon, on passe à la détermination.
        if self.accord_prejudice_physiologique != 0.0:
            return self.accord_prejudice_physiologique

        valeur: float = self.smig() * 12 * self.valeur_point_ip / 100 * self.taux_ip  # Selon YIGBEDEK
        return valeur

    @property
    def taux_conversion(self):
        taux_conversion: float = 0.0
        match self.person.age_retraite:
            case 55:
                taux_conversion: float = TableTemporaire55(self.person).taux_de_conversion()
            case 60:
                taux_conversion: float = TableTemporaire60(self.person).taux_de_conversion()
            case 65:
                taux_conversion: float = TableTemporaire65(self.person).taux_de_conversion()
        return taux_conversion

    @property
    def prejudice_economique(self) -> float:
        taux_conversion: float = self.taux_conversion
        if self.taux_ip < 50:
            return 0 # Il n'y a pas de préjudice économique en dessous de 50% d'IP.

        if self.person.est_salarie:
            valeur: float = self.person.perte_revenu_net_mensuel * 12 * taux_conversion # La différence de salaire capitalisé jusqu'à l'âge de la retraite.
        else:
            valeur: float = self.smig() * 12 * taux_conversion # La personne n'est pas salarié, sur la base du SMIG annuel.
        plafond: float = 10 * 12 * self.smig() # Plafond du code CIMA (Dix fois le SMIG annuel)
        return min(valeur, plafond)

    @property
    def prejudice_moral(self) -> float:
        # return 2 * 12 * self.smig() if self.taux_ip >= 80 else 0
        if self.taux_ip < 80:
            return 0 # Il n'y a pas de préjudice moral en dessous de 80% d'IP.

        valeur: float = 2 * 12 * self.smig() # L'indemnité est fixée à deux fois le montant du SMIG annuel.
        return valeur

    @property
    def valeur_totale(self) -> float:
        return sum([
            self.prejudice_physiologique,
            self.prejudice_economique,
            self.prejudice_moral
        ])
    pass


class NiveauPrejudice:
    """
    Cette class sert à évaluer le niveau du préjudice. Il s'agit de :
        - Très léger
        - Léger
        - Modéré
        - Moyen
        - Assez important
        - Très important
        - Exceptionnel
    """
    def __init__(self):
        pass

    @property
    def tres_leger(self):
        return 5

    @property
    def leger(self):
        return 10

    @property
    def moderer(self):
        return 20

    @property
    def moyen(self):
        return 40

    @property
    def assez_important(self):
        return 60

    @property
    def important(self):
        return 100

    @property
    def tres_important(self):
        return 150

    @property
    def exceptionnel(self):
        return 300


class PretiumDoloris:
    def __init__(self, person: Person, niveau_prejudice: int):
        self.person: Person = person
        self.niveau_prejudice: int = niveau_prejudice
        self.smig: float = max(self.person.smig_pays_accident, self.person.smig_pays_residence)

    @property
    def valeur(self) -> float:
        """
        Article 262 du code CIMA.
        :return: La valeur en pourcentage du smig annuel.
        """
        return self.niveau_prejudice / 100 * 12 * self.smig
    pass


class PejudiceEsthetique:
    def __init__(self, person: Person, niveau_prejudice: int):
        self.person: Person = person
        self.niveau_prejudice: int = niveau_prejudice
        self.smig: float = max(self.person.smig_pays_accident, self.person.smig_pays_residence)

    @property
    def valeur(self) -> float:
        """
        Selon M. YIGBEDEK, l'évaluation du préjudice esthétique se fait de la même façon que le pretium dolotis.
        :return: La valeur en pourcentage du smig annuel.
        """
        return self.niveau_prejudice / 100 * 12 * self.smig
    pass


class PrejudiceAgrement:
    pass


class PrejudiceMoraleDuConjoint:
    def __init__(self, person: Person, taux_ip: float, montant_alloue: float = 0.0):
        """
        Article 229 du code CIMA.
        :param person : La victime
        :param taux_ip : Le taux d'incapacité volontaire
        :param montant_alloue : Le montant alloué au titre du préjudice moral du conjoint
        """
        self.person: Person = person
        self.taux_ip: float = taux_ip
        self.montant_alloue: float = montant_alloue
        self.plafond: float = max(self.person.smig_pays_accident, self.person.smig_pays_residence) * 2 * 12 # Deux smig annuel.
        pass

    @property
    def montant_alloue(self):
        """
        Seulement en cas d'incapacité totale et si la victime est mariée et vivante.
        Le cas relatif au décès de la victime fera l'objet d'un autre traitement dans la suite de l'aglorithme.
        :return:
        """
        if self.person.est_mariee and self.taux_ip == 100 and self.person.est_vivante:
            return min(self.montant_alloue, self.plafond)
        return 0.0 # Le cas échéant, rien n'est alloué au titre de ce préjudice.

    @montant_alloue.setter
    def montant_alloue(self, valeur: int | float):
        """
        Afin de définir directement le montant de l'indeminité.
        :param valeur:
        :return:
        """
        self.montant_alloue: float = valeur if isinstance(valeur, int | float) else 0.0
    pass


class PrejudiceScolaire:
    pass


class AssistanceTiercePersonne:
    def __init__(self, taux_ip: float, indeminte_ip: float, montant_alloue: float = 0.0):
        self.taux_ip: float = taux_ip # Le taux d'IP de la victime
        self.indemnite_ip: float = indeminte_ip # L'indemnité allouée à la victime au titre de l'incapacité permanente.
        self.montant_alloue: float = montant_alloue # Montant allouée au titre de l'assistance d'une tierce personne.
        self.plafond: float = 50 / 100 * self.indemnite_ip # Le plafond selon le code CIMA.


    @property
    def montant_alloue(self) -> float:
        return min(self.montant_alloue, self.plafond)

    @montant_alloue.setter
    def montant_alloue(self, value: float | int):
        self.montant_alloue: float = value if value >= 0 else 0
    pass


class FraisDeTraitement:
    def __init__(self):
        self.__frais_meciaux_chirurgicaux_pharmaceutiques: float = 0.0
        self.__frais_transport: float = 0.0
        self.__frais_sejour_hospitalier: float = 0.0
        self.__frais_appareillage_et_prothese: float = 0.0
        self.__frais_reeducation: float = 0.0
        self.__frais_deplacement: float = 0.0
        self.__total: float = 0.0

    @property
    def frais_meciaux_chirurgicaux_pharmaceutiques(self) -> float:
        """
        Retourne les frais de transport médical engagés.
        """
        return self.__frais_meciaux_chirurgicaux_pharmaceutiques

    @frais_meciaux_chirurgicaux_pharmaceutiques.setter
    def frais_meciaux_chirurgicaux_pharmaceutiques(self, valeur: float | int):
        """
        Définit les frais de médicaux, chirurgicaux et pharmaceutiques.
        """
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__frais_meciaux_chirurgicaux_pharmaceutiques = round(float(valeur), 2)
        else:
            self.__frais_meciaux_chirurgicaux_pharmaceutiques = 0.0

    @property
    def frais_transport(self) -> float:
        """
        Retourne les frais de transport médical engagés le jour du sinistre pour emmener la victime à l'hôtpital
        """
        return self.__frais_transport

    @frais_transport.setter
    def frais_transport(self, valeur: float | int):
        """
        Définit les frais de transport avec validation automatique
        """
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__frais_transport = round(float(valeur), 2)
        else:
            self.__frais_transport = 0.0

    @property
    def frais_sejour_hospitalier(self) -> float:
        """
        Retourne les frais d'hospitalisation pour le box ou la chambre de la victime validés
        """
        return self.__frais_sejour_hospitalier

    @frais_sejour_hospitalier.setter
    def frais_sejour_hospitalier(self, valeur: float | int):
        """
        Définit les frais d'hospitalisation selon les règles CIMA
        """
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__frais_sejour_hospitalier = round(float(valeur), 2)
        else:
            self.__frais_sejour_hospitalier = 0.0

    @property
    def frais_appareillage_et_prothese(self) -> float:
        """
        Retourne le coût validé des appareillages/prothèses
        """
        return self.__frais_appareillage_et_prothese

    @frais_appareillage_et_prothese.setter
    def frais_appareillage_et_prothese(self, valeur: float | int):
        """
        Définit les frais d'appareillage et de prothèse avec contrôle strict
        """
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__frais_appareillage_et_prothese = round(float(valeur), 2)
        else:
            self.__frais_appareillage_et_prothese = 0.0

    @property
    def frais_reeducation(self) -> float:
        """
        Retourne les frais de rééducation après validation
        """
        return self.__frais_reeducation

    @frais_reeducation.setter
    def frais_reeducation(self, valeur: float | int):
        """
        Définit les frais de rééducation
        """
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__frais_reeducation = round(float(valeur), 2)
        else:
            self.__frais_reeducation = 0.0

    @property
    def frais_deplacement(self) -> float:
        """
        Retourne les frais de déplacement approuvés
        """
        return self.__frais_deplacement

    @frais_deplacement.setter
    def frais_deplacement(self, valeur: float | int):
        """
        Définit les frais de déplacement selon réglementation
        """
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__frais_deplacement = round(float(valeur), 2)
        else:
            self.__frais_deplacement = 0.0

    @property
    def total(self) -> float:
        """
        Définit le total
        """
        self.__total = sum([self.frais_transport,
                            self.frais_meciaux_chirurgicaux_pharmaceutiques,
                            self.frais_deplacement,
                            self.frais_sejour_hospitalier,
                            self.frais_appareillage_et_prothese,
                            self.frais_reeducation])
        return self.__total

    @total.setter
    def total(self, valeur):
        if isinstance(valeur, (float, int)) and valeur >= 0:
            self.__total = round(float(valeur), 2)
        else:
            self.__total = 0.0
    pass

