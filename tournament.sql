-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
\c tournament

CREATE TABLE players (
        playerID serial UNIQUE PRIMARY KEY,
        playerName text,
        wins int DEFAULT 0,
        loss int DEFAULT 0,
        matchesPlayed int DEFAULT 0
        );
CREATE TABLE matches (
        matchID serial UNIQUE PRIMARY KEY,
        winner serial,
        loser serial,
        FOREIGN KEY (winner) REFERENCES players (playerID),
        FOREIGN KEY (loser) REFERENCES players (playerID)
        );
