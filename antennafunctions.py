import math


def weight_cal(er,fo):
    c = 299792458
    result = c/(2*fo*1e6*(math.sqrt((er+1)/2)))
    return result*1000

def eeff_cal(er,fo,he):
    W =weight_cal(er,fo)
    result=( (er + 1) / 2 ) + (( (er - 1) / 2 )*(1/(math.sqrt(1+(12*(he/W))))))
    return result


""" height_cal -> length_cal"""
def height_cal(er,fo,he):
    eeff = eeff_cal(er, fo, he)
    W = weight_cal(er, fo)
    c = 299792458
    x = c/(2*fo*1e6*(math.sqrt(eeff)))
    y = 0.824*(he/1000)*(((eeff+0.3)*((W/(he))+0.264))/((eeff-0.258)*((W/he)+0.8)))
    result = (x-y)*1000
    return result