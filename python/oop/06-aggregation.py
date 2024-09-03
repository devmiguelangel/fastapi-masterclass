"""
Aggregation

Aggregation represents a whole-part relationship where one object (the whole) contains references to other objects (the parts). However, these parts can exist independently of the whole.
It's a weaker form of composition where the child objects do not necessarily cease to exist when the parent object is destroyed.
This allows for more flexible and loosely-coupled designs, as it models scenarios where objects have their own life cycle and can be shared among different parent objects.

Step-by-step Example:
1. Define Simple Classes for Components: We'll create a Player class that represents a player.
2. Define a Class that Uses Aggregation: We'll create a Team class that aggregates Player objects. The Player objects can exist independently of the Team.
"""

# Step 1: Define a Simple Class for Components
class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# Step 2: Define a Class Using Aggregation
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(f'{player.get_name()} added to team {self.team_name}')

    def remove_player(self, player):
        self.players.remove(player)
        print(f'{player.get_name()} removed from team {self.team_name}')

    def display_players(self):
        print(f'Players in team {self.team_name}:')
        for player in self.players:
            print(player.get_name())

# Create player objects
player1 = Player('Alice')
player2 = Player('Bob')
player3 = Player('Charlie')

# Create a team object
team = Team('Team A')
team.add_player(player1)
team.add_player(player2)

team.display_players()

team.remove_player(player1)

# Player objects can exist independently of the team
print(player1.get_name())
print(player2.get_name())
print(player3.get_name())
