from  random import randint 


class train:

  def __init__(self,trainno):
    self.trainno=trainno
  

  def book(self,fro,to):
    print(f"ticker is booked  in train no:{self.trainno} from {fro} to{to}")
  

  def getstatus(self  ):
    print(f"train no :{self.tranino} is running on time")
   
  def getfare(self , fro,to):
    print(f"ticker is booked  in train no:{self.trainno} from {fro} to{to} is {randint(222,5555)}")
    


t= train(2332)  
t.book("rmapur " ,"kokata")
