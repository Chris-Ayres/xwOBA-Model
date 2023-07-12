# xwOBA-Model

I am trying to design a model that can predict the wOBA value for balls in play using batted ball characteristics. 
Previously, tests for xwOBA have been done for both the MLB (https://technology.mlblogs.com/an-introduction-to-expected-weighted-on-base-average-xwoba-29d6070ba52b) 
as well as the KBO (https://benhowell71.com/introducing-kbo-xwoba-and-xwobacon/). When the Baseball Data Machine Learning team created their 
formula, they used weights for each outcome based on FanGraphs data, but then created their own model for determining xwOBAcon using exit 
velocity, launch angle, and sprint speed. Similarly, Ben Howell’s study in the KBO used the same formula, but he used R to get values more 
suitable for the KBO based on the MLB values. He also used contact, batted ball type, and direction to categorize hits and determined wOBA for 
each combination of contact and batted ball type.
In order to create this model, I will be using Statcast data on exit velocity, launch angle, and player sprint speed, as well as for any other 
player stats I might need throughout the process. Additionally, I will be using the MLB’s FanGraph weighted values to help calculate the wOBA. 
It might be helpful in this project to have a non-constant weight in regards to sprint speed, as the outcomes of certain balls in play will not 
be affected by a player’s speed. It also is important to note that the MLB made multiple major rule changes before this season, and these could 
possibly affect the weights of each outcome. Otherwise, there are not many risks or assumptions with this data. In order to create a model for 
xwOBA, I will need to construct a model for xwOBAcon. This will use data for exit velocity, launch angle, and sprint speed (in some cases) in 
order to predict the xwOBA for a batted ball. For modeling, I am unsure of what might be the best approach, but I could possibly use a neural 
network or other machine learning technique.

To begin, I created a dataframe that only included data from 2020-2022. This encapsulates a sufficient amount of recent data, while also being 
prior to the 2023 rule changes. Since we are trying to create a model for xwOBAcon, I dropped any pitch that didn't result in a ball in play. Next, 
I dropped any balls in play that did not have values for "launch_speed" or "launch_angle," as they wouldn't be able to be used in our model. I
then made a plot of the values with LS on the x-axis and LA on the y-axis. The color of the points corresponds to the type of ball in play.

*insert graph*

As seen above, while not exact, there are some clear values where we can predict the outcome of a batted ball, but we want to design a model that
can do so more accurately. To do this, I used the k-Nearest Neighbors method of machine learning. By using launch angle and launch speed values and
euclidean distance for a neighborhood of 23 values, it could predict the outcome correctly with over 68% accuracy.
