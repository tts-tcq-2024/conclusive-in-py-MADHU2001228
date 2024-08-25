from classify_temperature_breach import classify_temperature_breach
from send_alert import send_to_controller,send_to_email


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)
  else:
    raise ValueError(f"Unknown alert target: {alertTarget}")
    
  print(f"Alert sent to {alertTarget}: {breachType}")
