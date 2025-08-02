import edge_tts
import asyncio
import os


print("Python File Manager 🗄️");


def createFile():
    print("U are in file creation menu - :")
    fileName = str(input("Enter file name"))
    f = open(fileName, "w")
  
    fileinput = str(input("Enter the content u want to enter in file -"));
    f.write(fileinput);
    print("File created succesfully\n")
    f.close()


def readFile():
    fileName = str(input("Enter file name to open"))
    f  = open(fileName ,"r",encoding="utf-8");
    print("-----------------")
    content =  f.read();
    print("Reading.....3...2...1.. 🔊 🔊")
    
    return content;  


async def speak_text(message):
      
    voice = "hi-IN-MadhurNeural"  
    rate = "+0%"  

    output_file = "output.mp3"
    communicate = edge_tts.Communicate(message, voice=voice, rate=rate)
    await communicate.save(output_file)

    os.system(f"afplay {output_file}")  


def appendFile():
    fileName = str(input("Enter file name to open"))
    f = open(fileName,"a");
    fileinput = str(input("Enter the content u want add to file -"));
    f.write(fileinput);
    print("File appended succesfully\n")
    f.close();


def deleteFile():
        fileName = str(input("Enter file name to delete 👽"))
        if os.path.exists(fileName):
         os.remove(fileName)
        else:
            print("file doesn't exist's");
            print("File deleted succesfully ✅")
        

while True:
   
    print("Pls Select the Menu For the operation's 🎚️ ")
    print("Create a new File 📂 - 1")
    print("Read the file 🔉 - 2");
    print("add data to existing file 🖨️ - 3");
    print("Delete any file ? - 4")

    usr_inp = (input("Enter here >> "))
     
    if usr_inp == "1":
        createFile();
    elif usr_inp == "2":
        fileContent =  readFile();
        asyncio.run(speak_text(fileContent))
    elif usr_inp == "3":
        appendFile();
    elif usr_inp == "4":
        deleteFile();
    elif usr_inp == "5":
        exit;
    else:
        break;