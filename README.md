# Welcome to Qatar2022Soccer project
Goal of the project is to determine a probable winner of world cup playing with Fifa Ranking of the teams.

## Download & Install
```
python3 -m venv .
pip3 install -r requirements.txt
pip install --upgrade pip
```

## How to run?
```
python3 qwc.py -t <number of times to run simulation> -p <minimum different of points to determimne a winner>
```

## How it works?
It will run the simulation a number of times that the -r parameter will indicate. Another parameter is the number of points. If the difference between two teams is bigger than this number in the FIFA ranking, the best one will win. Otherwise the system will randomly select one winner between the two.

## Stats on SQLite
```sql
SELECT first_place,
       100* (cast(COUNT(*) as real))/ (SELECT cast(COUNT(*) as real) FROM simulation) AS percentage
FROM simulation
GROUP BY first_place
ORDER BY 2 DESC;
```

# Sources
- [Fifa Ranking](https://www.fifa.com/fifa-world-ranking/men?dateId=id13750)
- [https://medium.com/the-football-pub/predicting-football-match-outcomes-with-python-the-understat-package-c72f24c2d717](https://medium.com/the-football-pub/predicting-football-match-outcomes-with-python-the-understat-package-c72f24c2d717)



