# xwOBA-Model

I am trying to design a model that can predict the wOBA value for balls in play using batted ball characteristics. 
Previously, tests for xwOBA have been done for both the MLB as well as the KBO. When the Baseball Data Machine Learning team created their formula, 
they used weights for each outcome based on FanGraphs data, but then created their own model for determining xwOBAcon using exit velocity, 
launch angle, and sprint speed. Similarly, Ben Howell’s study in the KBO used the same formula, but he used R to get values more suitable 
for the KBO based on the MLB values. He also used contact, batted ball type, and direction to categorize hits and determined wOBA for each 
combination of contact and batted ball type.
In order to create this model, I will be using Statcast data on exit velocity, launch angle, and player sprint speed, as well as for any other 
player stats I might need throughout the process. Additionally, I will be using the MLB’s FanGraph weighted values to help calculate the wOBA. 
It might be helpful in this project to have a non-constant weight in regards to sprint speed, as the outcomes of certain balls in play will not 
be affected by a player’s speed. It also is important to note that the MLB made multiple major rule changes before this season, and these could 
possibly affect the weights of each outcome. Otherwise, there are not many risks or assumptions with this data. In order to create a model for 
xwOBA, I will need to construct a model for xwOBAcon. This will use data for exit velocity, launch angle, and sprint speed (in some cases) in 
order to predict the xwOBA for a batted ball. For modeling, I am unsure of what might be the best approach, but I could possibly use a neural 
network or other machine learning technique.
