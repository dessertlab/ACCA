import os
import pandas as pd
from pathlib import Path
from tqdm import tqdm
from tkinter import filedialog
import tkinter as tk

this_directory = os.getcwd()

dir_Ground_Truth = os.path.join(this_directory, os.path.join("Ground Truth and Predictions", "Ground Truth"))
ground_truth_name = os.listdir(dir_Ground_Truth)
dir_Ground_Truth = os.path.join(dir_Ground_Truth, ground_truth_name[0])

dir_Predictions = os.path.join(this_directory, os.path.join("Ground Truth and Predictions", "Predictions"))
output_dir = os.path.join(this_directory, os.path.join("Output", "Output_Syntactic_Analysis"))

root = tk.Tk()
root.withdraw()

predictions_File = filedialog.askopenfile(initialdir= dir_Predictions, 
                                          title = "Select Predictions File")

dir_Predictions = os.path.join(dir_Predictions, predictions_File.name)

matching_GT = 0

####### Operazioni preliminari #######

#Pulizia delle predizioni

read_directory = open(dir_Predictions, 'r')

list_prediction = read_directory.readlines()
list_prediction.pop(len(list_prediction)-1)
list_prediction.pop(0)

for i in range(len(list_prediction)):
    list_prediction[i] = list_prediction[i].replace("  " , "").replace("\"", "")
    if(i != ((len(list_prediction))-1)):
        list_prediction[i] = list_prediction[i][:-2]
        
prediction = pd.DataFrame({"Code": list_prediction})

read_directory = open(dir_Ground_Truth, 'r')

list_ground_truth = read_directory.readlines()

for i in range(len(list_ground_truth)):
    list_ground_truth[i] = list_ground_truth[i].replace("\n" , "")

ground_truth = pd.DataFrame({"Code": list_ground_truth})

#Inizializzazioni

list_predicted_snippet = []
list_ground_truth_snippet = []

list_output_compiler = []
num_syntax_correct = 0
count_matched = 0
count_no_compiler_error = 0

list_predicted_snippet_with_warning = []
list_output_compiler_with_warning = []

list_predicted_snippet_with_symbolNotDef = []
list_output_compiler_with_symbolNotDef = []

list_predicted_snippet_with_errors = []
list_output_compiler_with_errors = []

score = []
####### Verifica correttezza sintattica #######

for i in tqdm(range(prediction.size)):
    
    list_ground_truth_snippet.append(str(ground_truth["Code"][i]))
    list_predicted_snippet.append(str(prediction["Code"][i]))
        
    if(((str(ground_truth["Code"][i]) == str(prediction["Code"][i])) or
       (str(ground_truth["Code"][i]).replace(" ","") == str(prediction["Code"][i]).replace(" ","")))
       and matching_GT != 1):
        list_output_compiler.append("Matched with ground truth")
        num_syntax_correct = num_syntax_correct + 1 
        count_matched = count_matched + 1
        score.append(1)
    else:
        
        str_snippet = str(prediction["Code"][i])
        
        list_snippets_spllited_by_backslash = str_snippet.split('\\n ')    
        
        for j in range(len(list_snippets_spllited_by_backslash)):
            list_snippets_spllited_by_backslash[j] = list_snippets_spllited_by_backslash[j].replace('\\', '')
            
        #Creazione scrittura su un file di testo e conversione a .asm
    
        with open(output_dir + '/assembly_instruction.txt', 'w') as f:
                
            for z in range(len(list_snippets_spllited_by_backslash)):
                f.write(list_snippets_spllited_by_backslash[z])
                f.write("\n")
                
        p = Path(output_dir + '/assembly_instruction.txt')
        p.rename(p.with_suffix('.asm'))
        
        #Lancio del compilatore da shell (l'output è salvato in un file .txt temporaneo)
        os.chdir(output_dir)
        os.system("nasm -f bin assembly_instruction.asm 2>> temp.txt")
    
        #Rimozione del file .asm precedentemente creato
        
        #if os.path.isfile(output_dir + "/assembly_instruction.asm"):
        #    os.remove(output_dir + "/assembly_instruction.asm")
            
        #if os.path.isfile(output_dir + "/assembly_instruction"):
        #    os.remove(output_dir + "/assembly_instruction")
        
        #Verifica correttezza sintattica
    
        if(os.stat("temp.txt").st_size == 0):
            
            list_output_compiler.append("No compiler errors")    
            num_syntax_correct = num_syntax_correct + 1
            count_no_compiler_error = count_no_compiler_error + 1
            score.append(1)
    
        else :          
                         
            #Lettura del contenuto del file temporaneo e conversione in lista di output
            
            output_NASMcompiler = open(output_dir+"/temp.txt", 'r')
            list_output_NASMcompiler = output_NASMcompiler.readlines()
            output_NASMcompiler.close()
            
            list_output_compiler.append(''.join(list_output_NASMcompiler))

            #Variabile booleana di controllo
            error = False
            warning = False
            symbolNotDef = False
            
            #Si itera sulla lista di output
            
            for k in range(len(list_output_NASMcompiler)):
                
                #Conversione in stringa del k-esimo output e conversione in lista splittando con ' '
                
                str_output_NASMcompiler = str(list_output_NASMcompiler[k])
                list_splitted_output_NASMcompiler = str_output_NASMcompiler.split(' ')
                
                #Si verifica che non sia una warning o un simbolo non definito. 
                #In caso contrario, si setta la variabile di controllo a True
                
                if(list_splitted_output_NASMcompiler[1] != "warning:"):
                    if(list_splitted_output_NASMcompiler[2] == "symbol"):
                        if(list_splitted_output_NASMcompiler[4] == "not"):
                            if(list_splitted_output_NASMcompiler[5] != "defined\n"):
                                error = True
                            else:
                                symbolNotDef = True
                                
                                str_symbol = list_splitted_output_NASMcompiler[3]
                                str_symbol = str_symbol.replace("'","")
                                str_symbol = str_symbol[1:]
                                
                                with open(output_dir + "/assembly_instruction.asm", "a+") as f:
                                    f.write('\n')
                                    f.write(str_symbol + ":")
                                    f.close() 
                        else:
                            error = True
                    else :
                        error = True
                else:
                    warning = True
                
            #Verifica della presenza di errori e calcolo dei risultati
            
            if(symbolNotDef == True):
                
                if os.path.isfile(output_dir + "/temp.txt"):
                    os.remove(output_dir + "/temp.txt")
                    
                os.chdir(output_dir)
                os.system("nasm -f bin assembly_instruction.asm 2>> temp.txt")

                if(os.stat("temp.txt").st_size == 0): 
                    
                    list_predicted_snippet_with_symbolNotDef.append(str_snippet)    
                    list_output_compiler_with_symbolNotDef.append(''.join(list_output_NASMcompiler))
                
                else:
                     
                    error = True
                                        
                    output_NASMcompiler = open(output_dir+"/temp.txt", 'r')
                    list_output_NASMcompiler = output_NASMcompiler.readlines()
                    output_NASMcompiler.close()
                                      
            # if(warning == True and symbolNotDef == True):
            #     list_predicted_snippet_with_symbolNotDef.append(str_snippet)
            #     list_output_compiler_with_symbolNotDef.append(''.join(list_output_NASMcompiler))
            #     warning = False
            #     symbolNotDef = False
                          
            if(warning == True):
                list_predicted_snippet_with_warning.append(str_snippet)
                list_output_compiler_with_warning.append(''.join(list_output_NASMcompiler))
            
            if(error == False):
                num_syntax_correct = num_syntax_correct + 1
                score.append(1)
            else:
                list_predicted_snippet_with_errors.append(str_snippet)
                list_output_compiler_with_errors.append(''.join(list_output_NASMcompiler))
                score.append(0) 
                
            #Chiusura e rimozione del file temporaneo
        
        if os.path.isfile(output_dir + "/temp.txt"):
            os.remove(output_dir + "/temp.txt")
        
        if os.path.isfile(output_dir + "/assembly_instruction.asm"):
            os.remove(output_dir + "/assembly_instruction.asm")
        
        if os.path.isfile(output_dir + "/assembly_instruction"):
            os.remove(output_dir + "/assembly_instruction")
        
        
print("\n")
print("Number of Istances: "+str(prediction.size))
print(" - Number of predictions that match ground truth: "+str(count_matched) + " -("+str((count_matched/prediction.size)*100)+"%)")
print(" - Predictions for which there are no compilation errors: "+str(count_no_compiler_error)+ " -("+str((count_no_compiler_error/prediction.size)*100)+"%)")
print(" - Predictions with warning: "+str(len(list_predicted_snippet_with_warning)) + " -("+str((len(list_predicted_snippet_with_warning)/prediction.size)*100)+"%)")
print(" - Predictions with error 'symbol not defined': "+str(len(list_predicted_snippet_with_symbolNotDef)) + " -("+str((len(list_predicted_snippet_with_symbolNotDef)/prediction.size)*100)+"%)")
print(" - Predictions with other errors: "+str(len(list_predicted_snippet_with_errors)) + " -("+str((len(list_predicted_snippet_with_errors)/prediction.size)*100)+"%)")
print("\n")
print("Syntactic Correctness: "+ str((num_syntax_correct/prediction.size)*100)+"%")

#Salvataggio degli snippets e degli output errati e quelli che generano warning

nameFile = (predictions_File.name.split("/")[-1]).split(".")[0]
print("File: " + str(nameFile))
dir_results = os.path.join(output_dir, nameFile)

if not os.path.exists(dir_results):
    os.mkdir(os.path.join(dir_results))
    
# if not os.path.exists(os.path.join(output_dir, nameFile)):
#     os.mkdir(os.path.join(output_dir, nameFile))

df_data = {'Ground Truth Snippets' : list_ground_truth_snippet, 'Predicted Snippets' : list_predicted_snippet , 'NASM Output' : list_output_compiler, 'Score Syntax' : score}
df_snippets_compiled = pd.DataFrame(df_data)
df_snippets_compiled.to_csv(os.path.join(dir_results, "results_syntactic_analysis_"+str(nameFile)+".csv"), header=True, index=None, sep = ';')

dir_filtered = os.path.join(dir_results, "Filtered Snipptes")

if not os.path.exists(dir_filtered):
    os.mkdir(os.path.join(dir_filtered))

df_data_warning = {'Predicted Snippets' : list_predicted_snippet_with_warning , 'NASM Output Warning' : list_output_compiler_with_warning}
df_snippets_compiled = pd.DataFrame(df_data_warning)
df_snippets_compiled.to_csv(os.path.join(dir_filtered, "output_syntactic_analysis_warning_"+str(nameFile)+".csv"), header=True, index=None, sep = ';')

df_data_snt = {'Predicted Snippets' : list_predicted_snippet_with_symbolNotDef , 'NASM Output Symbol Not Defined' : list_output_compiler_with_symbolNotDef}
df_snippets_compiled = pd.DataFrame(df_data_snt)
df_snippets_compiled.to_csv(os.path.join(dir_filtered, "output_syntactic_analysis_symbolNotDefined_"+str(nameFile)+".csv"), header=True, index=None, sep = ';')

df_data_errors = {'Predicted Snippets' : list_predicted_snippet_with_errors , 'NASM Output Errors' : list_output_compiler_with_errors}
df_snippets_compiled = pd.DataFrame(df_data_errors)
df_snippets_compiled.to_csv(os.path.join(dir_filtered, "output_syntactic_analysis_errors_"+str(nameFile)+".csv"), header=True, index=None, sep = ';')
