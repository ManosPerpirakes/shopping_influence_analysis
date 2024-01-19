import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WhatsgoodlyData-6.csv")
exporttxt = ''
df["Answer"].fillna("None", inplace = True)
df_gender_social = df[(df["Segment Type"] == "Gender") & (df["Answer"] != "None")]
df_gender = df[df["Segment Type"] == "Gender"]
df_platform = df[(df["Segment Type"] == "Mobile") | (df["Segment Type"] == "Web")]
df_platform_social = df[((df["Segment Type"] == "Mobile") | (df["Segment Type"] == "Web")) & (df["Answer"] != "None")]
df_religion = df[(df["Segment Description"] == "Are you? Christian") | (df["Segment Description"] == "Are you? Muslim")]
df_religion_social = df[((df["Segment Description"] == "Are you? Christian") | (df["Segment Description"] == "Are you? Muslim")) & (df["Answer"] != "None")]
df_major = df[(df["Segment Description"] == "What's your major? ME/EE/other engineer") | (df["Segment Description"] == "What's your major? Business/Econ/Finance") | (df["Segment Description"] == "What's your major? Pre-med") | (df["Segment Description"] == "What's your major? Comm / marketing") | (df["Segment Description"] == "What's your major? Languages") | (df["Segment Description"] == "What's your major? Visual/performing arts") | (df["Segment Description"] == "What's your major? History") | (df["Segment Description"] == "What's your major? Political science / philosophy") | (df["Segment Description"] == "What's your major? Comp sci")]
df_major_social = df[((df["Segment Description"] == "What's your major? ME/EE/other engineer") | (df["Segment Description"] == "What's your major? Business/Econ/Finance") | (df["Segment Description"] == "What's your major? Pre-med") | (df["Segment Description"] == "What's your major? Comm / marketing") | (df["Segment Description"] == "What's your major? Languages") | (df["Segment Description"] == "What's your major? Visual/performing arts") | (df["Segment Description"] == "What's your major? History") | (df["Segment Description"] == "What's your major? Political science / philosophy") | (df["Segment Description"] == "What's your major? Comp sci")) & (df["Answer"] != "None")]
df_school = df[(df["Segment Description"] == "or private school? Private") | (df["Segment Description"] == "or private school? No school") | (df["Segment Description"] == "or private school? Public")]
df_school_social = df[((df["Segment Description"] == "or private school? Private") | (df["Segment Description"] == "or private school? No school") | (df["Segment Description"] == "or private school? Public")) & (df["Answer"] != "None")]
df_video_games = df[(df["Segment Description"] == "games a lot? Yes, console mostly") | (df["Segment Description"] == "games a lot? No") | (df["Segment Description"] == "games a lot? Yes, mobile mostly") | (df["Segment Description"] == "games a lot? Yes, PC mostly")]
df_video_games_social = df[((df["Segment Description"] == "games a lot? Yes, console mostly") | (df["Segment Description"] == "games a lot? No") | (df["Segment Description"] == "games a lot? Yes, mobile mostly") | (df["Segment Description"] == "games a lot? Yes, PC mostly")) & (df["Answer"] != "None")]
df_political = df[(df["Segment Description"] == "What's your leaning? Liberal 🔷") | (df["Segment Description"] == "What's your leaning? Conservative 🐘") | (df["Segment Description"] == "What's your leaning? In-between")]
df_political_social = df[((df["Segment Description"] == "What's your leaning? Liberal 🔷") | (df["Segment Description"] == "What's your leaning? Conservative 🐘") | (df["Segment Description"] == "What's your leaning? In-between")) & (df["Answer"] != "None")]
results_count_gender = df_gender.groupby(by= "Segment Description")["Count"].sum()
results_percentage_gender = (df_gender_social.groupby(by= "Segment Description")["Percentage"].sum())*100
results_count_platform = df_platform.groupby(by = "Segment Type")["Count"].sum()
results_percentage_platform = (df_platform_social.groupby(by = "Segment Type")["Percentage"].sum())*100
results_count_religion = df_religion.groupby(by = "Segment Description")["Count"].sum()
results_percentage_religion = (df_religion_social.groupby(by = "Segment Description")["Percentage"].sum())*100
results_count_major = df_major.groupby(by = "Segment Description")["Count"].sum()
results_percentage_major = (df_major_social.groupby(by = "Segment Description")["Percentage"].sum())*100
results_count_school = df_school.groupby(by = "Segment Description")["Count"].sum()
results_percentage_school = (df_school_social.groupby(by = "Segment Description")["Percentage"].sum())*100
results_count_games = df_video_games.groupby(by = "Segment Description")["Count"].sum()
results_percentage_games = (df_video_games_social.groupby(by = "Segment Description")["Percentage"].sum())*100
results_count_political = df_political.groupby(by = "Segment Description")["Count"].sum()
results_percentage_political = (df_political_social.groupby(by = "Segment Description")["Percentage"].sum())*100