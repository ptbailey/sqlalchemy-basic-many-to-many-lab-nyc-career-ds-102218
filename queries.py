from models import *

def return_christian_bales_roles(session):
    return (session.query(Actor).filter(Actor.name == "Christian Bale").one()).roles
    # Return a list of Christian Bale role instances

def return_catwoman_actors(session):
    return (session.query(Role).filter(Role.character == 'Catwoman').one()).actors
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors(session):
    return len((session.query(Role).filter(Role.character == 'Batman').one()).actors)
    # Return the number of actors that have played Batman
