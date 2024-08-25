from infer_breach import infer_breach

def classify_temperature_breach(coolingType, temperatureInC):
    cooling_limits = {
        'PASSIVE_COOLING': (0, 35),
        'HI_ACTIVE_COOLING': (0, 45),
        'MED_ACTIVE_COOLING': (0, 40)
    }
    
    lowerLimit, upperLimit = cooling_limits.get(coolingType, (0, 0))
    
    return infer_breach(temperatureInC, lowerLimit, upperLimit)

