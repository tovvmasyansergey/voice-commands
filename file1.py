"""
This module handles voice commands using speech_recognition.
Created by: Sergey Tovmasyan
Date: 05.06.2024
"""
import speech_recognition as sr
import os
import subprocess
def execute_command(command):
    """
    Function: execute_command
    Brief: The function takes a command and executes it
    Params: command - the command given by the user
    Return: None
    """
    if command.lower() == "home":
        file = os.path.expanduser("~")
        print(file)
    elif command.lower() == "directories":
        dirs = []
        for dir in os.listdir(os.path.expanduser("~")):
            if os.path.isdir(os.path.join(os.path.expanduser("~"),dir)):
                dirs.append(dir)
        print(dirs)
    elif command.lower() == "files of homework":
        f = os.path.expanduser("~")
        l = os.listdir(os.path.join(f,"homework"))
        for i in l:
            if i.endswith(".py"):
                print(i)
    elif command.lower() == "files of classwork":
        f = os.path.expanduser("~")
        l = os.listdir(os.path.join(f,"classwork"))
        print(l)
    elif command.lower() == "size before five hundred":
        home_dir = os.path.expanduser("~")
        homework_dir = os.path.join(home_dir,"homework")
        file_list = os.listdir(homework_dir)
        for file in file_list:
            file_path = os.path.join(homework_dir,file)
            if os.path.getsize(file_path) < 500:
                print(file)
    elif command.lower() == "create directory":
        home_dir = os.path.expanduser("~")
        new_dir = os.path.join(home_dir,"new_dir")
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)
            print("create")
        else:
            print("is exist")
    elif command.lower() == "create file":
        home_dir = os.path.expanduser("~")
        homework_dir = os.path.join(home_dir,"homework")
        file_path = os.path.join(home_dir,"homework","new_file1.py")
        if not os.path.isfile(file_path):
            with open(file_path,"w") as new_f:
                new_f.write('')
            print("create")
        else:
            print("exist")
    elif command.lower() == "open game":
        home_dir = os.path.expanduser("~")
        project2_dir = os.path.join(home_dir,"homework")
        file_path = os.path.join(project2_dir,"tic_tac_toe.py")
        subprocess.run(["python3",file_path],check = True)
    elif command.lower() == "open second game":
        home_dir = os.path.expanduser("~")
        project2_dir = os.path.join(home_dir,"homework")
        file_path = os.path.join(project2_dir,"task3.py")
        subprocess.run(["python3",file_path],check = True)
    elif command.lower() == "modules":
        home_dir = os.path.expanduser("~")
        subprocess.run(["pip list"],shell = True)
    else:
        print("no command")

def main():
    """
    Function: main
    Brief: The main function to capture voice command and execute it
    Params: None
    Return: None
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("say...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio,language = "en - US")
            print("you say: " + command)
            execute_command(command)
        except sr.UnknownValueError:
            print("dont understand")
        except sr.RequestError as e:
            print("error with networking")
if __name__ == "__main__":
    main()
