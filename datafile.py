#!/usr/bin/python3
#Alex Jordan
#1/28/2020


import pickle

games = { 1 :['FPS', 'Halo 3', 'Bungee', 'Microsoft', 'Xbox 360', '2007', '10', 'either', '30.00', 'yes', '1/15/2008',
         'This game blows chunks!']}

datafile = open("game_lib.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()

