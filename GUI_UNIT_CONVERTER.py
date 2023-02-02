from tkinter import *
import conversion_logics as cvl
from tkinter import ttk

root = Tk()
root.title('UNIT CONVERTER')
root.geometry('300x400')

root.config(bg='#0D3F58')


conversion_type_frm = LabelFrame(root, text='Conversion Category', border=5, bg='#0D3F58',fg="white")
conversion_type_frm.pack(pady=(5, 5), padx=(5, 5))
result = 0

def conversion_heart(category, from_what, to_what, value):
    global result
    output_entry.delete(0, END)
    try:
        if category == 'Area':
            if from_what == 'Acres':
                if to_what == 'Hectares':
                    result = cvl.area.acre.acretohectare(float(value))
                elif to_what == 'Square-Centimeter':
                    result = cvl.area.acre.acretosquarecentimeter(float(value))
                elif to_what == 'Square-Feet':
                    result = cvl.area.acre.acretosquarefeet(float(value))
                elif to_what == 'Square-Kilometer':
                    result = cvl.area.acre.acretosquarekilometer(float(value))
                elif to_what == 'Square-Meter':
                    result = cvl.area.acre.acretosquaremeter(float(value))

            elif from_what == 'Hectares':
                if to_what == 'Acres':
                    result = cvl.area.hectare.hectaretoacre(float(value))
                elif to_what == 'Square-Centimeter':
                    result = cvl.area.hectare.hectaretosquarecentimeter(float(value))
                elif to_what == 'Square-Feet':
                    result = cvl.area.hectare.hectaretosquarefeet(float(value))
                elif to_what == 'Square-Kilometer':
                    result = cvl.area.hectare.hectaretosquarekilometer(float(value))
                elif to_what == 'Square-Meter':
                    result = cvl.area.hectare.hectaretosquaremeter(float(value))

            elif from_what == 'Square-Centimeter':
                if to_what == 'Acres':
                    result = cvl.area.squarecentimeter.squarecentimetertoacre(float(value))
                elif to_what == 'Hectares':
                    result = cvl.area.squarecentimeter.squarecentimetertohectare(float(value))
                elif to_what == 'Square-Feet':
                    result = cvl.area.squarecentimeter.squarecentimetertosquarefeet(float(value))
                elif to_what == 'Square-Kilometer':
                    result = cvl.area.squarecentimeter.squarecentimetertosquarekilometer(float(value))
                elif to_what == 'Square-Meter':
                    result = cvl.area.squarecentimeter.squarecentimetertometer(float(value))

            elif from_what == 'Square-Feet':
                if to_what == 'Acres':
                    result = cvl.area.squarefeet.squarefeettoacre(float(value))
                elif to_what == 'Hectares':
                    result = cvl.area.squarefeet.squarefeettohectare(float(value))
                elif to_what == 'Square-Centimeter':
                    result = cvl.area.squarefeet.squarefeettosquarecentimeter(float(value))
                elif to_what == 'Square-Kilometer':
                    result = cvl.area.squarefeet.squarefeettosquarekilometer(float(value))
                elif to_what == 'Square-Meter':
                    result = cvl.area.squarefeet.squarefeettosquaremeter(float(value))

            elif from_what == 'Square-Kilometer':
                if to_what == 'Acres':
                    result = cvl.area.squarekilometer.squarekilometertoacer(float(value))
                elif to_what == 'Hectares':
                    result = cvl.area.squarekilometer.squarekilometertohectare(float(value))
                elif to_what == 'Square-Centimeter':
                    result = cvl.area.squarekilometer.squarekilometertosquarecentimeter(float(value))
                elif to_what == 'Square-Feet':
                    result = cvl.area.squarekilometer.squarekilometertosquarefeet(float(value))
                elif to_what == 'Square-Meter':
                    result = cvl.area.squarekilometer.squarekilometertosquaremeter(float(value))

            elif from_what == 'Square-Meter':
                if to_what == 'Acres':
                    result = cvl.area.squaremeter.squaremetertoacer(float(value))
                elif to_what == 'Hectares':
                    result = cvl.area.squaremeter.squaremetertohectare(float(value))
                elif to_what == 'Square-Centimeter':
                    result = cvl.area.squaremeter.squaremetertosquarecentimeter(float(value))
                elif to_what == 'Square-Feet':
                    result = cvl.area.squaremeter.squaremetertosquarefeet(float(value))
                elif to_what == 'Square-Kilometer':
                    result = cvl.area.squaremeter.squaremetertosquarekilometer(float(value))

        elif category == 'Angle':
            if from_what == 'Degree':
                if to_what == 'Gradian':
                    result = cvl.angle.degree.degreetogradian(float(value))
                elif to_what == 'Radian':
                    result = cvl.angle.degree.degreetoradian(float(value))

            if from_what == 'Radian':
                if to_what == 'Gradian':
                    result = cvl.angle.radian.radiantogradian(float(value))
                elif to_what == 'Degree':
                    result = cvl.angle.radian.radiantodegree(float(value))

            if from_what == 'Gradian':
                if to_what == 'Radian':
                    result = cvl.angle.gradian.gradiantoradian(float(value))
                elif to_what == 'Degree':
                    result = cvl.angle.gradian.gradiantodegree(float(value))

        elif category == 'Energy':
            if from_what == 'Calorie':
                if to_what == 'Joule':
                    result = cvl.energy.calorie.calorietojoule(float(value))
                elif to_what == 'Kilo-Calorie':
                    result = cvl.energy.calorie.calorietokilocalorie(float(value))
                elif to_what == 'Kilo-Joule':
                    result = cvl.energy.calorie.calorietokilojoule(float(value))

            elif from_what == 'Joule':
                if to_what == 'Calorie':
                    result = cvl.energy.joule.jouletocalorie(float(value))
                elif to_what == 'Kilo-Calorie':
                    result = cvl.energy.joule.jouletokilocalorie(float(value))
                elif to_what == 'Kilo-Joule':
                    result = cvl.energy.joule.jouletokilojoule(float(value))

            elif from_what == 'Kilo-Calorie':
                if to_what == 'Calorie':
                    result = cvl.energy.kilocalorie.kilocalorietocalorie(float(value))
                elif to_what == 'Joule':
                    result = cvl.energy.kilocalorie.kilocalorietojoule(float(value))
                elif to_what == 'Kilo-Joule':
                    result = cvl.energy.kilocalorie.kilocalorietokilojoule(float(value))

            elif from_what == 'Kilo-Joule':
                if to_what == 'Calorie':
                    result = cvl.energy.kilojoule.kilojouletocalorie(float(value))
                elif to_what == 'Kilo-Calorie':
                    result = cvl.energy.kilojoule.kilojouletokilocalorie(float(value))
                elif to_what == 'Joule':
                    result = cvl.energy.kilojoule.kilojouletojoule(float(value))

        elif category == 'Length':
            if from_what == 'Angstrom':
                if to_what == 'Centimeter':
                    result = cvl.length.angstrom.angstromtocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.angstrom.angstromtofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.angstrom.angstromtoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.angstrom.angstromtokilometer(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.angstrom.angstromtometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.angstrom.angstromtomilimeter(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.angstrom.angstromtonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.angstrom.angstromtomile(float(value))

            elif from_what == 'Centimeter':
                if to_what == 'Angstrom':
                    result = cvl.length.centimeter.centimetertoangstrom(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.centimeter.centimetertofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.centimeter.centimetertoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.centimeter.centimetertokilometer(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.centimeter.centimetertometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.centimeter.centimetertomilimeter(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.centimeter.centimetertonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.centimeter.centimetertomile(float(value))

            elif from_what == 'Feet':
                if to_what == 'Angstrom':
                    result = cvl.length.feet.feettoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.feet.feettocentimeter(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.feet.feettoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.feet.feettokilometer(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.feet.feettometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.feet.feettomilimeter(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.feet.feettonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.feet.feettomile(float(value))

            elif from_what == 'Inch':
                if to_what == 'Angstrom':
                    result = cvl.length.inch.inchtoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.inch.inchtocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.inch.inchtofeet(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.inch.inchtokilometer(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.inch.inchtometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.inch.inchtomilimeter(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.inch.inchtonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.inch.inchtomile(float(value))

            elif from_what == 'Kilometer':
                if to_what == 'Angstrom':
                    result = cvl.length.kilometer.kilometertoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.kilometer.kilometertocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.kilometer.kilometertofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.kilometer.kilometertoinch(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.kilometer.kilometertometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.kilometer.kilometertomilimeter(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.kilometer.kilometertonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.kilometer.kilometertomile(float(value))

            elif from_what == 'Meter':
                if to_what == 'Angstrom':
                    result = cvl.length.meter.metertoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.meter.metertocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.meter.metertofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.meter.metertoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.meter.metertokilometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.meter.metertomilimeter(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.meter.metertonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.meter.metertomile(float(value))

            elif from_what == 'Milimeter':
                if to_what == 'Angstrom':
                    result = cvl.length.milimeter.milimetertoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.milimeter.milimetertocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.milimeter.milimetertofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.milimeter.milimetertoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.milimeter.milimetertokilometer(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.milimeter.milimetertometer(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.milimeter.milimetertonanometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.milimeter.milimetertomile(float(value))

            elif from_what == 'Nanometer':
                if to_what == 'Angstrom':
                    result = cvl.length.nanometer.nanometertoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.nanometer.nanometertocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.nanometer.nanometertofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.nanometer.nanometertoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.nanometer.nanometertokilometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.nanometer.nanometertomilimeter(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.nanometer.nanometertometer(float(value))
                elif to_what == 'Mile':
                    result = cvl.length.nanometer.nanometertomile(float(value))

            elif from_what == 'Mile':
                if to_what == 'Angstrom':
                    result = cvl.length.mile.miletoangstrom(float(value))
                elif to_what == 'Centimeter':
                    result = cvl.length.mile.miletocentimeter(float(value))
                elif to_what == 'Feet':
                    result = cvl.length.mile.miletofeet(float(value))
                elif to_what == 'Inch':
                    result = cvl.length.mile.miletoinch(float(value))
                elif to_what == 'Kilometer':
                    result = cvl.length.mile.miletokilometer(float(value))
                elif to_what == 'Milimeter':
                    result = cvl.length.mile.miletomilimeter(float(value))
                elif to_what == 'Meter':
                    result = cvl.length.mile.miletometer(float(value))
                elif to_what == 'Nanometer':
                    result = cvl.length.mile.miletonanometer(float(value))

        elif category == 'Power':
            if from_what == 'BTU/minute':
                if to_what == 'Foot-Pound/minute':
                    result = cvl.power.btu.btutofootpound(float(value))
                elif to_what == 'Horse-Power':
                    result = cvl.power.btu.btutohorsepower(float(value))
                elif to_what == 'Kilowatt':
                    result = cvl.power.btu.btutokilowatt(float(value))
                elif to_what == 'Watt':
                    result = cvl.power.btu.btutowatt(float(value))

            elif from_what == 'Foot-Pound/minute':
                if to_what == 'BTU/minute':
                    result = cvl.power.footpound.footpoundtobtu(float(value))
                elif to_what == 'Horse-Power':
                    result = cvl.power.footpound.footpoundtohorsepower(float(value))
                elif to_what == 'Kilowatt':
                    result = cvl.power.footpound.footpoundtokilowatt(float(value))
                elif to_what == 'Watt':
                    result = cvl.power.footpound.footpoundtowatt(float(value))

            elif from_what == 'Horse-Power':
                if to_what == 'BTU/minute':
                    result = cvl.power.horsepower.horsepowertobtu(float(value))
                elif to_what == 'Foot-Pound/minute':
                    result = cvl.power.horsepower.horsepowertofootpound(float(value))
                elif to_what == 'Kilowatt':
                    result = cvl.power.horsepower.horsepowertokilowatt(float(value))
                elif to_what == 'Watt':
                    result = cvl.power.horsepower.horsepowertowatt(float(value))

            elif from_what == 'Kilowatt':
                if to_what == 'BTU/minute':
                    result = cvl.power.kilowatt.kilowatttobtu(float(value))
                elif to_what == 'Foot-Pound/minute':
                    result = cvl.power.kilowatt.kilowatttofootpound(float(value))
                elif to_what == 'Horse-Power':
                    result = cvl.power.kilowatt.kilowatttohorsepower(float(value))
                elif to_what == 'Watt':
                    result = cvl.power.kilowatt.kilowatttowatt(float(value))

            elif from_what == 'Watt':
                if to_what == 'BTU/minute':
                    result = cvl.power.watt.watttobtu(float(value))
                elif to_what == 'Foot-Pound/minute':
                    result = cvl.power.watt.watttofootpound(float(value))
                elif to_what == 'Horse-Power':
                    result = cvl.power.watt.watttohorsepower(float(value))
                elif to_what == 'Kilowatt':
                    result = cvl.power.watt.watttokilowatt(float(value))

        elif category == 'Pressure':
            if from_what == 'Atmosphere':
                if to_what == 'Bar':
                    result = cvl.pressure.atmosphere.atmospheretobar(float(value))
                elif to_what == 'Kilopascal':
                    result = cvl.pressure.atmosphere.atmospheretokilopascal(float(value))
                elif to_what == 'Pascal':
                    result = cvl.pressure.atmosphere.atmospheretopascal(float(value))
                elif to_what == 'MilimeterHg':
                    result = cvl.pressure.atmosphere.atmospheretommofhg(float(value))

            elif from_what == 'Bar':
                if to_what == 'MilimeterHg':
                    result = cvl.pressure.bar.bartommofhg(float(value))
                elif to_what == 'Pascal':
                    result = cvl.pressure.bar.bartopascal(float(value))
                elif to_what == 'Kilopascal':
                    result = cvl.pressure.bar.bartokilopascal(float(value))
                elif to_what == 'Atmosphere':
                    result = cvl.pressure.bar.bartoatmosphere(float(value))

            elif from_what == 'Kilopascal':
                if to_what == 'MilimeterHg':
                    result = cvl.pressure.kilopascal.kilopascaltommofhg(float(value))
                elif to_what == 'Pascal':
                    result = cvl.pressure.kilopascal.kilopascaltopascal(float(value))
                elif to_what == 'Bar':
                    result = cvl.pressure.kilopascal.kilopascaltobar(float(value))
                elif to_what == 'Atmosphere':
                    result = cvl.pressure.kilopascal.kilopascaltoatmosphere(float(value))

            elif from_what == 'Pascal':
                if to_what == 'MilimeterHg':
                    result = cvl.pressure.pascal.pascaltommofhg(float(value))
                elif to_what == 'Kilopascal':
                    result = cvl.pressure.pascal.pascaltokilopascal(float(value))
                elif to_what == 'Bar':
                    result = cvl.pressure.pascal.pascaltobar(float(value))
                elif to_what == 'Atmosphere':
                    result = cvl.pressure.pascal.pascaltoatmosphere(float(value))

            elif from_what == 'MilimeterHg':
                if to_what == 'Pascal':
                    result = cvl.pressure.mmofhg.mmofhgtopascal(float(value))
                elif to_what == 'Kilopascal':
                    result = cvl.pressure.mmofhg.mmofhgtokilopascal(float(value))
                elif to_what == 'Bar':
                    result = cvl.pressure.mmofhg.mmofhgtobar(float(value))
                elif to_what == 'Atmosphere':
                    result = cvl.pressure.mmofhg.mmofhgtoatmosphere(float(value))

        elif category == 'Temperature':
            if from_what == 'Celcius':
                if to_what == 'Kelvin':
                    result = cvl.temperature.celcius.celciustokelvin(float(value))
                elif to_what == 'Fahrenheit':
                    result = cvl.temperature.celcius.celciustofahrenheit(float(value))

            elif from_what == 'Kelvin':
                if to_what == 'Celcius':
                    result = cvl.temperature.kelvin.kelvintofahrenheit(float(value))
                elif to_what == 'Fahrenheit':
                    result = cvl.temperature.kelvin.kelvintofahrenheit(float(value))

            elif from_what == 'Fahrenheit':
                if to_what == 'Celcius':
                    result = cvl.temperature.fahrenheit.fahrenheittocelcius(float(value))
                elif to_what == 'Kelvin':
                    result = cvl.temperature.fahrenheit.fahrenheittokelvin(float(value))

        elif category == 'Time':
            if from_what == 'Day':
                if to_what == 'Hour':
                    result = cvl.time.day.daytohour(float(value))
                elif to_what == 'Minute':
                    result = cvl.time.day.daytominute(float(value))
                elif to_what == 'Second':
                    result = cvl.time.day.daytosecond(float(value))

            elif from_what == 'Hour':
                if to_what == 'Day':
                    result = cvl.time.hour.hourtoday(float(value))
                elif to_what == 'Minute':
                    result = cvl.time.hour.hourtominute(float(value))
                elif to_what == 'Second':
                    result = cvl.time.hour.hourtosecond(float(value))

            elif from_what == 'Minute':
                if to_what == 'Day':
                    result = cvl.time.minute.minutetoday(float(value))
                elif to_what == 'Hour':
                    result = cvl.time.minute.minutetohour(float(value))
                elif to_what == 'Second':
                    result = cvl.time.minute.minutetosecond(float(value))

        elif category == 'Velocity':
            if from_what == 'Centimeter/second':
                if to_what == 'Meter/second':
                    result = cvl.velocity.cmpersec.cmpersecondtompersecond(float(value))
                elif to_what == 'Kilometer/hour':
                    result = cvl.velocity.cmpersec.cmpersecondtokilometerperhr(float(value))
                elif to_what == 'Miles/hour':
                    result = cvl.velocity.cmpersec.cmpersecondtomilesperhr(float(value))

            elif from_what == 'Meter/second':
                if to_what == 'Centimeter/second':
                    result = cvl.velocity.mpersec.mpersecondtocmpersecond(float(value))
                elif to_what == 'Miles/hour':
                    result = cvl.velocity.mpersec.mpersecondtomilesperhr(float(value))
                elif to_what == 'Kilometer/hour':
                    result = cvl.velocity.mpersec.mpersecondtokilometerperhr(float(value))

            elif from_what == 'Kilometer/hour':
                if to_what == 'Centimeter/second':
                    result = cvl.velocity.kmpersec.kilometerperhrtocmpersecond(float(value))
                elif to_what == 'Miles/hour':
                    result = cvl.velocity.kmpersec.kilometerperhrtomilesperhr(float(value))
                elif to_what == 'Meter/second':
                    result = cvl.velocity.kmpersec.kilometerperhrtometerpersecond(float(value))

            elif from_what == 'Miles/hour':
                if to_what == 'Centimeter/second':
                    result = cvl.velocity.milesperhr.milesperhrtocmpersecond(float(value))
                elif to_what == 'Kilometer/hour':
                    result = cvl.velocity.milesperhr.milesperhrtokilometerperhr(float(value))
                elif to_what == 'Meter/second':
                    result = cvl.velocity.milesperhr.milesperhrtometerpersecond(float(value))

        elif category == 'Volume':  # ['Cubic Centimeter', 'Cubic Meter', 'Liter','Gallon']
            if from_what == 'Cubic-Centimeter':
                if to_what == 'Cubic-Meter':
                    result = cvl.volume.cubiccenti.cubiccentimetertocubicmeter(float(value))
                elif to_what == 'Liter':
                    result = cvl.volume.cubiccenti.cubiccentimetertoliter(float(value))
                elif to_what == 'Gallon':
                    result = cvl.volume.cubiccenti.cubiccentimetertogallon(float(value))

            elif from_what == 'Cubic-Meter':
                if to_what == 'Liter':
                    result = cvl.volume.cubicmeter.cubicmetertoliter(float(value))
                elif to_what == 'Gallon':
                    result = cvl.volume.cubicmeter.cubicmetertogallon(float(value))
                elif to_what == 'Cubic-Centimeter':
                    result = cvl.volume.cubicmeter.cubicmetertocubiccentimeter(float(value))

            elif from_what == 'Liter':
                if to_what == 'Cubic-Meter':
                    result = cvl.volume.liter.litertocubicmeter(float(value))
                elif to_what == 'Gallon':
                    result = cvl.volume.liter.litertogallon(float(value))
                elif to_what == 'Cubic-Centimeter':
                    result = cvl.volume.liter.litertocubiccentimeter(float(value))

            elif from_what == 'Gallon':
                if to_what == 'Cubic-Meter':
                    result = cvl.volume.gallon.gallontocubicmeter(float(value))
                elif to_what == 'Liter':
                    result = cvl.volume.gallon.gallontoliter(float(value))
                elif to_what == 'Cubic-Centimeter':
                    result = cvl.volume.gallon.gallontocubiccentimeter(float(value))


        elif category == 'Weight/Mass':
            if from_what == 'Kilogram':
                if to_what == 'Hectogram':
                    result = cvl.weightbymass.kilogram.kilogramtohectogram(float(value))
                elif to_what == 'Decigram':
                    result = cvl.weightbymass.kilogram.kilogramtodecigram(float(value))
                elif to_what == 'Gram':
                    result = cvl.weightbymass.kilogram.kilogramtogram(float(value))
                elif to_what == 'Dekagram':
                    result = cvl.weightbymass.kilogram.kilogramtodekagram(float(value))
                elif to_what == 'Centigram':
                    result = cvl.weightbymass.kilogram.kilogramtocentigram(float(value))
                elif to_what == 'Miligram':
                    result = cvl.weightbymass.kilogram.kilogramtomiligram(float(value))

            elif from_what == 'Hectogram':
                if to_what == 'Kilogram':
                    result = cvl.weightbymass.hectogram.hectogramtokilogram(float(value))
                elif to_what == 'Decigram':
                    result = cvl.weightbymass.hectogram.hectogramtodecigram(float(value))
                elif to_what == 'Gram':
                    result = cvl.weightbymass.hectogram.hectogramtogram(float(value))
                elif to_what == 'Dekagram':
                    result = cvl.weightbymass.hectogram.hectogramtodekagram(float(value))
                elif to_what == 'Centigram':
                    result = cvl.weightbymass.hectogram.hectogramtocentigram(float(value))
                elif to_what == 'Miligram':
                    result = cvl.weightbymass.hectogram.hectogramtomiligram(float(value))

            elif from_what == 'Decigram':
                if to_what == 'Kilogram':
                    result = cvl.weightbymass.decigram.decigramtokilogram(float(value))
                elif to_what == 'Hectogram':
                    result = cvl.weightbymass.decigram.decigramtohectogram(float(value))
                elif to_what == 'Gram':
                    result = cvl.weightbymass.decigram.decigramtogram(float(value))
                elif to_what == 'Dekagram':
                    result = cvl.weightbymass.decigram.decigramtodekagram(float(value))
                elif to_what == 'Centigram':
                    result = cvl.weightbymass.decigram.decigramtocentigram(float(value))
                elif to_what == 'Miligram':
                    result = cvl.weightbymass.decigram.decigramtomiligram(float(value))

            elif from_what == 'Gram':
                if to_what == 'Kilogram':
                    result = cvl.weightbymass.gram.gramtokilogram(float(value))
                elif to_what == 'Hectogram':
                    result = cvl.weightbymass.gram.gramtohectogram(float(value))
                elif to_what == 'Decigram':
                    result = cvl.weightbymass.gram.gramtodecigram(float(value))
                elif to_what == 'Dekagram':
                    result = cvl.weightbymass.gram.gramtodekagram(float(value))
                elif to_what == 'Centigram':
                    result = cvl.weightbymass.gram.gramtocentigram(float(value))
                elif to_what == 'Miligram':
                    result = cvl.weightbymass.gram.gramtomiligram(float(value))

            elif from_what == 'Dekagram':
                if to_what == 'Kilogram':
                    result = cvl.weightbymass.dekagram.dekagramtokilogram(float(value))
                elif to_what == 'Hectogram':
                    result = cvl.weightbymass.dekagram.dekagramtohectogram(float(value))
                elif to_what == 'Decigram':
                    result = cvl.weightbymass.dekagram.dekagramtodecigram(float(value))
                elif to_what == 'Gram':
                    result = cvl.weightbymass.dekagram.dekagramtogram(float(value))
                elif to_what == 'Centigram':
                    result = cvl.weightbymass.dekagram.dekagramtocentigram(float(value))
                elif to_what == 'Miligram':
                    result = cvl.weightbymass.dekagram.dekagramtomiligram(float(value))

            elif from_what == 'Centigram':
                if to_what == 'Kilogram':
                    result = cvl.weightbymass.centigram.centigramtokilogram(float(value))
                elif to_what == 'Hectogram':
                    result = cvl.weightbymass.centigram.centigramtohectogram(float(value))
                elif to_what == 'Decigram':
                    result = cvl.weightbymass.centigram.centigramtodecigram(float(value))
                elif to_what == 'Gram':
                    result = cvl.weightbymass.centigram.centigramtogram(float(value))
                elif to_what == 'Dekagram':
                    result = cvl.weightbymass.centigram.centigramtogram(float(value))
                elif to_what == 'Miligram':
                    result = cvl.weightbymass.centigram.centigramtomiligram(float(value))

            elif from_what == 'Miligram':
                if to_what == 'Kilogram':
                    result = cvl.weightbymass.miligram.miligramtokilogram(float(value))
                elif to_what == 'Hectogram':
                    result = cvl.weightbymass.miligram.miligramtohectogram(float(value))
                elif to_what == 'Decigram':
                    result = cvl.weightbymass.miligram.miligramtodecigram(float(value))
                elif to_what == 'Gram':
                    result = cvl.weightbymass.miligram.miligramtogram(float(value))
                elif to_what == 'Centigram':
                    result = cvl.weightbymass.miligram.miligramtocentigram(float(value))
                elif to_what == 'Dekagram':
                    result = cvl.weightbymass.miligram.miligramtodekagram(float(value))
        output_entry.insert(0, result)
    except ValueError:
        input_entry.delete(0, END)
        input_entry.insert(0, 'Value Missing!')


calc_button = Button(root, text='Calculate', font=('Cascadia Code', 13),bg='#CFA30B', fg='black')


def select_category(category):
    global output_entry, input_entry
    calc_button.pack(pady=10)

    menu_list = []

    if category == 'Area':
        area_list = ['Acres', 'Hectares', 'Square-Centimeter', 'Square-Feet', 'Square-Kilometer', 'Square-Meter']
        menu_list = area_list.copy()
    elif category == 'Angle':
        angle_list = ['Degree', 'Gradian', 'Radian']
        menu_list = angle_list.copy()
    elif category == 'Energy':
        energy_list = ['Calorie', 'Joule', 'Kilo-Calorie', 'Kilo-Joule']
        menu_list = energy_list.copy()
    elif category == 'Length':
        length_list = ['Angstrom', 'Centimeter', 'Feet', 'Inch','Kilometer', 'Meter', 'Milimeter','Nanometer', 'Mile']
        menu_list = length_list.copy()
    elif category == 'Power':
        power_list = ['BTU/minute', 'Foot-Pound/minute', 'Horse-Power', 'Kilowatt', 'Watt']
        menu_list = power_list.copy()
    elif category == 'Pressure':
        pressure_list = ['Atmosphere', 'Bar', 'Kilopascal', 'Pascal', 'MilimeterHg']
        menu_list = pressure_list.copy()
    elif category == 'Temperature':
        temp_list = ['Celcius', 'Kelvin', 'Fahrenheit']
        menu_list = temp_list.copy()
    elif category == 'Time':
        time_list = ['Day', 'Hour', 'Minute', 'Second']
        menu_list = time_list.copy()
    elif category == 'Velocity':
        velocity_list = ['Centimeter/second', 'Meter/second', 'Kilometer/hour', 'Miles/hour']
        menu_list = velocity_list.copy()
    elif category == 'Volume':
        volume_list = ['Cubic-Centimeter', 'Cubic-Meter', 'Liter', 'Gallon']
        menu_list = volume_list.copy()
    elif category == 'Weight/Mass':
        mass_list = ['Kilogram', 'Hectogram', 'Decigram', 'Gram', 'Dekagram', 'Centigram', 'Miligram']
        menu_list = mass_list.copy()
    from_var = StringVar()
    from_var.set(menu_list[0])
    from_what_dropdown = ttk.Combobox(from_what_frm, textvariable=from_var, font=('Lato', 12))
    from_what_dropdown['values'] = menu_list
    from_what_dropdown['state'] = 'readonly'
    from_what_dropdown.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
    input_lbl = Label(from_what_frm, text='Input', font=('Lato', 12))
    input_lbl.grid(row=1, column=0, padx=(5, 0))
    input_entry = Entry(from_what_frm, width=20, font=('Cascadia Code', 12))
    input_entry.grid(row=1, column=1, padx=10, pady=(0, 5))
    to_var = StringVar()
    to_var.set(menu_list[0])
    to_what_dropdown = ttk.Combobox(to_what_frm, textvariable=to_var, font=('Lato', 12))
    to_what_dropdown['values'] = menu_list
    to_what_dropdown['state'] = 'readonly'
    to_what_dropdown.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
    output_lbl = Label(to_what_frm, text='Output', font=('Lato', 12))
    output_lbl.grid(row=1, column=0, padx=(5, 0))
    output_entry = Entry(to_what_frm, width=20, font=('Cascadia Cide', 12))
    output_entry.grid(row=1, column=1, padx=10, pady=(0, 5))
    calc_button.config(command=lambda: conversion_heart(category, from_var.get(), to_var.get(), input_entry.get()))


unit_types = ['Area', 'Angle', 'Energy', 'Length', 'Power',
              'Pressure', 'Temperature', 'Time',
              'Velocity', 'Volume', 'Weight/Mass'] #types of conversion categories
unit_var = StringVar()  # stores the type of conversion
unit_var.set(unit_types[0])

category_dropdown = ttk.Combobox(conversion_type_frm, textvariable=unit_var, font=('Lato', 12))
category_dropdown['values'] =  unit_types
category_dropdown['state'] = 'readonly'
category_dropdown.pack(pady=5, padx=5)

set_btn = Button(conversion_type_frm, text='Set Category', command=lambda: select_category(unit_var.get()), bg='#CFA30B',
                 font=('Cascadia Code', 13), fg='black')
set_btn.pack(pady=(0, 5))

from_what_frm = LabelFrame(root, text='From What', bg='#0D3F58', border=3,fg="white")
from_what_frm.pack(pady=5, padx=5)

to_what_frm = LabelFrame(root, text='To what', bg='#0D3F58', border=3,fg="white")
to_what_frm.pack(pady=5, padx=5)

Button(root, text='CLOSE', font=('Cascadia Code', 16), bg="#1A80B3", fg='black', command=root.destroy).pack(side=BOTTOM,fill=BOTH)

mainloop()
