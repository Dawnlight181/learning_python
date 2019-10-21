n = "カミュ"
print(n[0])
print(n[1])
print(n[2])

A = input("入力1")
B = input("入力2")
string = "私は昨日{}を書いて、{}に送った!".format(A, B)
print(string)

x = "aldous Huxley was born in 1894".title()
print(x)

r = "どこで？ だれが？ いつ？".split("？")
print(r)

fox = ["The", "fox", "jamped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)

ans = "A screaming comes across the sky.".replace("s", "$")
print(ans)

aaa = "Hemingway".index("m")
print(aaa)

bbb = "I like 'Fact Fulness'"
print(bbb)
ccc = "I said 'Take it easy' and made friends with them."
print(ccc)

concat = "three" + "three" + "three"
mult = "three" * 3
print(concat)
print(mult)

April = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
ddd = April[0:10]
print(ddd)
