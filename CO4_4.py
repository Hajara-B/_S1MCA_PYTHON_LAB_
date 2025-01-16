class Time:
    def __init__(self,hr,min,sec):
        self.__hr=hr 
        self.__min=min
        self.__sec=sec

    def __add__(self,other):
        total__secs=self.__sec + other.__sec
        extra__min=total__secs//60
        secs=total__secs%60

        total__mins=self.__min + other.__min + extra__min
        extra__hr=total__mins//60
        mins=total__mins%60

        hrs=self.__hr + other.__hr + extra__hr

        return Time(hrs,mins,secs)

    def display(self):
        return f"{self.__hr:02}:{self.__min:02}:{self.__sec:02}"

print("----TIME1---")
hr1=int(input("hr1: "))
min1=int(input("min1: "))
sec1=int(input("sec1: "))

time1=Time(hr1,min1,sec1)

print("----TIME2---")
hr2=int(input("hr2: "))
min2=int(input("min2: "))
sec2=int(input("sec3: "))

time2=Time(hr2,min2,sec2)

time_sum=time1 + time2
print(time_sum.display())





        
