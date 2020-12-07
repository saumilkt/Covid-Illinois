# Week 3 #
__Progress__:
- We've consolidated all of the Data from August until Now
- We've figured out how the project is going to look. It will consist of:
  - A Main screen that shows a scatterplot of counties superimposed over Illinois. 
    - We can select between different metrics via dropdown and will have different colors to represent each
      - Metrics can include cases/deaths/case fatality ratio, and socioeconomic status comparisons as well
    - Severity of metrics is visualized through changes in hue and opacity
  - Mousing over each county will show a tooltip that contains basic stats, cases/deaths/case fatality ratio/socioeconomic status info
  - Clicking on a county will show more detailed county specific graphs, such as cases/deaths over time

__This Week's Objectives__
- Make graphs interactive by using an interactive plotting library such as MPLD3
- Gather socioeconomic status data for all counties
- Work with Rajat to transition project to being some sort of webapp

__Action Items for Week 3:__
- Make a scatterplot of Cases and Deaths of all Illinois counties using MPLD3: __Kai__
  > Note: This will likely require making separate graphs to account for Cook County (Chicago)'s outlier nature
- Make a scatterplot of Cases/Person and Death/Person of all Illinois counties using MPLD3: __Jimmy__
- Make Cases/Deaths/Case Fatility Ratio over time Plots for individual Counties using MPLD3: __Gabriel__
- Research Socioeconomic data for all Illinois counties, including median and avg. income, # of hospitals, population: __Saumil__




# Week 2 #
__Progress__:
- We have dataframes for all of days from the start of school to 10/31. 
- Most of the data only includes cases and deaths though, so we need to move to the more data-rich covid daily reports dataset
  - It can be found here: [https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports]

__This Week's Objectives:__
- Generate Dataframes *for all days starting from start of school to now* from the new dataset
- Brainstorm Ideas for how to Visualize the Data; during the meeting itself, we came up with a few:
  - Use scatterplot of counties' lat and longitude to overlay data over a map of illinois
  - If we are looking at data across time and only for 1 county, we should probably use a line plot
  - If we are looking at data across counties and only for a single time period/day, we should probably use a scatter plot
- Make Basic Visualizations on County Data to familiarize yourself with MatPlotLib and Pandas

__Action Items for Week 2:__
- Make Dataframes for Covid-Daily-Reports dataset if not done already: __Everyone__
- Brainstorm Ideas on How to Visualize Data: __Everyone__
- Make Basic Visualizations on County Data for Familiarize yourself with MPL/PD
  - Adams County - DeWitt County: __Gabriel__
  - Douglas County - Jackson County: __Jimmy__
  - Jefferson County - Madison County: __Kai__
  - Marion County - Richland County: __Ryan__
  - All remaining counties (Rock Island - Woodford): __Saumil__




#  Week 1 #

__Dataset:__ Johns Hopkins Covid Dataset

- [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)

__Objectives:__

- Focus on Illinois
  - Data to Analyze:
    - And and Organizing by County
    - Cities
    - Arrange by Median Income/ Socioeconomic status
    - Cases
  - Ideal Timeline:
    - Since school year started (august 24, 2020)

__Timeframe:__

- Week 1: Consolidate the Data
- Week 2: Visualize Data
- Week 3: Visualize Data
- Week 4: Superimposing over a Map of Illinois
- Future: Make it interactive

__Action Items for Week 1:__

- Make Dataframes for Each metric we want to test
  - August + Sept 1-15: Jimmy
  - Sept 15-Sept 30: Saumil
  - Oct 1- 15: Kai
  - Oct 15-31: Gabriel
  - Nov 1 till Now: Ryan
