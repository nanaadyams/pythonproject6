import nidaqmx

import mysql.connector

mydb = mysql.connector.connect(
  host="mjdr3247_daqmotor",
  user="mjdr3247_daqmotor",
  passwd="nadyaSHAMARA1406",
  database="mjdr3247_daqmotor"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT voltase FROM tb_knob ORDER BY timestamp DESC LIMIT 1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  task = nidaqmx.Task()
  task.ao_channels.add_ao_voltage_chan('Dev1/ao1', 'mychannel', 0,5)
  task.start()
  value = myresult
  task.write (value)
    
  task.stop ()
  task.close ()
