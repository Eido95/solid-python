# DIP: The Dependency Inversion Principle

# (2017) The most flexible systems are those in whichsource code
# dependencies refer only to abstractions, not to concretions.

# (2002)
# A. High-level modules should not depend on low-level modules.
# Both should depend on abstractions.
# B. Abstractions should not depend upon details.
# Details should depend upon abstractions

# (2000) Depend upon Abstractions. Do not depend upon concretions.
from enum import Enum


class Team(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class Student:
    def __init__(self, name):
        self.name = name


class TeamMembership:
    def __init__(self):
        self.team_memberships = []

    def add_team_membership (self, student, team):
        self.team_memberships.append((student, team))


class Analysis:
    def __init__(self, team_student_membership):
        memberships = team_student_membership.team_memberships
        for membership in memberships:
            if membership[1] == Team.RED:
                print(f'{membership[0].name} in red team')


student1 = Student("Student1")
student2 = Student("Student2")
team_membership = TeamMembership()
team_membership.add_team_membership(student1, Team.BLUE)
team_membership.add_team_membership(student1, Team.RED)
analysis = Analysis(team_membership)
