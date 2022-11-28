import requests
import os
from PTL import Image
from Body.Speak import Speak

Api_Key = "vEB6PspDgE8obAcyf1zU3Jc1vlbpp5nfpXrmlbN3"

def NasaNews(Date):
    Speak("Extracting Data From Nasa . ")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date':str(Date)}

    r = requests.get(Url,params = Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Data) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)

    Path_1 = "D:\\python project\\AI using python\\" + str(FileName)
    Path_2 = "D:\\python project\\AI using python\\Data\\NasaDataBase\\" + str(FileName)
    os.rename(Path_1,Path_2)
    img = Image.open(Path_2)
    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")

NasaNews('2021-01-01')