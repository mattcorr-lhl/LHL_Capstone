# Formula 1 Data Analysis - LHL Capstone Project

## Project/Goals

The aim of this project was to apply my data analysis skills towards a personal interest of mine, Formula 1 (F1). F1 is a motorsport with an extensive history and engineering focus, as a result there has been enormous amounts of data accumulated over the years to analyze. The goal of my project was to determine who was the most dominant driver/team pairing over the course of the History of F1 while also taking a look at some of the factors that make them so successful.

## Process

All of the data for this project was sourced from the [Ergast API](http://ergast.com/mrd) (unfortunatly it is being deprecated EOY 2024). Ergast contains extensive data on the entire history of F1, with columns such as pitstop duration, 500,000 lap time records and much more.

#### EDA

- Once I had downloaded all of the data, the first thing I noticed was the use of the `\N` character to signify a null value. This would obviously break many calculations that rely on number calculations. To remove these I utilized the popular Python library [Pandas](https://pandas.pydata.org/), loaded the data into a DataFrame and then used the `.replace()` function to remove these values from the 14 tables (see `python_scripts/fix_nulls.py`).

- Some interesting trends I noticed while looking at the data include (see [Formula 1 - Exploratory Analysis](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-ExploratoryAnalysis/EDA)):
  - Straight line top speed doesn't increase much from year to year. This is because production cars had already broken the 300km/h speed limit by 1986, such as the [Ferrari F40](https://en.wikipedia.org/wiki/Ferrari_F40) with a top speed of 367 km/h. The real modern engineering feats around F1 are dramatically improved cornering speeds through the use of advanced aerodynamics, suspension and tire composition.
  - The fastest lap of the race tends to occur right at the end of the Grand Prix as the cars have burned through most of their fuel, making them much lighter and thus take corners better.
  - 

#### Visualizations
- 

## Results

Dashboards (hosted on Tableau Public):
- [Formula 1 - Constructor Statistics](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-TeamStatistics/TeamStatistics?)
- [Formula 1 - Driver Career Statistics](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-DriverCareerStatistics/DriverStatistics)
- [Formula 1 - Exploratory Analysis](https://public.tableau.com/app/profile/matthew.corr6019/viz/Formula1-ExploratoryAnalysis/EDA)

After my analysis I think it's safe to say that **Lewis Hamilton** is the undisputed greatest driver from the 21st century (up until 2022 at least, currently the 2023 season is being dominated by Max Verstappen & Red Bull). I came to this conclusion not only through simple statistics such as total number of points (which theoretically any skilled can achieve if they race long enough with a decent team) but also more nuanced statistics such as
- Risk Aversion - How likely is the driver to get in a collision
- Podium % - How likely is the driver to end up on the podium (1st, 2nd or 3rd)
- Win Rate - Per race
- Points per Lap - 

## Challenges

- I believed that the formatted `.csv` database export provided from Ergast's Database Images would have been the simpler solution but instead up being much more cumbersome as the data was heavily normalized and was split across 14 tables.
  
- [Ergast](http://ergast.com/mrd) considers each change of team name as a "new" team. In Formula 1 teams are frequently rebranded without a change in factory, car or staff (e.g. Toro Rosso switched to Alpha Tauri in 2020; Renault switched to Alpine in 2021). This made it much harder to track a given teams performance over the years while also causing some unsightly visuals.

## Future Goals

- As I alluded to in my first challenge, I would like to gather the data utilizing the API instead of the premade `.csv` images. This give me much greater detail over which data I wanted to pull down and in my specified format.

- Once switched over to the API, it would be interesting to see if I could get the Python run API calls to trigger every time a new race finishes so the data keeps up with the current season as it progresses.