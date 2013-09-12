"""

Hey there, my name is Devon. If you're reading this,
you're probably looking to learn a little bit about what I've done.

In this directory, you can find solutions that I've written,
in Python, to a lot of the problems found in
Cracking the Coding Interview (4e) by the folks at CareerCup.com

In this file, I've done something a little different. I've written
a Python class that does a pretty good job of defining me.

It's got some academic stuff, some professional details,
as well as a number of personal facts about me.

"""

import datetime

class Devon(Student):
    def __init__(self):
        self.hometown = "Columbus, OH"
        self.age = 21
        super().__init__(university="USC", graduation="May, 2014")
        self.internships = {
            'summer_2013' : ["Apple", "Software Engineering Intern - OS X Product Release"]
            'spring_2013' : ["Riot Games", "Community Intern"]
            'fall_2012' : ["Riot Games", "Community Intern"]
            'summer_2012' : ["Sony Electronics", "Software Engineering Intern - Television"]
            'spring_2012' : ["Riot Games", "Web Content Intern"]
            'fall_2011' : ["Sony Pictures Entertainment", "IT/Business Analyst Intern"]
            'summer_2011' : ["Abbott Laboratories", "Engineering Intern"]
            }
        self.interests = [
            "Video Games",
            "Television",
            "Film",
            "Philosophy",
            "Good Tea, good coffee",
            "Tech News",
            "Side Projects",
            "The web"
            ]
        self.favorites = {
            "TV Show" : "Breaking Bad",
            "Film" : "Lord of the Rings: Return of the King",
            "Band" : "Mumford & Sons",
            "Game" : "Super Smash Brothers: Brawl"
            }