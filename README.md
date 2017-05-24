# Tournament Results

Full Stack Nanodegree Program Project 4. Tasked with creating a database schema based on Postgres SQL and Python. Languages used in this were Python 2.7 and SQL.

## Getting Started

Clone this repository by typing `git clone https://github.com/bryancresswell/tournamentResults.git`

## Testing

To test the app, simply connect to the vagrant machine by first typing `vagrant up`, then `vagrant ssh`. Navigate to your \vagrant directory with `cd \vagrant`. Once done, set up the database by first typing `psql`, then `\i tournament.sql`. After which, type `python tournament.py` which will show you the output and results of the test.

## Lessons Learnt

I tried to prevent SQL injection via the use of query parameters, which was interesting for me as I never thought much about SQL injections, although they are frequently heard of in the cyber security scene. Toying around with databases allows me to understand the importance of having well thought out normalized tables, as well as aiding in my overall problem solving skills. This was a fun project to undertake in general.
