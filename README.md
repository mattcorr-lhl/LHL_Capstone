# Formula 1 Data Analysis - LHL Capstone Project

## Project/Goals

The aim of this project was to apply my data analysis skills towards a personal interest of mine, Formula 1 (F1). F1 is a motorsport with an extensive history and engineering focus, as a result there has been enormous amounts of data accumulated over the years to analyze. The goal of my project was to determine who was the most dominant driver/team pairing over the course of the History of F1 while also taking a look at some of the factors that make them so successful.

**Live Visualizations can be found on Tableau Public** (or see `.twbx` file included above):
- [Formula 1 - Constructor Statistics](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-TeamStatistics/TeamStatistics?)
- [Formula 1 - Driver Career Statistics](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-DriverCareerStatistics/DriverStatistics)
- [Formula 1 - Exploratory Analysis](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-ExploratoryAnalysis/EDA)

## Process

All of the data for this project was sourced from the [Ergast API](http://ergast.com/mrd) (unfortunatly it is being deprecated EOY 2024). Ergast contains extensive data on the entire history of F1, with columns such as pitstop duration, 500,000 lap time records and much more.

#### EDA

- Once I had downloaded all of the data, the first thing I noticed was the use of the `\N` character to signify a null value. This would obviously break many calculations that rely on number calculations. To remove these I utilized the popular Python library [Pandas](https://pandas.pydata.org/), loaded the data into a DataFrame and then used the `.replace()` function to remove these values from the 14 tables (see `python_scripts/fix_nulls.py`).

- Thankfully Ergast maintains high data integrity so I was not left with any missing data. However I did note that the older races did not have nearly as much information recorded about their sessions. As a results I decided focus on the periods from 2000 to 2022 (as the 2023 season has not been completed yet).

- When creating calculations such as # of points I will make sure to take the number of races run (or number of laps) into consideration. This will help normalize the data, almost like the "per capita" calculations in my last project [Cause of Death Analysis with Tableau](https://github.com/mattcorr-lhl/Causes-of-Death-Tableau-Analysis)

#### Creating the Visualizations
- Once I had the data in Tableau I had to start relating the tables together, which proved quite difficult as Tableau is limited to a star structure, meaning I was unable to recreate the [ERD suggested by Ergast](http://ergast.com/images/ergast_db.png). However thankfully I was able to get around this for the most part using a mix of joins and calculated fields.

- The first visualizations I made were some line charts that attempted to correlate various columns to see if I could notice any patterns, see the [Formula 1 - Exploratory Analysis](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-ExploratoryAnalysis/EDA) dashboard for the visuals that I created. I provide my interpretations in the [results](#results) section.

## Results

After my analysis I think it's safe to say that **Lewis Hamilton** is the undisputed greatest driver from the 21st century. I came to this conclusion not only through simple statistics such as that he is the leader in total number of points scored (which theoretically any skilled can achieve if they race long enough with a decent team) but also a wide range of other facts including:

- Risk Aversion - How likely is the driver to get in a collision
- Podium % - How likely is the driver to end up on the podium (1st, 2nd or 3rd)
- Win % - How likely is the driver to get first place (# of wins / number of races)
- Points per Lap - How many points has the driver gotten per number of laps run. This statistic is a good indicator of a drivers performance 

Lewis tops all of the mentioned statistics above as well as many others that I did not cover. However it is worth noting that in Formula 1 the performance of a driver is heavily tied to the performance of their team, much more so than other sports as they not only provide the crew, but the car itself. Even the best driver would not be able to perform with a car that is not able to keep up. To view the relative performance of a team over a given range of years you can utilize the [Formula 1 - Constructor Statistics](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-TeamStatistics/TeamStatistics?) dashboard. It also contains a Gantt chart that allows you to view how long a team has been active for, sorted by most years in the sport.

Some other interesting trends I noticed while looking at the data include (see [Formula 1 - Exploratory Analysis](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-ExploratoryAnalysis/EDA)):
  - Straight line top speed doesn't increase much from year to year. I hypothesize this is due to the fact that production cars had already broken the 300km/h speed limit by 1986 such as the [Ferrari F40](https://en.wikipedia.org/wiki/Ferrari_F40) with a top speed of 367 km/h. The real modern engineering feats around F1 are dramatically improved cornering speeds through the use of advanced aerodynamics, suspension and tire composition.
  
  - The fastest lap of the race tends to occur right at the end of the Grand Prix as the cars have burned through most of their fuel, making them much lighter and thus improve on lap time.
  
  - Pitstop duration has minimal correlation to the lap in which the stop is performed.

  - Your starting position from qualifying heavy impacts where you will finish the race. Which obviously makes sense as the farther back you start, the more cars you will have to jockey with to make your way to the front.

  - On average, the first lap of a Grand Prix is significantly slower than the laps that follow. This can be attributed to the fact 

## Challenges

- I believed that the formatted `.csv` database export provided from Ergast's Database Images would have been the simpler solution but instead up being much more cumbersome as the data was heavily normalized and was split across 14 tables.
  
- [Ergast](http://ergast.com/mrd) considers each change of team name as a "new" team. In Formula 1 teams are frequently rebranded without a change in factory, car or staff (e.g. Toro Rosso switched to Alpha Tauri in 2020; Renault switched to Alpine in 2021). This made it much harder to track a given teams performance over the years while also causing some unsightly visuals.

## Future Goals

- As I alluded to in my first challenge, I would like to gather the data utilizing the API instead of the premade `.csv` images. This give me much greater detail over which data I wanted to pull down and in my specified format.

- Once switched over to the API, it would be interesting to see if I could get the Python run API calls to trigger every time a new race finishes so the data keeps up with the current season as it progresses.