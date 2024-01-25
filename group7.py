import pandas as pd
df = pd.read_csv("Int_Monthly_Visitor (1).csv", thousands=',', na_values=' na ')
df = df.fillna(value=0)
class VisitorsAnalyticsUtils:
    def __init__ (self,):
        pass
    def loadDataFile (self):
        pd.set_option('display.max_columns', None)
        df = pd.read_csv("Int_Monthly_Visitor (1).csv", thousands=',', na_values=' na ')
        df = df.fillna(value=0)
        print(df[:5])
        return df
    def getTop3countries (self):
        if time == 1 and region == 1:
            print(f"{asia.iloc[:119].sum().sort_values(ascending=False).head(3)}")
        elif time ==2 and region == 1:
            print(f"{asia.iloc[120:240].sum().sort_values(ascending=False).head(3)}")
        elif time ==3 and region == 1:
            print(f"{asia.iloc[240:360].sum().sort_values(ascending=False).head(3)}")
        elif time ==4 and region == 1:
            print(f"{asia.iloc[360:481].sum().sort_values(ascending=False).head(3)}")
        elif time == 1 and region == 2:
            print(f"{europe.iloc[:119].sum().sort_values(ascending=False).head(3)}")
        elif time ==2 and region == 2:
            print(f"{europe.iloc[120:240].sum().sort_values(ascending=False).head(3)}")
        elif time ==3 and region == 2:
            print(f"{europe.iloc[240:360].sum().sort_values(ascending=False).head(3)}")
        elif time ==4 and region == 2:
            print(f"{europe.iloc[360:481].sum().sort_values(ascending=False).head(3)}")
        elif time == 1 and region == 3:
            print(f"{others.iloc[:119].sum().sort_values(ascending=False).head(3)}")
        elif time ==2 and region == 3:
            print(f"{others.iloc[120:240].sum().sort_values(ascending=False).head(3)}")
        elif time ==3 and region == 3:
             print(f"{others.iloc[240:360].sum().sort_values(ascending=False).head(3)}")
        elif time ==4 and region == 3:
            print(f"{others.iloc[360:481].sum().sort_values(ascending=False).head(3)}")
    def parseData (self):
        if time == 1 and region == 1:
            print(f"{asia.iloc[:119].info()}")
            print(f"{asia.iloc[:119].describe()}")
        elif time ==2 and region == 1:
            print(f"{asia.iloc[120:240].info()}")
            print(f"{asia.iloc[120:240].describe()}")
        elif time ==3 and region == 1:
            print(f"{asia.iloc[240:360].info()}")
            print(f"{asia.iloc[240:360].describe()}")
        elif time ==4 and region == 1:
            print(f"{asia.iloc[360:480].info()}")
            print(f"{asia.iloc[360:480].describe}")
        elif time == 1 and region == 2:
            print(f"{europe.iloc[:119].info()}")
            print(f"{europe.iloc[:119].describe()}")
        elif time ==2 and region == 2:
            print(f"{europe.iloc[120:240].info()}")
            print(f"{europe.iloc[120:240].describe()}")
        elif time ==3 and region == 2:
            print(f"{europe.iloc[240:360].info()}")
            print(f"{europe.iloc[240:360].describe()}")
        elif time ==4 and region == 2:
            print(f"{europe.iloc[360:481].info()}")
            print(f"{europe.iloc[360:481].describe()}")
        elif time == 1 and region == 3:
            print(f"{others.iloc[:119].info()}")
            print(f"{others.iloc[:119].describe()}")
        elif time ==2 and region == 3:
            print(f"{others.iloc[120:240].info()}")
            print(f"{others.iloc[120:240].describe()}")
        elif time ==3 and region == 3:
            print(f"{others.iloc[240:360].info()}")
            print(f"{others.iloc[240:360].describe()}")
        elif time ==4 and region == 3:
            print(f"{others.iloc[360:481].info()}")
            print(f"{others.iloc[360:481].describe()}")
call = VisitorsAnalyticsUtils()
while True:
    one = "1978-1987"
    two = "1988-1997"
    three = "1998-2007"
    four = "2008-2017"
    asia = df[[" Brunei Darussalam "," Indonesia "," Malaysia "," Philippines "," Thailand "," Viet Nam "," Myanmar "," Japan "," Hong Kong "," China "," Taiwan "," Korea, Republic Of "," India "," Pakistan "," Sri Lanka "," Saudi Arabia "," Kuwait "," UAE "]]
    others = df[[" USA "," Canada "," Australia "," New Zealand "," Africa "]]
    europe = df[[" United Kingdom "," Germany "," France "," Italy "," Netherlands "," Greece "," Belgium & Luxembourg "," Switzerland "," Austria "," Scandinavia "," CIS & Eastern Europe "]]
    time = int(input(f"enter year period: 1={one} , 2={two} , 3={three} , 4={four}"))
    region = int(input(f"enter region name: 1={asia} , 2={europe} , 3={others}"))
    if time not in [1,2,3,4] or region not in [1,2,3]:
        print(f"please try again")
        break
    else:
        call.loadDataFile()
        call.getTop3countries()
        call.parseData()
    break