import pandas as pd
import xlrd as xl

ScriptTypes = {
	"DESCRIPTOR":1
}

def WriteScript(file, commands):
	f= open(file,"w+")
	for command in commands:
		f.write(command + "\n")
	f.close()

def ShowScript(commands):
	for command in commands:
		print(command)

def GenerateCommands(listId, row, commands):
	commands.append("create_concept\t" + row["DESCRIPTION"])
	commands.append("update_concept\t$conceptId\tattrs=" + str(ScriptTypes[row["TYPE"]]) + ":" + row["TYPE"])
	commands.append("create_term\t" + row["OFFICIAL"] + "\ten\t$conceptId")
	commands.append("update_list\t" + str(listId) + "\tlock=false")
	commands.append("update_list\t" + str(listId) + "\tterms=$termId")
	commands.append("update_list\t" + str(listId) + "\tlock=true")


def GenerateControlledVocabularyScript(data, listId):
	# scriptCommands = ["$conceptId = 0"]
	# scriptCommands = ["update_list\t"+ str(listId) +"\tlock=false"]
	scriptCommands = []

	for lab, row in data.iterrows():
		GenerateCommands(listId,row, scriptCommands)

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
	