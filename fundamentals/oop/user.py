# create a user class with specified attributes and methods
import inspect

class user():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        # method to print user info
        for key, val in self.__dict__.items():
            print(key+": "+str(val))
    def enroll(self):
        # method to enroll user in rewards program, checks if already enrolled
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points += 200
            return True
        else:
            print('User already a gold card rewards member.')
            return False
    def spend_points(self, amount):
        # method to spend rewards points
        if self.is_rewards_member:
            if self.gold_card_points >= amount:
                self.gold_card_points -= amount
            else:
                print('Spend amount greater than User\'s gold card balance')
        else:
            print('User is not a gold card rewards member.')


# test example to show functionality of user class
elmer = user('Elmer', 'Fudd', 'elmer@fuddindustries.com', 35)

elmer.display_info() # print original instance of user elmer
elmer.spend_points(40) # shows cannot spend if not a rewards member
elmer.enroll() # enroll elmer in gold card rewards program
elmer.enroll() # show that elmer cannot enroll twice
elmer.enroll() # it doesn't matter how many more times he tries, still can only enroll once
elmer.spend_points(50) # elmer spends 50 points on supplies

bugs = user('Bugs', 'Bunny', 'bbunny2@gmail.com', 12)

bugs.enroll()
bugs.spend_points(800) # user bugs cannot spend more points than he has
bugs.spend_points(80)

elmer.display_info() # print information for updated instance of user elmer
bugs.display_info() # print information for updated instance of user bugs