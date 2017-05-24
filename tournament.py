#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import re


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    table = "matches"
    playerTable = "players"
    c.execute("DELETE FROM %s;" % (table,))
    # UPDATE statement is to reset all values to default after deleting all
    # rows from matches table
    c.execute("""UPDATE %s SET wins = 0, 
        loss = 0, matchesPlayed = 0""" % (playerTable,))
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    table = "players"
    c = conn.cursor()
    c.execute("DELETE FROM %s;" % (table,))
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    table = "players"
    c = conn.cursor()
    c.execute("SELECT COUNT(playerID) FROM %s;" % (table,))
    result = c.fetchone()[0]
    conn.commit()
    conn.close()
    return result

def registerPlayer(name):                                                                   
    """Adds a player to the tournament database.                                            
    The database assigns a unique serial id number for the player.  (This                   
    should be handled by your SQL database schema, not in your Python code.)                
                                                                                            
    Args:                                                                                   
      name: the player's full name (need not be unique).                                    
    """                                                                                     
    conn = connect()                                                                        
    c = conn.cursor()                                                                       
    # Regex is used here for instances where we might have apostrophes in one's             
    # name                                                                                  
    c.execute("INSERT INTO players (playerName) VALUES ('{}')".format(                      
        re.sub(r'\'', '', name)));                                                          
    conn.commit()                                                                           
    conn.close()                                                                            
                                                                                            
def playerStandings():                                                                      
    """Returns a list of the players and their win records, sorted by wins.                 
                                                                                            
    The first entry in the list should be the player in first place, or a player            
    tied for first place if there is currently a tie.                                       
                                                                                            
    Returns:                                                                                
      A list of tuples, each of which contains (id, name, wins, matches):                   
        id: the player's unique id (assigned by the database)                               
        name: the player's full name (as registered)                                        
        wins: the number of matches the player has won                                      
        matches: the number of matches the player has played                                
    """                                                                                     
    conn = connect()                                                                        
    c = conn.cursor()                                                                       
    table = "players"                                                                       
    c.execute("""SELECT playerID,                                                           
        playerName,                                                                         
        wins,                                                                               
        matchesPlayed FROM %s ORDER BY wins DESC;""" % (table,))                            
    result = c.fetchall()                                                                   
    conn.commit()                                                                           
    conn.close()                                                                            
    return result                                                                           
                                                                                            
def reportMatch(winner, loser):                                                             
    """Records the outcome of a single match between two players.                           
                                                                                            
    Args:                                                                                   
      winner:  the id number of the player who won                                          
      loser:  the id number of the player who lost                                          
    """                                                                                     
    conn = connect()                                                                        
    c = conn.cursor()                                                                       
    # Inserts a row into the matches table, and updates subsequent data                     
    c.execute("""INSERT INTO matches (winner, loser)                                        
        VALUES ('%i', '%i')""" % (winner, loser))                                           
    c.execute("""UPDATE players SET wins = wins + 1,                                        
        matchesPlayed = matchesPlayed + 1                                                   
        WHERE playerID = %s""" % (winner,))                                                 
    c.execute("""UPDATE players SET loss = loss + 1,                                        
        matchesPlayed = matchesPlayed + 1                                                   
        WHERE playerID = %s""" % (loser,))                                                  
    conn.commit()                                                                           
    conn.close()                                                                            
                                                                                            
def swissPairings():                                                                        
    """Returns a list of pairs of players for the next round of a match.                    
                                                                                            
    Assuming that there are an even number of players registered, each player               
    appears exactly once in the pairings.  Each player is paired with another               
    player with an equal or nearly-equal win record, that is, a player adjacent             
    to him or her in the standings.                                                         
                                                                                            
    Returns:                                                                                
      A list of tuples, each of which contains (id1, name1, id2, name2)                     
        id1: the first player's unique id                                                   
        name1: the first player's name                                                      
        id2: the second player's unique id                                                  
        name2: the second player's name                                                     
    """                                                                                     
    conn = connect()                                                                        
    c = conn.cursor()                                                                       
    table = "players"                                                                       
    c.execute("""SELECT playerID,                                                           
        playerName FROM %s ORDER BY wins DESC;""" % (table,))                               
    result = c.fetchall()
    pairings = list()
    if (result % 2 != 0):
        return None
    else:                                                                   
    # For loop to simply pair up adjacent players based on                                  
    # already sorted value from the playerStandings() method                                
        for i in range(0, len(result), 2):                                                      
            tmpList = result[i:i+2]                                                             
            temp1 = tmpList[0]                                                                  
            temp2 = tmpList[1]                                                                  
            pairings.append((temp1[0], temp1[1], temp2[0], temp2[1]))                           
        return pairings   
    return None 