"""
Xavier Gendron
404
Roche, Papier, Ciseaux
"""

import arcade

from game_state import GameState

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE:Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player_list = arcade.SpriteList()
        self.attack_list = arcade.SpriteList()
        self.player_points = 0
        self.computer_points = 0

        compy = arcade.Sprite("assets/compy.png")
        compy.center_x = 575
        compy.center_y = 300
        self.player_list.append(compy)

        facebeard = arcade.Sprite("assets/faceBeard.png")
        facebeard.center_x = 225
        facebeard.center_y = 300
        facebeard.scale = 0.2
        self.player_list.append(facebeard)
        arcade.set_background_color(arcade.color.AMAZON)

        # Si vous avez des listes de sprites, il faut les créer ici et les
        # initialiser à None.

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        pass

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        self.clear()
        self.player_list.draw()

        # player attack
        arcade.draw.draw_lrbt_rectangle_outline(125, 175, 200, 250, arcade.color.GRAY)
        arcade.draw.draw_lrbt_rectangle_outline(200, 250, 200, 250, arcade.color.GRAY)
        arcade.draw.draw_lrbt_rectangle_outline(275, 325, 200, 250, arcade.color.GRAY)

        # computer attack
        arcade.draw.draw_lrbt_rectangle_outline(550, 600, 200, 250, arcade.color.GRAY)

        # titre
        arcade.draw_text("Roche, Papier, Ciseau", 100, 500, arcade.color.BLACK, 50, bold=True)

        # player score
        arcade.draw_text(f"Nombre de points: {self.player_points}", 125, 150, arcade.color.BLACK, 20, bold=True)

        # computer score
        arcade.draw_text(f"Nombre de points: {self.computer_points}", 475, 150, arcade.color.BLACK, 20, bold=True)

        # Invoquer la méthode "draw()" de vos sprites ici.

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres:
            - key: la touche enfoncée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

        Pour connaître la liste des touches possibles:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres:
            - key: la touche relâchée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Méthode invoquée lorsque le curseur de la souris se déplace dans la fenêtre.
        Paramètres:
            - x, y: les coordonnées de l'emplacement actuel de la sourir
            - delta_X, delta_y: le changement (x et y) depuis la dernière fois que la méthode a été invoqué.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button: le bouton de la souris relâché
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
