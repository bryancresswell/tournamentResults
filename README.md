# Tournament Results

Full Stack Nanodegree Program Project #4. Tasked with creating a database schema based on Postgres SQL and Python. Languages used in this were Python 2.7 and SQL.

## Getting Started

Clone this repository by typing `git clone https://github.com/bryancresswell/tournamentResults.git`

## Launching Vagrant

Once you have installed [Vagrant](vagrantup.com), clone the Full Stack Nanodegree files from [here](https://github.com/udacity/fullstack-nanodegree-vm). Once done, navigate to the folder, then type `vagrant up`. Once ready, type `vagrant ssh` which will connect you to the VM.

## Setting up the database

Once you are connected in the VM, type `cd /vagrant` to change to the current directory. You should see `vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$`. This will be where you enter your commands. To quickly set up the database, just type `psql -f tournament.sql`. This will automatically create the "tournament" database.

## Testing

Once the database is created (which you can check by using `\dt` in the `psql` shell), you are all ready to test the app! To test, type `python tournament_test.py` which will show you the output and results of the test.

## Lessons Learnt

I tried to prevent SQL injection via the use of query parameters, which was interesting for me as I never thought much about SQL injections, although they are frequently heard of in the cyber security scene. Toying around with databases allows me to understand the importance of having well thought out normalized tables, as well as aiding in my overall problem solving skills. This was a fun project to undertake in general.
