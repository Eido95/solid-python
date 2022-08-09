# SRP The Single Responsibility Principle

# (2017) A module should be responsible to one, and only one, actor.
# model = class
# actor = who it's responsible to serve

# (2002) A class should have only one reason to change.
from abc import abstractmethod
from enum import Enum


class Team(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class Student:
    def __init__(self, name):
        self.name = name


class TeamMemberShipLookup:
    @abstractmethod
    def find_all_students_of_team(self, team):
        pass


class TeamMembership(TeamMemberShipLookup):
    def __init__(self):
        self.team_memberships = []

    def add_team_membership(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students_of_team(self, team):
        for members in self. team_memberships:
            if members [1] == team:
                yield members[0].name


class Analysis:
    def __init__(self, team_membership_lookup):
        for student in team_membership_lookup.find_all_students_of_team(Team.RED):
            print(f'{student} in red team')


student1 = Student('Student1')
student3 = Student('Student3')
team_membership = TeamMembership()
team_membership.add_team_membership(student1, Team.BLUE)
team_membership.add_team_membership(student3, Team.RED),
Analysis(team_membership)
