def ReadInSimulationData():
  Data = [[0, 0] for i in range(50 + 1)]
  FileIn = open("SimulationData.txt", 'r')
  DataString = FileIn.readline()
  Count = 0
  while DataString != "" and Count < 50:
    colon = DataString.index(":")
    Count += 1
    Data[Count][0] = int(DataString[0:colon])
    Data[Count][1] = int(DataString[(colon+1):])
    DataString = FileIn.readline()
  FileIn.close()
  print(Data)

ReadInSimulationData()