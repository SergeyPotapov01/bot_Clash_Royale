from keras.models import load_model

import cv2
import numpy as np


class CardInBatlle:
    def __init__(self):
        self.model = load_model('neural_networks/card_in_batlle.h5')
        self.class_names = ['Archer_Queen', 'Archers', 'Arrows', 'Baby_Dragon', 'Balloon', 'Bandit', 'Barbarian_Barrel',
                            'Barbarian_Hut', 'Barbarians', 'Bats', 'Battle_Healer', 'Battle_Ram', 'Bomb_Tower', 'Bomber',
                            'Bowler', 'Cannon', 'Cannon_Cart', 'Clone', 'Dark_Prince', 'Dart_Goblin', 'Earthquake',
                            'Electro_Dragon', 'Electro_Giant', 'Electro_Spirit', 'Electro_Wizard', 'Elite_Barbarians',
                            'Elixir_Collector', 'Elixir_Golem', 'Executiomer', 'Fire_Spirit', 'Fireball', 'Firecracker',
                            'Fisherman', 'Flying_Machine', 'Freeze', 'Furnace', 'Gaint_Skeleton', 'Giant', 'Giant_Snowball',
                            'Goblin_Barrel', 'Goblin_Cage', 'Goblin_Drill', 'Goblin_Gang', 'Goblin_Giant', 'Goblin_Hut',
                            'Goblins', 'Golden_Knight', 'Golem', 'Graveyard', 'Guards', 'Heal_Spirit', 'Hog_Rider',
                            'Hunter', 'Ice_Golem', 'Ice_Spirit', 'Ice_Wizard', 'Inferno_Dragon', 'Inferno_Tower',
                            'Knight', 'Lava_Hound', 'Lightnimg', 'Lumberjack', 'Magic_Archer', 'Mega_Knight', 'Mega_Minion',
                            'Miner', 'Mini_PEKKA', 'Minion_Horde', 'Minions', 'Mortar', 'Mother_Witch', 'Musketeer',
                            'Night_Witch', 'Pekka', 'Poison', 'Prince', 'Princess', 'Rage', 'Ram_Rider', 'Rascals',
                            'Rocket', 'Royal_Delivery', 'Royal_Ghost', 'Royal_Giant', 'Royal_Hogs', 'Royal_Recruits',
                            'Skeleton_Army', 'Skeleton_Barrel', 'Skeleton_Dragons', 'Skeleton_King', 'Skeletons',
                            'Sparky', 'Spear_Goblins', 'Tesla', 'The_Log', 'Three_Musketeers', 'Tombstone', 'Tornado',
                            'Valkyrie', 'Wall_Breakers', 'Witch', 'Wizard', 'X-Bow', 'Zap', 'Zappies', 'МУСОР']

    def predict(self, image):
        image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGBA2RGB)
        image = image.astype("float") / 255.0
        image = image.reshape(1, 2184)
        prediction = self.model.predict(image)
        prediction = np.argmax(prediction)
        return self.class_names[prediction]


class ElixirInBatlle:
    def __init__(self):
        self.model = load_model('neural_networks/Elixir.h5')
        self.class_names = ['0', '1', '10', '2', '3', '4', '5', '6', '7', '8', '9', 'МУСОР']
        self.elixir = 0

    def predict(self, image):
        image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGBA2RGB)
        image = image.astype("float") / 255.0
        image = image.reshape(1, 840)
        prediction = self.model.predict(image)
        prediction = np.argmax(prediction)
        try:
            self.elixir = int(self.class_names[prediction])
        except ValueError:
            pass

        return self.elixir


class Chest:
    def __init__(self):
        self.model = load_model
        self.class_names = ['Emptiness', 'Silver_Chest', 'Golden_Chest', 'Giant_Chest', 'Magical_Chest',
                            'Mega_Lightning_Chest', 'Epic_Chest', 'Legendary_Chest', 'Royal_Wild_Chest',
                            'Gold_Crate', 'Plentiful_Gold_Crate', 'Overflowing_Gold_Crate']


    def predict(self, image):
        image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGBA2RGB)
        image = image.astype("float") / 255.0
        image = image.reshape(1, 2184)
        prediction = self.model.predict(image)
        prediction = np.argmax(prediction)
        return self.class_names[prediction]