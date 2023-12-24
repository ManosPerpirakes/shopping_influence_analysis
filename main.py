import pandas as pd

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
print("\nInfluence of social media to shoppers:\n")
exporttxt += "Influence of social media to shoppers:\n\n"
results_count_gender = df_gender.groupby(by= "Segment Description")["Count"].sum()
results_percentage_gender = (df_gender_social.groupby(by= "Segment Description")["Percentage"].sum())*100
results_count_platform = df_platform.groupby(by = "Segment Type")["Count"].sum()
results_percentage_platform = (df_platform_social.groupby(by = "Segment Type")["Percentage"].sum())*100
results_count_religion = df_religion.groupby(by = "Segment Description")["Count"].sum()
results_percentage_religion = (df_religion_social.groupby(by = "Segment Description")["Percentage"].sum())*100
results_count_major = df_major.groupby(by = "Segment Description")["Count"].sum()
results_percentage_major = (df_major_social.groupby(by = "Segment Description")["Percentage"].sum())*100
print("Count of voters by group:\n")
exporttxt += "Count of voters by group:\n\n"
print(results_count_gender)
exporttxt += str(results_count_gender)
print()
exporttxt += "\n\n"
print(results_count_platform)
exporttxt += str(results_count_platform)
print()
exporttxt += "\n\n"
print(results_count_religion)
exporttxt += str(results_count_religion)
print()
exporttxt += "\n\n"
print(results_count_major)
exporttxt += str(results_count_major)
print()
exporttxt += "\n\n"
print("Percentage of influence:\n")
exporttxt += "Percentage of influence:\n\n"
print(results_percentage_gender)
exporttxt += str(results_percentage_gender)
print()
exporttxt += "\n\n"
print(results_percentage_platform)
exporttxt += str(results_percentage_platform)
print()
exporttxt += "\n\n"
print(results_percentage_religion)
exporttxt += str(results_percentage_religion)
print()
exporttxt += "\n\n"
print(results_percentage_major)
exporttxt += str(results_percentage_major)
with open("analysis.txt", "w") as file:
    file.write(exporttxt)