import pandas
class VisitorsAnalyticsUtils:
    def __init__ (self,):
        pass
    def loadDataFile (self):
        pandas.set_option('display.max_columns', None)
        df = pandas.read_csv("Int_Monthly_Visitor (1).csv", thousands=',', na_values=' na ')
        dfn = pandas.read_csv("Int_Monthly_Visitor (1).csv",thousands= ',',na_values=" na ")
        df = df.fillna(value=0)
        year_series =  df["   "]
        year_series = year_series.str.strip()
        year_df = year_series.str.split(" ",expand=True)
        df = df.assign(year = year_df[0]) 
        df = df.drop(columns="   ")
        dfn = dfn.drop(columns="   ")
        print(df[:5])
        return dfn
    def getTop3countries (self):
        match time , region:
            case(1,1):
                print("*** Top 3 countries ***")
                print(asia.loc[:119].sum().sort_values(ascending=False).head(3))
            case(2,1):
                print("*** Top 3 countries ***")
                print(asia.loc[120:240].sum().sort_values(ascending=False).head(3))
            case(3,1):
                print("*** Top 3 countries ***")
                print(asia.loc[240:360].sum().sort_values(ascending=False).head(3))
            case(4,1):
                print("*** Top 3 countries ***")
                print(asia.loc[360:481].sum().sort_values(ascending=False).head(3))
            case(1,2):
                print("*** Top 3 countries ***")
                print(europe.loc[:119].sum().sort_values(ascending=False).head(3))
            case(2,2):
                print("*** Top 3 countries ***")
                print(europe.loc[120:240].sum().sort_values(ascending=False).head(3))
            case(3,2):
                print("*** Top 3 countries ***")
                print(europe.loc[240:360].sum().sort_values(ascending=False).head(3))
            case(4,2):
                print("*** Top 3 countries ***")
                print(europe.loc[360:481].sum().sort_values(ascending=False).head(3))
            case(1,3):
                print("*** Top 3 countries ***")
                print(others.loc[:119].sum().sort_values(ascending=False).head(3))
            case(2,3):
                print("*** Top 3 countries ***")
                print(others.loc[120:240].sum().sort_values(ascending=False).head(3))
            case(3,3):
                print("*** Top 3 countries ***")
                print(others.loc[240:360].sum().sort_values(ascending=False).head(3))
            case(4,3):
                print("*** Top 3 countries ***")
                print(others.loc[360:481].sum().sort_values(ascending=False).head(3))
    def parseData (self):
            match time , region:
                case(1,1):
                    print("*** Pared Data (Regions) ***")
                    print(asiay.iloc[:119].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[:119].describe())
                case(2,1):
                    print("*** Pared Data (Regions) ***")
                    print(asiay.iloc[120:240].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[120:240].describe())
                case(3,1):
                    print("*** Pared Data (Regions) ***")
                    print(asiay.iloc[240:360].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[240:360].describe())
                case(4,1):
                    print("*** Pared Data (Regions) ***")
                    print(asiay.iloc[360:481].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[360:481].describe)
                case(1,2):
                    print("*** Pared Data (Regions) ***")
                    print(europey.iloc[:120].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[:120].describe())
                case(2,2):
                    print("*** Pared Data (Regions) ***")
                    print(europey.iloc[120:240].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[120:240].describe())
                case(3,2):
                    print("*** Pared Data (Regions) ***")
                    print(europey.iloc[240:360].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[240:360].describe())
                case(4,2):
                    print("*** Pared Data (Regions) ***")
                    print(europey.iloc[360:481].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[360:481].describe())
                case(1,3):
                    print("*** Pared Data (Regions) ***")
                    print(othersy.iloc[:120].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[:120].describe())
                case(2,3):
                    print("*** Pared Data (Regions) ***")
                    print(othersy.iloc[120:240].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[120:240].describe())
                case(3,3):
                    print("*** Pared Data (Regions) ***")
                    print(othersy.iloc[240:360].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[240:360].describe())
                case(4,3):
                    print("*** Pared Data (Regions) ***")
                    print(othersy.iloc[360:481].info())
                    print("*** Parsed Data (Years) ***")
                    print(years.iloc[360:481].describe())
df = pandas.read_csv("Int_Monthly_Visitor (1).csv", thousands=',', na_values=' na ')
df = df.fillna(value=0)
year_series =  df["   "]
year_series = year_series.str.strip()
year_df = year_series.str.split(" ",expand=True)
df = df.drop(columns="   ")
df = df.assign(year = year_df[0]).astype('float64')
df = df.assign(month = year_df[1])
years = df['year']
months = df['month']
asia = df[[" Brunei Darussalam "," Indonesia "," Malaysia "," Philippines "," Thailand "," Viet Nam "," Myanmar "," Japan "," Hong Kong "," China "," Taiwan "," Korea, Republic Of "," India "," Pakistan "," Sri Lanka "," Saudi Arabia "," Kuwait "," UAE "]]
others = df[[" USA "," Canada "," Australia "," New Zealand "," Africa "]]
europe = df[[" United Kingdom "," Germany "," France "," Italy "," Netherlands "," Greece "," Belgium & Luxembourg "," Switzerland "," Austria "," Scandinavia "," CIS & Eastern Europe "]]
asiay = df[['year'] + ['month'] + [" Brunei Darussalam "," Indonesia "," Malaysia "," Philippines "," Thailand "," Viet Nam "," Myanmar "," Japan "," Hong Kong "," China "," Taiwan "," Korea, Republic Of "," India "," Pakistan "," Sri Lanka "," Saudi Arabia "," Kuwait "," UAE "]]
othersy = df[['year'] + ['month'] + [" USA "," Canada "," Australia "," New Zealand "," Africa "]]
europey = df[['year'] + ['month'] + [" United Kingdom "," Germany "," France "," Italy "," Netherlands "," Greece "," Belgium & Luxembourg "," Switzerland "," Austria "," Scandinavia "," CIS & Eastern Europe "]]
c = VisitorsAnalyticsUtils()
while True:
    print("year period:1=1978-1987,2=1988-1997,3=1998-2007,4=2008-2017")
    time = int(input(f"enter year period: 1, 2, 3, 4"))
    print("region:1=asia,2=europe,3=others")
    region = int(input(f"enter region name: 1 , 2, 3"))
    if time not in [1,2,3,4] or region not in [1,2,3]:
        print(f"please try again")
        break
    else:
        c.loadDataFile()
        c.getTop3countries()
        c.parseData()
        print(VisitorsAnalyticsUtils , c , year_series , year_df , years , months)
    break
