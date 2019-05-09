import pandas as pd
import xlrd as xl

def WriteScript(file, commands):
	f= open(file,"w+")
	for command in commands:
		f.write(command + "\n")
	f.close()

def ShowScript(commands):
	for command in commands:
		print(command)

def GenerateCommands(row, commands):
	commands.append(row["DESCRIPTION"])

def GenerateControlledVocabularyScript(data, listId):
	scriptCommands = ["update_list	"+ str(listId) +"	lock=false"]

	for lab, row in data.iterrows():
		GenerateCommands(row, scriptCommands)

	scriptCommands.append("update_list	"+ str(listId) +"	lock=true")
	return scriptCommands

def ReadSampleData(file):
	return pd.read_excel(file)
    
    
if __name__ == '__main__':
	file = "MyScripts.txt"
	dataFile = "Super Powers Descriptor List.xlsx"
	data = ReadSampleData(dataFile)
	listId = 126890
	script = GenerateControlledVocabularyScript(data, listId)
	ShowScript(script)
	WriteScript(file, script)
