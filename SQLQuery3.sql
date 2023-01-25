--Pull out the global death and percentage of death vs population--

Select 
location,
population,
cast(total_deaths as int) / cast(total_cases as int) AS Percentageofdeaths
From [COVID REPORT]
ORDER by Percentageofdeaths Desc
