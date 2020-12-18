import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
CSV_FILE_PATH = "./data/train_V2.csv"
data = pd.read_csv(CSV_FILE_PATH)

# # ------------------------------------------------------
# # -              Basic info of the data                -
# # ------------------------------------------------------
# # Check the basic info of training dataset
# data.info()
#
# # Check the first 5 rows
# print(data.head(5))
#
# # Check the missing value of the dataset
# print(data.isnull().sum())
# print(data[data['winPlacePerc'].isnull()])
#
# # Drop row with NaN 'winPlacePerc' value
# data.drop(2744604, inplace=True)


# Some information of the game
Group = ['Id', 'groupId', 'matchId']
for item in Group:
    print('unique [{}] count {}:'.format(item, data[item].nunique()))

match_types = data.loc[:, "matchType"].value_counts().to_frame().reset_index()
match_types.columns = ["Type", "Count"]
print(match_types)
# Collect the type of game less than 1.7 thousand
Total = 0
# for count in match_types["Count"]:
#     Total += count
print(Total)
a = []
b = []
for typeName in match_types["Type"]:
    # print(typeName)
    a.append(typeName)
for count in match_types["Count"]:
    b.append(100*(count/(len(data)-1)))

for typeName, ratio in zip(a, b):
    print("{} : {:.4f}%".format(typeName, ratio))

# new_rows = ["Others", Total]
# match_types.loc[6] = new_rows
# print(match_types)


#
# # The plot of match types count
# plt.figure(figsize=(15, 8))
# sns.barplot(x="Type", y="Count", data=match_types[:7])
# plt.title("Match types Counts")
# plt.savefig('./image/Match types Counts.png')
# plt.show()
#
# # ------------------------------------------------------
# # -                    DATA Analysis                   -
# # ------------------------------------------------------
# # correlation matrix
# plt.subplots(figsize=(15, 15))
# sns.heatmap(data.corr(), square=True, annot=True, fmt='.3f', annot_kws={"size": 8}, cmap="RdBu_r", center=0)
# plt.savefig('./image/correlation matrix.png')
# plt.show()
#
#
# # ------------------------------------------------------
# # -                    Funny truth                     -
# # ------------------------------------------------------
# print(data['teamKills'].describe())
# print('The maximum of team kills is {number1}.'.format(number1=data['teamKills'].max()))
# print('The average of team kills is {number2}.'.format(number2=data['teamKills'].mean()))
# print('The minimum of team kills is {number3}.'.format(number3=data['teamKills'].min()))
# print("The longest kill distance {}".format(data["longestKill"].max()))
# print("The average kill distance {}".format(data["longestKill"].mean()))
#
# walk_distance = data.copy()
# walk_distance = walk_distance[walk_distance["kills"] > 0]
# print(len(walk_distance))
#
# # One type of cheater
# # Create new col call totalDistance
# new_data = data.copy()
# new_data['totalDistance'] = new_data['rideDistance'] + new_data['walkDistance'] + new_data['swimDistance']
# # Create col call killsWithoutMoving
# new_data['killsWithoutMoving'] = ((new_data['kills'] > 0) & (new_data['totalDistance'] == 0))
# print("The total number of kill without moving is {}"
#       .format(len(new_data[new_data['killsWithoutMoving'] == True])))
#
# # The plot of win distribution
# plt.title("Win  Distribution")
# sns.distplot(data['winPlacePerc'], kde=False)
# plt.savefig('./image/win distribution.png')
# plt.show()
#
# # ------------------------------------------------------
# # -                    Kill Analysis                   -
# # ------------------------------------------------------
# # Basic info of killer
# print(data['kills'].describe())
# print("The average of each team kills {:.4f} players, "
#       "99% of people have {} kills, the most kills number is {}."
#       .format(data['kills'].mean(), data['kills'].quantile(0.99), data['kills'].max()))
#
#
# # Plot of kill count
# kill_data = data.copy()
# kill_data.loc[kill_data['kills'] > kill_data['kills'].quantile(0.99)] = '7+'
# sns.countplot(kill_data['kills'].astype('str').sort_values())
# plt.title("Kills Count")
# plt.savefig('./image/kills count.png')
# plt.show()
#
#
# # Lucky boy
# kill_data2 = data.copy()
# kill_data2 = kill_data2[kill_data2['kills'] == 0]
# counts = len(kill_data2[kill_data2['winPlacePerc'] == 1])
# per = counts/len(kill_data2)
# print("There are {} players win the chicken without kill anyone, the percentage is {:.4f}% \n "
#       "(Total people who win the game without kill anyone / Total people who kill zero people in the game)"
#       .format(counts, 100*per))
#
# # People who is not that lucky
# print("----------------------------------")
# print("The number of player who kill 0 people {}, the percentage is {:.2f}% in all the people"
#       .format(len(kill_data2), 100*(len(kill_data2)/len(data))))
# print("----------------------------------")
# print("The number of player who kill 0 people and did 0 damage is {},"
#       " the percentage is {:.2f}% in all the people who kill 0 people"
#       .format(len(kill_data2[kill_data2["damageDealt"] == 0]),
#               100*(len(kill_data2[kill_data2["damageDealt"] == 0])/len(kill_data2))))
#
# # # Plot of Damage by 0 killers
# # kill_data4 = data.copy()
# # kill_data4 = kill_data4[kill_data4['kills'] == 0]
# # plt.title("Damage Dealt by 0 killers")
# # sns.displot(kill_data4['damageDealt'])
# # plt.show()
#
# # Plot of kill vs win
# sns.jointplot(x="winPlacePerc", y="kills", data=data, color='black')
# plt.title("Kills vs Win")
# plt.savefig('./image/kills vs. win.png')
# plt.show()

# kills1 = data.copy()
# kills1['killsCategories'] = pd.cut(kills1['kills'], [-1, 0, 2, 5, 10, 60], labels=['0_kills','1-2_kills', '3-5_kills', '6-10_kills', '10+_kills'])
# sns.boxplot(x='kills', y='winPlacePerc', data=kills1)
# plt.show()
#
# # Plot of DBNOs vs ratio
# plt.figure(figsize=(15, 5))
# sns.pointplot(x='DBNOs', y='winPlacePerc', data=data, alpha=0.8)
# plt.title('DBNOs VS Win Ratio')
# plt.grid()
# plt.savefig('./image/DBNOS vs Win.png')
# plt.show()
# #
# # Plot of DBNOs count
# plt.figure(figsize=(15, 8))
# kill_data3 = data.copy()
# kill_data3 = kill_data3[kill_data3['kills'] == 0]
# kill_data3.loc[kill_data3['DBNOs'] > 7] = '7+'
# sns.countplot(kill_data3['DBNOs'].astype('str').sort_values())
# plt.title("DBNOs Count")
# plt.savefig('./image/BDNOs count.png')
# plt.show()
#
# # The plot of damagedealt  vs win ratio
# # kill_data3 = data.copy()
# # kill_data3['damageDealt_rank'] = pd.cut(kill_data3['damageDealt'],
# #                                         [-1, 500, 1000, 1500, 2000, 2500, 60000],
# #                                         labels=['0-500', '500-1000', '1000-1500',
# #                                         '1500-2000', '2000-2500', '2500+'])
# #
# # sns.pointplot(x='damageDealt', y='winPlacePerc', data=kill_data3)
# # plt.xticks(rotation=45)
# # plt.title('damageDealt VS. Win Ratio')
# # plt.show()
#
# # The plot of damagedealt  vs win ratio
# data2 = data.copy()
# data2['damageDealt_rank'] = pd.cut(data2['damageDealt'],
#                                    [-1, 500, 1000, 1500, 2000, 2500, 60000]
#                                    , labels=['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500+'])
# f, ax1 = plt.subplots()
# sns.pointplot(x='damageDealt_rank', y='winPlacePerc', data=data2, alpha=0.8)
# plt.xlabel('damageDealtk')
# plt.xticks(rotation=45)
# plt.ylabel('Win Percentage')
# plt.title('damageDealt VS Win Ratio')
# plt.grid()
# plt.savefig('./image/damageDealt vs Win.png')
# plt.show()
# # ------------------------------------------------------
# # -                    Walk Analysis                   -
# # ------------------------------------------------------
# # Basic info of walker
#
# # Some facts about walking distance
# print(data['walkDistance'].describe())
#
# print("The average of each team walk for {:.2f} m, "
#       "99% of people have walk {} m, the most walking distance is {}m."
#       .format(data['walkDistance'].mean(), data['walkDistance'].quantile(0.99), data['walkDistance'].max()))
#
# # The plot of the distribution of walking
# walk_data = data.copy()
# walk_data = walk_data[walk_data['walkDistance'] < walk_data['walkDistance'].quantile(0.99)]
# plt.title("Walking Distance Distribution")
# sns.distplot(walk_data['walkDistance'], kde=False)
# plt.savefig('./image/Walk distribution.png')
# plt.show()
#
#
# # Plot of walk vs win
# sns.scatterplot(x="winPlacePerc", y="walkDistance", data=data)
# plt.title("walkDistance vs Win ")
# plt.savefig('./image/Walk vs win.png')
# plt.show()
#
#
# # ------------------------------------------------------
# # -                    Drive Analysis                  -
# # ------------------------------------------------------
# print(data['rideDistance'].describe())
#
# print("The average of each team drive for {:.2f} m, "
#       "99% of people have drive {} m, the most driving distance is {}m."
#       .format(data['rideDistance'].mean(), data['rideDistance'].quantile(0.99), data['rideDistance'].max()))
#
# # The plot of the distribution of driving
# drive_data = data.copy()
# drive_data = drive_data[drive_data['rideDistance'] < drive_data['rideDistance'].quantile(0.99)]
# plt.title("Drive Distance Distribution")
# sns.distplot(drive_data['rideDistance'], kde=False, color='red')
# plt.savefig('./image/drive distribution.png')
# plt.show()
#

# # The plot of the distribution of driving
# drive_data = data.copy()
# drive_data = drive_data[drive_data['rideDistance'] < drive_data['rideDistance'].quantile(0.99)]
# plt.title("Drive Distance Distribution")
# sns.distplot(drive_data['rideDistance'], kde=False, color='red')
# plt.savefig('./image/drive distribution.png')
# plt.show()
#
# # Plot of drive vs win
# sns.scatterplot(x="winPlacePerc", y="rideDistance", data=data)
# plt.title("rideDistance vs win")
# plt.savefig('./image/drive vs win.png')
# plt.show()
#
# swim = data.copy()
# swim['swimDistance'] = pd.cut(swim['swimDistance'], [-1, 0, 5, 20, 5286], labels=['0m','1-5m', '6-20m', '20m+'])
# plt.figure(figsize=(15, 8))
# sns.boxplot(x="swimDistance", y="winPlacePerc", data=swim)
# plt.show()

# walk = data.copy()
# walk['walkDistance'] = pd.cut(walk['walkDistance'], [-1, 3000, 6000, 10000, 17300], labels=['0km','1-3km', '4-6km', '6km+'])
# plt.figure(figsize=(15, 8))
# sns.boxplot(x="walkDistance", y="winPlacePerc", data=walk)
# plt.show()
# # ------------------------------------------------------
# # -            Walk/Drive/Swimming Analysis            -
# # ------------------------------------------------------
#
# #
# walk0 = data[data["walkDistance"] == 0]
# ride0 = data[data["rideDistance"] == 0]
# swim0 = data[data["swimDistance"] == 0]
# print("{} of players didn't walk at all, {} players didn't drive and {} didn't swim."
#       .format(len(walk0), len(ride0), len(swim0)))
#
# # ------------------------------------------------------
# # -                 Heal/Boost Analysis                -
# # ------------------------------------------------------
# print("The average person uses {:.1f} heal items, 99% of people use {} or less, the most used is {}."
#       .format(data['heals'].mean(), data['heals'].quantile(0.99), data['heals'].max()))
# print("The average person uses {:.1f} boost items, 99% of people use {} or less, the most used is {}."
#       .format(data['boosts'].mean(), data['boosts'].quantile(0.99), data['boosts'].max()))
#
#
# # The plot of the distribution of healing
# heal_data = data.copy()
# heal_data = heal_data[heal_data['heals'] < heal_data['heals'].quantile(0.99)]
# heal_data = heal_data[heal_data['boosts'] < heal_data['boosts'].quantile(0.99)]
# plt.title("heals  Distribution")
# sns.distplot(heal_data['heals'], kde=False)
# plt.savefig('./image/heals distribution.png')
# plt.show()
# #
# # # The plot of the distribution of boosts
# # plt.title("boosts  Distribution")
# # sns.distplot(heal_data['boosts'], kde=False)
# # plt.savefig('./image/boost distribution.png')
# # plt.show()
# #
# # The point plot of boosts and heals with the winPlacePerc
# plt.subplots(figsize=(14, 4))
# sns.pointplot(x='heals', y='winPlacePerc', data=heal_data, color='red')
# sns.pointplot(x='boosts', y='winPlacePerc', data=heal_data, color='blue')
# plt.text(4, 0.6, 'Heals', color='red')
# plt.text(4, 0.55, 'Boosts', color='blue')
# plt.xlabel('Number of heal/boost items')
# plt.ylabel('Win Percentage')
# plt.title('Heals / Boosts  VS Win Ratio')
# plt.grid()
# plt.savefig('./image/boost and heal vs win.png')
# plt.show()


# # Plot of swim vs win
# sns.scatterplot(x="winPlacePerc", y="swimDistance", data=data)
# plt.title("swimDistance vs win")
# plt.savefig('./image/swim vs win.png')
# plt.show()
