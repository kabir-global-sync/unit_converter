class Area:
    def __init__(self):
        self.num = None
        self.acre = self.Acre()
        self.hectare = self.Hectare()
        self.squarefeet = self.Squarefeet()
        self.squarecentimeter = self.Squarecentimeter()
        self.squarekilometer = self.Squarekilometer()
        self.squarekilometer = self.Squarekilometer()
        self.squaremeter = self.Squaremeter()

    class Acre:

        def acretohectare(self, num):
            return num / 2.471

        def acretosquarecentimeter(self, num):
            return num * 40468564.224

        def acretosquarefeet(self, num):
            return num * 43560

        def acretosquarekilometer(self, num):
            return num * 0.0040468

        def acretosquaremeter(self, num):
            return num * 4046.8564

    class Hectare:
        def hectaretoacre(self, num):
            return num * 2.47105

        def hectaretosquarecentimeter(self, num):
            return num * 100000000

        def hectaretosquarefeet(self, num):
            return num * 107639.104

        def hectaretosquarekilometer(self, num):
            return num * 0.01

        def hectaretosquaremeter(self, num):
            return num * 10000

    class Squarecentimeter:
        def squarecentimetertoacre(self, num):
            return num * (2.4710 * 10 ** (-8))

        def squarecentimetertohectare(self, num):
            return num * (10 ** (-8))

        def squarecentimetertosquarefeet(self, num):
            return num * 0.00107639

        def squarecentimetertosquarekilometer(self, num):
            return num * (10 ** (-10))

        def squarecentimetertometer(self, num):
            return num * (10 ** (-4))

    class Squarefeet:
        def squarefeettoacre(self, num):
            return num * 2.29568 * (10 ** (-5))

        def squarefeettohectare(self, num):
            return num * 0.000009290304

        def squarefeettosquarecentimeter(self, num):
            return num * 929.0304

        def squarefeettosquarekilometer(self, num):
            return num * 0.00000009290304

        def squarefeettosquaremeter(self, num):
            return num * 0.09290304

    class Squarekilometer:
        def squarekilometertoacer(self, num):
            return num * 247.10538

        def squarekilometertohectare(self, num):
            return num * 100

        def squarekilometertosquarecentimeter(self, num):
            return num * (10 ** 10)

        def squarekilometertosquarefeet(self, num):
            return num * 10763910.416

        def squarekilometertosquaremeter(self, num):
            return num * 1000000

    class Squaremeter:
        def squaremetertoacer(self, num):
            return num * (2.471053 * (10 ** (-4)))

        def squaremetertohectare(self, num):
            return num * 0.0001

        def squaremetertosquarecentimeter(self, num):
            return num * 10000

        def squaremetertosquarefeet(self, num):
            return num * 10.76391

        def squaremetertosquarekilometer(self, num):
            return num * 0.000001


class Angle:
    def __init__(self):
        self.num = None
        self.degree = self.Degree()
        self.gradian = self.Gradian()
        self.radian = self.Radian()

    class Degree:
        def degreetogradian(self, num):
            return num * 1.111111

        def degreetoradian(self, num):
            return num * 0.017453292

    class Gradian:
        def gradiantodegree(self, num):
            return num * 0.9

        def gradiantoradian(self, num):
            return num * 0.0157079

    class Radian:
        def radiantodegree(self, num):
            return num * 57.2957795

        def radiantogradian(self, num):
            return num * 63.661977


class Energy:
    def __init__(self):
        self.num = None
        self.calorie = self.Calorie()
        self.joule = self.Joule()
        self.kilocalorie = self.Kilocalorie()

    class Calorie:
        def calorietojoule(self, num):
            return num * 4.1868

        def calorietokilocalorie(self, num):
            return num * 0.001

        def calorietokilojoule(self, num):
            return num * 0.0041868

    class Joule:
        def jouletocalorie(self, num):
            return num * 0.23884589

        def jouletokilocalorie(self, num):
            return num * 2.3884 * (10 ** (-4))

        def jouletokilojoule(self, num):
            return num * 0.001

    class Kilocalorie:
        def kilocalorietocalorie(self, num):
            return num * 1000

        def kilocalorietojoule(self, num):
            return num * 4186.8

        def kilocalorietokilojoule(self, num):
            return num * 4.1868

    class Kilojoule:
        def kilojouletocalorie(self, num):
            return num * 238.8458966

        def kilojouletokilocalorie(self, num):
            return num * 0.2388458

        def kilojouletojoule(self, num):
            return num * 1000


class Length:
    def __init__(self):
        self.num = None
        self.angstrom = self.Angstrom()
        self.centimeter = self.Centimeter()
        self.meter = self.Meter()
        self.feet = self.Feet()
        self.inch = self.Inch()
        self.kilometer = self.Kilometer()
        self.milimeter = self.Milimeter()
        self.mile = self.Mile()
        self.nanometer = self.Nanometer()

    class Angstrom:
        def angstromtocentimeter(self, num):
            return num * (10 ** (-8))

        def angstromtofeet(self, num):
            return num * (3.28083 * 10 ** (-10))

        def angstromtoinch(self, num):
            return num * 3.93700 * (10 ** (-9))

        def angstromtokilometer(self, num):
            return num * 10 ** (-13)

        def angstromtometer(self, num):
            return num * 10 ** (-10)

        def angstromtomilimeter(self, num):
            return num * 0.0000001

        def angstromtonanometer(self, num):
            return num * 0.1

        def angstromtomile(self, num):
            return num * 6.21371 * 10 ** (-14)

    class Centimeter:
        def centimetertoangstrom(self, num):
            return num * 10 ** 8

        def centimetertofeet(self, num):
            return num * 0.03280839

        def centimetertoinch(self, num):
            return num * 0.39370078

        def centimetertokilometer(self, num):
            return num * 0.00001

        def centimetertometer(self, num):
            return num * 0.01

        def centimetertomilimeter(self, num):
            return num * 10

        def centimetertonanometer(self, num):
            return num * 10000000

        def centimetertomile(self, num):
            return num * 6.213711922 * (10 ** (-6))

    class Feet:
        def feettoangstrom(self, num):
            return num * 3048000000

        def feettocentimeter(self, num):
            return num * 30.48

        def feettoinch(self, num):
            return num * 12

        def feettokilometer(self, num):
            return num * 0.0003048

        def feettometer(self, num):
            return num * 0.3048

        def feettomilimeter(self, num):
            return num * 304.8

        def feettonanometer(self, num):
            return num * 304800000

        def feettomile(self, num):
            return num * 1.893939393 * (10 ** (-4))

    class Inch:
        def inchtoangstrom(self, num):
            return num * 254000000

        def inchtocentimeter(self, num):
            return num * 2.54

        def inchtofeet(self, num):
            return num * 0.083333333

        def inchtokilometer(self, num):
            return num * 0.0000254

        def inchtometer(self, num):
            return num * 0.0254

        def inchtomilimeter(self, num):
            return num * 25.4

        def inchtonanometer(self, num):
            return num * 25400000

        def inchtomile(self, num):
            return num * 1.5782828 * (10 ** (-5))

    class Kilometer:
        def kilometertoangstrom(self, num):
            return num * (10 ** 13)

        def kilometertocentimeter(self, num):
            return num * 100000

        def kilometertofeet(self, num):
            return num * 3280.839895

        def kilometertoinch(self, num):
            return num * 39370.0787401

        def kilometertometer(self, num):
            return num * 1000

        def kilometertomilimeter(self, num):
            return num * 1000000

        def kilometertonanometer(self, num):
            return num * 1000000000000

        def kilometertomile(self, num):
            return num * 0.621371192

    class Meter:
        def metertoangstrom(self, num):
            return num * 10000000000

        def metertocentimeter(self, num):
            return num * 100

        def metertofeet(self, num):
            return num * 3.28083989

        def metertoinch(self, num):
            return num * 39.370078740

        def metertokilometer(self, num):
            return num * 0.001

        def metertomilimeter(self, num):
            return num * 1000

        def metertonanometer(self, num):
            return num * 1000000000

        def metertomile(self, num):
            return num * 6.213711922 * (10 ** (-4))

    class Milimeter:
        def milimetertoangstrom(self, num):
            return num * 10000000

        def milimetertocentimeter(self, num):
            return num * 0.1

        def milimetertofeet(self, num):
            return num * 0.0032808398

        def milimetertoinch(self, num):
            return num * 0.039370078

        def milimetertokilometer(self, num):
            return num * 0.000001

        def milimetertometer(self, num):
            return num * 0.001

        def milimetertonanometer(self, num):
            return num * 1000000

        def milimetertomile(self, num):
            return num * 6.21371192 * (10 ** (-7))

    class Nanometer:
        def nanometertoangstrom(self, num):
            return num * 10

        def nanometertocentimeter(self, num):
            return num * 0.0000001

        def nanometertofeet(self, num):
            return num * 3.2808398950 * (10 ** (-9))

        def nanometertoinch(self, num):
            return num * 3.93700787 * (10 ** (-8))

        def nanometertokilometer(self, num):
            return num * 0.000000000001

        def nanometertometer(self, num):
            return num * 0.000000001

        def nanometertomilimeter(self, num):
            return num * 0.000001

        def nanometertomile(self, num):
            return num * 6.21371192 * (10 ** (-13))

    class Mile:
        def miletoangstrom(self, num):
            return num * 16093440000000

        def miletocentimeter(self, num):
            return num * 160934.4

        def miletofeet(self, num):
            return num * 5280

        def miletoinch(self, num):
            return num * 63360

        def miletokilometer(self, num):
            return num * 1.609344

        def miletometer(self, num):
            return num * 1609.344

        def miletomilimeter(self, num):
            return num * 1609344

        def miletonanometer(self, num):
            return num * 1609344000000


class Power:
    def __init__(self):
        self.num = None
        self.btu = self.BTU
        self.footpound = self.Footpound()
        self.horsepower = self.Horsepower()
        self.kilowatt = self.Kilowatt()
        self.watt = self.Watt()

    class BTU:
        def btutofootpound(self, num):
            return num * 778.1693709

        def btutohorsepower(self, num):
            return num * 0.0235808900

        def btutokilowatt(self, num):
            return num * 0.01758426666

        def btutowatt(self, num):
            return num * 17.58426666

    class Footpound:
        def footpoundtobtu(self, num):
            return num * 0.0012850672

        def footpoundtohorsepower(self, num):
            return num * 3.03030303 * (10 ** (-5))

        def footpoundtokilowatt(self, num):
            return num * 2.25969658 * (10 ** (-5))

        def footpoundtowatt(self, num):
            return num * 0.022596965

    class Horsepower:
        def horsepowertobtu(self, num):
            return num * 42.4072203

        def horsepowertofootpound(self, num):
            return num * 33000

        def horsepowertokilowatt(self, num):
            return num * 0.74569987

        def horsepowertowatt(self, num):
            return num * 745.699871

    class Kilowatt:
        def kilowatttobtu(self, num):
            return num * 56.869019

        def kilowatttofootpound(self, num):
            return num * 44253.72895

        def kilowatttohorsepower(self, num):
            return num * 1.341022089

        def kilowatttowatt(self, num):
            return num * 1000

    class Watt:
        def watttobtu(self, num):
            return num * 0.05686901

        def watttofootpound(self, num):
            return num * 44.253728

        def watttohorsepower(self, num):
            return num * 0.00134102

        def watttokilowatt(self, num):
            return num * 0.001


class Pressure:
    def __init__(self):
        self.num = None
        self.atmosphere = self.Atmosphere()
        self.kilopascal = self.Kilopascal()
        self.pascal = self.Pascal()
        self.mmofhg = self.Mmofhg()
        self.bar = self.Bar()

    class Atmosphere:
        def atmospheretobar(self, num):
            return num * 1.01325

        def atmospheretokilopascal(self, num):
            return num * 101.325

        def atmospheretopascal(self, num):
            return num * 101325

        def atmospheretommofhg(self, num):
            return num * 760.12753

    class Bar:
        def bartoatmosphere(self, num):
            return num * 0.98692326

        def bartokilopascal(self, num):
            return num * 100

        def bartopascal(self, num):
            return num * 10000

        def bartommofhg(self, num):
            return num * 750.187546

    class Kilopascal:
        def kilopascaltoatmosphere(self, num):
            return num * 0.009869232667

        def kilopascaltobar(self, num):
            return num * 0.01

        def kilopascaltopascal(self, num):
            return num * 1000

        def kilopascaltommofhg(self, num):
            return num * 7.50187546

    class Pascal:
        def pascaltoatmosphere(self, num):
            return num * 9.86923266 * (10 ** (-6))

        def pascaltobar(self, num):
            return num * 0.00001

        def pascaltokilopascal(self, num):
            return num * 0.001

        def pascaltommofhg(self, num):
            return num * 0.00750187

    class Mmofhg:
        def mmofhgtoatmosphere(self, num):
            return num * 0.00131556

        def mmofhgtobar(self, num):
            return num * 0.001333

        def mmofhgtokilopascal(self, num):
            return num * 0.1333

        def mmofhgtopascal(self, num):
            return num * 133.3


class Temperature:
    def __init__(self):
        self.num = None
        self.celcius = self.Celcius()
        self.kelvin = self.Kelvin()
        self.fahrenheit = self.Fahrenheit()

    class Celcius:
        def celciustokelvin(self, num):

            if num == 0:
                return 273.15
            else:
                return num * 274.15

        def celciustofahrenheit(self, num):

            if num == 0:
                return 32
            else:
                return ((9*num)/5)+32

    class Kelvin:
        def kelvintocelcius(self, num):

            if num == 0:
                return -273.15
            else:
                return num * (-272.15)

        def kelvintofahrenheit(self, num):

            if num == 0:
                return -459.67
            else:
                return num * (-457.87)

    class Fahrenheit:
        def fahrenheittocelcius(self, num):

            if num == 0:
                return -17.7778
            else:
                return num * (-17.222222)

        def fahrenheittokelvin(self, num):

            if num == 0:
                return 255.3722
            else:
                return num * 255.927777


class Time:
    def __init__(self):
        self.num = None
        self.day = self.Day()
        self.hour = self.Hour()
        self.minute = self.Minute()
        self.second = self.Second()

    class Day:
        def daytohour(self, num):
            return num * 24

        def daytominute(self, num):
            return num * 1440

        def daytosecond(self, num):
            return num * 86400

    class Hour:
        def hourtoday(self, num):
            return num * 0.041666

        def hourtominute(self, num):
            return num * 60

        def hourtosecond(self, num):
            return num * 3600

    class Minute:
        def minutetoday(self, num):
            return num * 6.94444 * (10 ** (-4))

        def minutetohour(self, num):
            return num * 0.0166666

        def minutetosecond(self, num):
            return num * 60

    class Second:
        def secondtoday(self, num):
            return num * 1.15740 * (10 ** (-5))

        def secondtohour(self, num):
            return num * 2.777777 * (10 ** (-4))

        def secondtominute(self, num):
            return num * 0.0166666


class Velocity:
    def __init__(self):
        self.num = None
        self.cmpersec = self.Cmpersecond()
        self.mpersec = self.Mpersecond()
        self.kmpersec = self.Kilometerpersecond()
        self.milerperhr = self.Milesperhr()

    class Cmpersecond:
        def cmpersecondtompersecond(self, num):
            return num * 0.01

        def cmpersecondtokilometerperhr(self, num):
            return num * 0.036

        def cmpersecondtomilesperhr(self, num):
            return num * 0.0223693

    class Mpersecond:
        def mpersecondtocmpersecond(self, num):
            return num * 100

        def mpersecondtokilometerperhr(self, num):
            return num * 3.6

        def mpersecondtomilesperhr(self, num):
            return num * 2.23693629

    class Kilometerpersecond:
        def kilometerperhrtocmpersecond(self, num):
            return num * 27.77777777

        def kilometerperhrtometerpersecond(self, num):
            return num * 0.27777777

        def kilometerperhrtomilesperhr(self, num):
            return num * 0.62137119

    class Milesperhr:
        def milesperhrtocmpersecond(self, num):
            return num * 44.704

        def milesperhrtometerpersecond(self, num):
            return num * 0.44704

        def milesperhrtokilometerperhr(self, num):
            return num * 1.609344


class Volume:
    def __init__(self):
        self.num = None
        self.cubiccenti = self.Cubiccentimeter()
        self.cubicmeter = self.Cubicmeter()
        self.liter = self.Liter()
        self.gallon = self.Gallon()

    class Cubiccentimeter:
        def cubiccentimetertocubicmeter(self, num):
            return num * 0.000001

        def cubiccentimetertoliter(self, num):
            return num * 0.001

        def cubiccentimetertogallon(self, num):
            return num * 2.64172052 * (10 ** (-4))

    class Cubicmeter:
        def cubicmetertocubiccentimeter(self, num):
            return num * 1000000

        def cubicmetertoliter(self, num):
            return num * 1000

        def cubicmetertogallon(self, num):
            return num * 264.17205

    class Liter:
        def litertocubiccentimeter(self, num):
            return num * 1000

        def litertocubicmeter(self, num):
            return num * 0.001

        def litertogallon(self, num):
            return num * 0.2641720523

    class Gallon:
        def gallontocubiccentimeter(self, num):
            return num * 3785.411784

        def gallontocubicmeter(self, num):
            return num * 0.003785411784

        def gallontoliter(self, num):
            return num * 3.785411784


class WeigthByMass:
    def __init__(self):
        self.num = None
        self.kilogram = self.Kilogram()
        self.hectogram = self.Hectogram()
        self.dekagram = self.Dekagram()
        self.gram = self.Gram()
        self.decigram = self.Decigram()
        self.centigram = self.Centigram()
        self.miligram = self.Miligram()

    class Kilogram:
        def kilogramtohectogram(self, num):
            return num * 10

        def kilogramtodecigram(self, num):
            return num * 10000

        def kilogramtogram(self, num):
            return num * 1000

        def kilogramtodekagram(self, num):
            return num * 100

        def kilogramtocentigram(self, num):
            return num * 100000

        def kilogramtomiligram(self, num):
            return num * 1000000

    class Hectogram:
        def hectogramtokilogram(self, num):
            return num * 0.1

        def hectogramtodecigram(self, num):
            return num * 1000

        def hectogramtogram(self, num):
            return num * 100

        def hectogramtodekagram(self, num):
            return num * 10

        def hectogramtocentigram(self, num):
            return num * 10000

        def hectogramtomiligram(self, num):
            return num * 100000

    class Decigram:
        def decigramtokilogram(self, num):
            return num * 0.0001

        def decigramtohectogram(self, num):
            return num * 0.001

        def decigramtogram(self, num):
            return num * 0.1

        def decigramtodekagram(self, num):
            return num * 0.01

        def decigramtocentigram(self, num):
            return num * 10

        def decigramtomiligram(self, num):
            return num * 100

    class Gram:
        def gramtokilogram(self, num):
            return num * 0.001

        def gramtohectogram(self, num):
            return num * 0.01

        def gramtodecigram(self, num):
            return num * 10

        def gramtodekagram(self, num):
            return num * 0.1

        def gramtocentigram(self, num):
            return num * 100

        def gramtomiligram(self, num):
            return num * 1000

    class Dekagram:
        def dekagramtokilogram(self, num):
            return num * 0.01

        def dekagramtohectogram(self, num):
            return num * 0.1

        def dekagramtodecigram(self, num):
            return num * 100

        def dekagramtogram(self, num):
            return num * 10

        def dekagramtocentigram(self, num):
            return num * 1000

        def dekagramtomiligram(self, num):
            return num * 10000

    class Centigram:
        def centigramtokilogram(self, num):
            return num * 0.00001

        def centigramtohectogram(self, num):
            return num * 0.0001

        def centigramtodecigram(self, num):
            return num * 0.1

        def centigramtogram(self, num):
            return num * 0.01

        def centigramtodekagram(self, num):
            return num * 0.001

        def centigramtomiligram(self, num):
            return num * 10

    class Miligram:
        def miligramtokilogram(self, num):
            return num * 0.000001

        def miligramtohectogram(self, num):
            return num * 0.00001

        def miligramtodecigram(self, num):
            return num * 0.01

        def miligramtogram(self, num):
            return num * 0.001

        def miligramtodekagram(self, num):
            return num * 0.0001

        def miligramtocentigram(self, num):
            return num * 0.1


#######################################
area = Area()
angle = Angle()
energy = Energy()
length = Length()
power = Power()
pressure = Pressure()
temperature = Temperature()
time = Time()
velocity = Velocity()
volume = Volume()
weightbymass = WeigthByMass()
