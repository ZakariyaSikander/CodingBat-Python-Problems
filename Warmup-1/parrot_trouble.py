# in trouble if the parrot is talking and it is before 7:00 or after 20:00

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)
