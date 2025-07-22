class Head():
    def __init__(self):
        pass



class Torso():
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm



class Arm():
    def __init__(self, hand):
        self.hand = hand



class Hand():
    def __init__(self):
        pass



class Leg():
    def __init__(self, foot):        
        self.foot = foot



class Feet():
    def __init__(self):
        pass


class Human():
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg

#Upper body
head = Head()
right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
torso = Torso(head, right_arm, left_arm)

#Lower body
right_foot = Feet()
left_foot = Feet()
right_leg = Leg(right_foot)
left_leg = Leg(left_foot)

# Torso already has the head and both arms attached, both armas already have hands attached to them.
# Each leg already has its corresponding foot attached to it. Hence, Creating the object Human already should have all the body parts.
human = Human(torso, right_leg, left_leg)


