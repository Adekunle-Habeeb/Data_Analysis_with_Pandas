import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrrels = len(data[data["Primary Fur Color"] == "Black"])

# print(gray_squirrrels)
# print(red_squirrrels)
# print(black_squirrrels)

data_dict ={
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrrels, red_squirrrels, black_squirrrels],
}

dat = pandas.DataFrame(data_dict)
print(dat)

dat.to_csv("Squirell_Data.csv")














