import random

innerCount = 0
lastState = "中"
def onceWish():
    global innerCount
    while True:
        hit = random.randint(1, 1000)
        if innerCount > 73:
            if(innerCount-73)*60+6 >= hit >= 1:
                innerCount = 0
                return True
            else:
                innerCount +=1
                return False
        else:
            if 6 >= hit >= 1:
                innerCount = 0
                return True
            else:
                innerCount += 1
                return False

def genshinWish():
    global innerCount, lastState
    if onceWish():
        if lastState == "中":
            if random.randint(0,1) == 0:
                return "中"
            else:
                lastState = "歪"
                return "歪"
        else:
            lastState = "中"
            return "中"
    else:
        return None

def wishXGolds(x):
    for _ in range(x):
        count = 0
        while True:
            g = genshinWish()
            if g is None:
                count += 1
            else:
                print(f"前{count}次没出金，")
                print(f"最后一次金是{g}。")
                break
                
if __name__ == "__main__":
    wishXGolds(5)