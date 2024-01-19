from main import *

exporttxt= ""
print("\nInfluence of social media to shoppers:\n")
exporttxt += "Influence of social media to shoppers:\n\n"
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
print(results_count_school)
exporttxt += str(results_count_school)
print()
exporttxt += "\n\n"
print(results_count_games)
exporttxt += str(results_count_games)
print()
exporttxt += "\n\n"
print(results_count_political)
exporttxt += str(results_count_political)
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
print()
exporttxt += "\n\n"
print(results_percentage_school)
exporttxt += str(results_percentage_school)
print()
exporttxt += "\n\n"
print(results_percentage_games)
exporttxt += str(results_percentage_games)
print()
exporttxt += "\n\n"
print(results_percentage_political)
exporttxt += str(results_percentage_political)
exportlst = []
for i in exporttxt:
    if not (i == "🔷" or i == "🐘"):
        exportlst += i
exporttxt = ""
for i in exportlst:
    exporttxt += i
with open("analysis.txt", "w") as file:
    file.write(exporttxt)