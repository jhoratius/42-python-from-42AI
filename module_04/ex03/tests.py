from FileLoader import FileLoader
from HowManyMedals import how_many_medals

loader = FileLoader()
data = loader.load('./data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15

how_many_medals(data, "Kjetil Andr Aamodt")
# Output
# 0.019302325581395347