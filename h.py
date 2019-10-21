musicians = ["Avicii", "Sia", "Labrinth",]
print(musicians)

locations = [(20.2334, 97.7888), (20.3200, 23.4829), (23.2342, 29.3293)]
print(locations)

traits = {"height": "170",
          "color": "black",
          "writer": "Horie",}

n = input("キーを入力してください")
if n in traits:
    print(traits[n])
else:
    print("別のキーを入力してください")

fav_musician = {"Sia":
                ["Chandelier", "Thundercloud","Cheap Thrills"],
                "Avicii":
                ["The night", "Waiting for love", "Without you"]}

print(fav_musician["Sia"])
