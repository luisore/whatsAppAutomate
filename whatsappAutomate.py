import pywhatkit
 
# using Exception Handling to avoid 
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+5491122646171", 
                        "Hello", 
                        17, 31)
  print("Successfully Sent!")
 
except:
   
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")