# xwOBA-Model

I am trying to design a model that can predict the wOBA value for balls in play using batted ball characteristics. Previously, tests for xwOBA have been done for both the MLB (https://technology.mlblogs.com/an-introduction-to-expected-weighted-on-base-average-xwoba-29d6070ba52b) as well as the KBO (https://benhowell71.com/introducing-kbo-xwoba-and-xwobacon/). When the Baseball Data Machine Learning team created their formula, they used weights for each outcome based on FanGraphs data, but then created their own model for determining xwOBAcon using exit velocity, launch angle, and sprint speed. Similarly, Ben Howell’s study in the KBO used the same formula, but he used R to get values more suitable for the KBO based on the MLB values. He also used contact, batted ball type, and direction to categorize hits and determined wOBA for each combination of contact and batted ball type.
In order to create this model, I will be using Statcast data on exit velocity and launch angle, as well as for balls in play and classification of outs, singles, and so on. Additionally, I will be using the MLB’s FanGraph weighted values to help calculate the wOBA. 
It might be helpful in this project to have a non-constant weight in regards to sprint speed, as the outcomes of certain balls in play will not be affected by a player’s speed. It also is important to note that the MLB made multiple major rule changes before this season, and these could possibly affect the weights of each outcome. Otherwise, there are not many risks or assumptions with this data. 
In order to create a model for xwOBA, I will need to construct a model for xwOBAcon. This will use data for exit velocity and launch angle in order to predict the xwOBA for a batted ball. For modeling, I am unsure of what might be the best approach, but I could possibly use a neural network or other machine learning technique.
To begin, I created a dataframe that only included data from 2020-2022. This encapsulates a sufficient amount of recent data, while also being prior to the 2023 rule changes. Since I am trying to create a model for xwOBAcon, I dropped any pitch that didn't result in a ball in play. Next, I dropped any balls in play that did not have values for "launch_speed" or "launch_angle," as they wouldn't be able to be used in the model. I also consolidated every non-hit outcome to just be labeled "out" and dropped the catcher's interference outcomes as a whole because the swings were interfered with. I then made a plot of the values with LS on the x-axis and LA on the y-axis. The color of the points corresponds to the type of ball in play.

![](Initial_Graph.png)

As seen above, while not exact, there are some clear values where we can predict the outcome of a batted ball, but I want to design a model that can do so more accurately. To do this, I used the k-Nearest Neighbors method of machine learning. First, I scaled the data in order to account for using euclidean distance, By using launch angle and launch speed values and euclidean distance for a neighborhood of 23 values, it could predict the outcome correctly with over 76% accuracy.
I then used the log loss parameter to evaluated my model's performance. The result was just over 1, so while it isn't bad, I also knew there was most likely a better method to use. However, I continued with my KNN model and created calibration curves for each of the 5 possible outcomes to determine where there could be possible over/under fitting.
After the calibration curves were constructed, I then moved to the Random Forest model. I used "log_loss" as my criterion in order to stay consistent with my work for the KNN model, and tried a few different max depths before deciding that 7 was the optimal number to give accurate, but not overfitted predictions.This model got a slightly higher accuracy score (over 77%), but this was not the only way I wanted to compare the models. I then used the log loss parameter for the Random Forest and got a value of just above .59, a large improvement over the results from the KNN log loss result. I also constructed a confusion matrix for the Random Forest model and made some analysis on why these results would make sense. To finish the Random Forest analysis, I created another calibration curve for each possible outcome, all of which were improvements over the KNN calibration curves. 
Lastly, I used my model to show the comparison of xwOBA to actual outcomes in a dataframe by using FanGraphs' values for wOBA. I multipled the probability of each outcome by their respective values and then summed them to give an xwOBA reading for each ball in play. This concluded with a recreation of the graph from earier, but this time with xwOBA as the color map, as shown below.

![](xwOBA_Graph.png)