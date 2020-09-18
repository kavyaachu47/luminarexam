f=open("complete.csv","r")
dict={}
for lines in f:
    Date,State,Latitude,Longitude,TotalConfirmedcases,Death,Cured,Newcases,Newdeaths,Newrecovered = lines.rstrip("\n").split(",")
    if(State not in dict):
        dict[State] = {"State": State, "confirmed": TotalConfirmedcases, "Death": Death, "recovered": Newrecovered}

def fetchData(**kwargs):
    id = kwargs["State"]
    if(State not in dict):
       # dict[State] = {"State": State, "confirmed": TotalConfirmedcases, "Death": Death, "recovered": Newrecovered}

        print("state doesnot exist")
    else:
        dict[State] = {"State": State, "confirmed": TotalConfirmedcases, "Death": Death, "recovered": Newrecovered}
        print(dict[State]["confirmed"])
        if "param" in kwargs:
            val = kwargs["param"]
            print(dict[State][val])
fetchData(State="Kerala",param="confirmed")
print("confirmedcases=",TotalConfirmedcases)

def fetchData1(**kwargs):
    id = kwargs["State"]
    if(State not in dict):
        print("state doesnot exist")
    else:
         print(dict[State]["Death"])
         if "prop" in kwargs:
            val = kwargs["param"]
            print(dict[State][val])
fetchData1(State="Kerala",param="Death")
print("death=",Death)

def fetchData2(**kwargs):
    id = kwargs["State"]
    if(State not in dict):
        print("state doesnot exist")
    else:
         print(dict[State]["recovered"])
         if "prop" in kwargs:
            val = kwargs["param"]
            print(dict[State][val])
fetchData2(State="Kerala",param="recovered")
print("recoveredcases=",Newrecovered)