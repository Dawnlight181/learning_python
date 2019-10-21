import csv

cinemas = [["トップガン", "リスキービジネス", "マイノリティリポート"], ["タイタニック", "ザ・レブネント", "インセプション"], ["トレイニングデイ", "マン・オン・ワイヤー", "フライト"]]
with open("cinemas.csv", "w") as f:
    spamwriter = csv.writer(f, delimiter=",")
    for cinema in cinemas:
        spamwriter.writerow(cinema)
