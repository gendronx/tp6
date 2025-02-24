"""
Xavier Gendron
404
Roche, Papier, Ciseaux
"""

import arcade
from random import randint

from game_state import GameState
from attack_animation import AttackAnimation, AttackType

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
        self.computer_rock_attack = arcade.SpriteList()
        self.computer_paper_attack = arcade.SpriteList()
        self.computer_scissors_attack = arcade.SpriteList()
        self.player_points = 0
        self.computer_points = 0
        self.game_state = GameState.NOT_STARTED
        self.player_attack = None
        self.rock_attack = False
        self.paper_attack = False
        self.scissors_attack = False
        self.computer_attack = None
        self.flag = False
        self.gagnant_round = ""
        self.gagnant_partie = ""

        self.compy = arcade.Sprite("assets/compy.png")
        self.compy.center_x = 575
        self.compy.center_y = 300
        self.player_list.append(self.compy)

        self.facebeard = arcade.Sprite("assets/faceBeard.png")
        self.facebeard.center_x = 225
        self.facebeard.center_y = 300
        self.facebeard.scale = 0.2
        self.player_list.append(self.facebeard)
        arcade.set_background_color(arcade.color.AMAZON)

        # roche
        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock.center_x = 158
        self.rock.center_y = 225
        self.rock.scale = 0.4
        self.attack_list.append(self.rock)

        # papier
        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.center_x = 228
        self.paper.center_y = 225
        self.paper.scale = 0.4
        self.attack_list.append(self.paper)

        # ciseau
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.scissors.center_x = 303
        self.scissors.center_y = 225
        self.scissors.scale = 0.4
        self.attack_list.append(self.scissors)

        # roche ordi
        self.computer_rock = AttackAnimation(AttackType.ROCK)
        self.computer_rock.center_x = 575
        self.computer_rock.center_y = 225
        self.computer_rock.scale = 0.4
        self.computer_rock_attack.append(self.computer_rock)

        # papier ordi
        self.computer_paper = AttackAnimation(AttackType.PAPER)
        self.computer_paper.center_x = 575
        self.computer_paper.center_y = 225
        self.computer_paper.scale = 0.4
        self.computer_paper_attack.append(self.computer_paper)

        # ciseau ordi
        self.computer_scissors = AttackAnimation(AttackType.SCISSORS)
        self.computer_scissors.center_x = 575
        self.computer_scissors.center_y = 225
        self.computer_scissors.scale = 0.4
        self.computer_scissors_attack.append(self.computer_scissors)
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
        self.attack_list.draw()

        # player rectangle
        arcade.draw.draw_lrbt_rectangle_outline(125, 175, 200, 250, arcade.color.GRAY)
        arcade.draw.draw_lrbt_rectangle_outline(200, 250, 200, 250, arcade.color.GRAY)
        arcade.draw.draw_lrbt_rectangle_outline(275, 325, 200, 250, arcade.color.GRAY)

        # computer rectangle
        arcade.draw.draw_lrbt_rectangle_outline(550, 600, 200, 250, arcade.color.GRAY)

        # titre
        arcade.draw_text("Roche, Papier, Ciseau", 100, 500, arcade.color.BLACK, 50, bold=True)

        # player score
        arcade.draw_text(f"Nombre de points: {self.player_points}", 125, 150, arcade.color.BLACK, 20, bold=True)

        # computer score
        arcade.draw_text(f"Nombre de points: {self.computer_points}", 475, 150, arcade.color.BLACK, 20, bold=True)

        # computer attack
        if self.computer_attack == AttackType.ROCK:
            self.computer_rock_attack.draw()

        if self.computer_attack == AttackType.PAPER:
            self.computer_paper_attack.draw()

        if self.computer_attack == AttackType.SCISSORS:
            self.computer_scissors_attack.draw()

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("Appuyer sur une image, puis espace pour faire une attaque", 75, 450, arcade.color.BLACK,
                             20, bold=True)

        if self.game_state == GameState.ROUND_DONE:
            arcade.draw_text(f"{self.gagnant_round} a gagne le round", 200, 450, arcade.color.BLACK, 25, bold=True)

        if self.game_state == GameState.GAME_OVER:
            arcade.draw_text(f"La partie est terminer, {self.gagnant_partie} a gagne", 125, 450, arcade.color.BLACK, 25,
                             bold=True)

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        self.rock.on_update(delta_time)
        self.paper.on_update(delta_time)
        self.scissors.on_update(delta_time)

        if self.game_state == GameState.ROUND_ACTIVE and self.flag == True:
            pc_attack = randint(0, 2)
            if pc_attack == 0:
                self.computer_attack = AttackType.ROCK
            elif pc_attack == 1:
                self.computer_attack = AttackType.PAPER
            else:
                self.computer_attack = AttackType.SCISSORS

            # pointage
            if self.player_attack == AttackType.ROCK:
                if self.computer_attack == AttackType.ROCK:
                    self.gagnant_round = "Egalite, personne n'"
                    self.game_state = GameState.ROUND_DONE

                elif self.computer_attack == AttackType.PAPER:
                    self.gagnant_round = "L'ordinateur"
                    self.computer_points += 1
                    self.game_state = GameState.ROUND_DONE

                elif self.computer_attack == AttackType.SCISSORS:
                    self.gagnant_round = "Le joueur"
                    self.player_points += 1
                    self.game_state = GameState.ROUND_DONE

            if self.player_attack == AttackType.PAPER:
                if self.computer_attack == AttackType.ROCK:
                    self.gagnant_round = "Le joueur"
                    self.player_points += 1
                    self.game_state = GameState.ROUND_DONE

                elif self.computer_attack == AttackType.PAPER:
                    self.gagnant_round = "Egalite, personne n'"
                    self.game_state = GameState.ROUND_DONE

                elif self.computer_attack == AttackType.SCISSORS:
                    self.gagnant_round = "L'ordinateur"
                    self.computer_points += 1
                    self.game_state = GameState.ROUND_DONE

            if self.player_attack == AttackType.SCISSORS:
                if self.computer_attack == AttackType.ROCK:
                    self.gagnant_round = "L'ordinateur"
                    self.computer_points += 1
                    self.game_state = GameState.ROUND_DONE

                elif self.computer_attack == AttackType.PAPER:
                    self.gagnant_round = "Le joueur"
                    self.player_points += 1
                    self.game_state = GameState.ROUND_DONE

                elif self.computer_attack == AttackType.SCISSORS:
                    self.gagnant_round = "Egalite, personne n'"
                    self.game_state = GameState.ROUND_DONE

        if self.player_points == 3:
            self.gagnant_partie = "le joueur"
            self.game_state = GameState.GAME_OVER

        if self.computer_points == 3:
            self.gagnant_partie = "l'ordinateur"
            self.game_state = GameState.GAME_OVER

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
        if key == arcade.key.SPACE and self.game_state == GameState.NOT_STARTED:
            self.flag = True
            self.game_state = GameState.ROUND_ACTIVE

        if key == arcade.key.SPACE and self.game_state == GameState.ROUND_DONE:
            self.flag = True
            self.game_state = GameState.ROUND_ACTIVE

        if key == arcade.key.SPACE and self.game_state == GameState.GAME_OVER:
            self.flag = True
            self.player_points = 0
            self.computer_points = 0
            self.game_state = GameState.ROUND_ACTIVE

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
        if self.rock.collides_with_point((x, y)):
            self.player_attack = AttackType.ROCK

        if self.paper.collides_with_point((x, y)):
            self.player_attack = AttackType.PAPER

        if self.scissors.collides_with_point((x, y)):
            self.player_attack = AttackType.SCISSORS

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
