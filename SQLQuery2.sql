-- PERCENTAGE OF DEATH IN ASIA  -- 

SELECT
location,
continent, 
Max(total_deaths) as Highestdeaths,
Max (cast(total_deaths as int)/ population)*100 As Percentageofdeaths
FROM [COVID REPORT]
WHERE continent like '%Asia%'
GROUP BY Location,continent
ORDER BY Percentageofdeaths DESC

