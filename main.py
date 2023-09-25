import matplotlib.pyplot as plt
import pandas as pd
office_episodes_df = pd.read_csv("datasets/office_episodes.csv")

colors = []
size = []

#Colors append
for x, y in office_episodes_df.iterrows():
    if y['scaled_ratings'] < 0.25:
        colors.append("red")
    elif 0.25 <= y['scaled_ratings'] < 0.50:
        colors.append("orange")
    elif 0.50 <= y['scaled_ratings'] < 0.75:
        colors.append("lightgreen")
    else:
        colors.append("darkgreen")

#Size append
for x, y in office_episodes_df.iterrows():
    if y['has_guests'] == True:
        size.append(250)
    else: size.append(25)

has_guest_star = office_episodes_df['has_guests'] == True

no_guest_star = office_episodes_df['has_guests'] == False

fig = plt.figure()

office_episodes_df['colors'] = colors
office_episodes_df['size'] = size
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.scatter(office_episodes_df['episode_number'], office_episodes_df['viewership_mil'], c=office_episodes_df['colors'], s=office_episodes_df['size'])
plt.show()



stars_df = office_episodes_df[has_guest_star]
print(office_episodes_df[office_episodes_df['viewership_mil'] > 20]['guest_stars'])

