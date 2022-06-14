import random
def shutudai():
    q=["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    a=[["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
    r=random.randint(0,2)
    m=input(f"問題:\n{q[r]}\n答えるんだ:")
    if m in a[r]:
        print("正解！！！")
    else:
        print("出直してこい")
shutudai()