import os
import pandas as pd
from pathlib import Path
import angr
import claripy
import collections
import shutil
from tqdm import tqdm
from tkinter import filedialog
import tkinter as tk

def postProcessingSND(str_GT, str_PR, output_dir):
    
    changeScore = False
    list_symbolsGT = []
    list_symbolsPR = []
     
    #############################PER GT#####################################
    list_snippetsGT_spllited_by_backslash = []
    list_snippetsGT_spllited_by_backslash = str_GT.split('\\n ')    
    
    for j in range(len(list_snippetsGT_spllited_by_backslash)):
        list_snippetsGT_spllited_by_backslash[j] = list_snippetsGT_spllited_by_backslash[j].replace('\\', '')

    #Creazione scrittura su un file di testo e conversione a .asm
    
    with open(output_dir + '/GT_PP.txt', 'w') as f:
        
        for z in range(len(list_snippetsGT_spllited_by_backslash)):
            f.write(list_snippetsGT_spllited_by_backslash[z])
            f.write("\n")

        f.close()

    p = Path(output_dir + '/GT_PP.txt')
    p.rename(p.with_suffix('.asm'))
        
    #Lancio del compilatore da shell (l'output è salvato in un file .txt temporaneo)
    os.chdir(output_dir)
    os.system("nasm -f bin GT_PP.asm -o GT_PP.obj 2>> tempFileGT_PP.txt")
    
    #Controllo se .asm fa riferimento ad un'architettura 64bit
    if(os.stat("tempFileGT_PP.txt").st_size != 0):
    
        #Lettura del contenuto del file temporaneo e conversione in lista di output
    
        output_NASMcompiler = open(output_dir+"/tempFileGT_PP.txt", 'r')
        list_output_NASMcompiler = output_NASMcompiler.readlines()
        output_NASMcompiler.close()
    
        #Si itera sulla lista di output
    
        for k in range(len(list_output_NASMcompiler)):
        
            #Conversione in stringa del k-esimo output e conversione in lista splittando con ' '
        
            str_output_NASMcompiler = str(list_output_NASMcompiler[k])
            list_splitted_output_NASMcompiler = str_output_NASMcompiler.split(' ')
                        
            #Si verifica che non sia una warning o un simbolo non definito. 
            #In caso contrario, si setta la variabile di controllo a True
    
            if(list_splitted_output_NASMcompiler[2] == "symbol"):
                if(list_splitted_output_NASMcompiler[4] == "not"):
                    if(list_splitted_output_NASMcompiler[5] == "defined\n"):
                        str_symbol = list_splitted_output_NASMcompiler[3]
                        str_symbol = str_symbol.replace("'","")
                        str_symbol = str_symbol[1:]
                        list_symbolsGT.append(str_symbol)

    ########################################################################        

    #############################PER PR#####################################
    list_snippetsPR_spllited_by_backslash = []
    list_snippetsPR_spllited_by_backslash = str_PR.split('\\n ')    
    
    for j in range(len(list_snippetsPR_spllited_by_backslash)):
        list_snippetsPR_spllited_by_backslash[j] = list_snippetsPR_spllited_by_backslash[j].replace('\\', '')

    #Creazione scrittura su un file di testo e conversione a .asm
    
    with open(output_dir + '/PR_PP.txt', 'w') as f:
        
        for z in range(len(list_snippetsPR_spllited_by_backslash)):
            f.write(list_snippetsPR_spllited_by_backslash[z])
            f.write("\n")

        f.close()

    p = Path(output_dir + '/PR_PP.txt')
    p.rename(p.with_suffix('.asm'))
        
    #Lancio del compilatore da shell (l'output è salvato in un file .txt temporaneo)
    os.chdir(output_dir)
    os.system("nasm -f bin PR_PP.asm -o PR_PP.obj 2>> tempFilePR_PP.txt")
    
    #Controllo se .asm fa riferimento ad un'architettura 64bit
    if(os.stat("tempFilePR_PP.txt").st_size != 0):
    
        #Lettura del contenuto del file temporaneo e conversione in lista di output
    
        output_NASMcompiler = open(output_dir+"/tempFilePR_PP.txt", 'r')
        list_output_NASMcompiler = output_NASMcompiler.readlines()
        output_NASMcompiler.close()
    
        #Si itera sulla lista di output
    
        for k in range(len(list_output_NASMcompiler)):
        
            #Conversione in stringa del k-esimo output e conversione in lista splittando con ' '
        
            str_output_NASMcompiler = str(list_output_NASMcompiler[k])
            list_splitted_output_NASMcompiler = str_output_NASMcompiler.split(' ')
                        
            #Si verifica che non sia una warning o un simbolo non definito. 
            #In caso contrario, si setta la variabile di controllo a True
    
            if(list_splitted_output_NASMcompiler[2] == "symbol"):
                if(list_splitted_output_NASMcompiler[4] == "not"):
                    if(list_splitted_output_NASMcompiler[5] == "defined\n"):
                        str_symbol = list_splitted_output_NASMcompiler[3]
                        str_symbol = str_symbol.replace("'","")
                        str_symbol = str_symbol[1:]
                        list_symbolsPR.append(str_symbol)

    ########################################################################        

    if(len(list_symbolsGT) == len(list_symbolsPR)):
        
        for p in range(len(list_symbolsGT)):
            if(list_symbolsGT[p] == list_symbolsPR[p] or
               "_"+list_symbolsGT[p] == list_symbolsPR[p] or
               list_symbolsGT[p] == "_"+list_symbolsPR[p]):
                changeScore = False
            else:
                changeScore = True
    else:
        changeScore = True         
        
     
    if os.path.isfile(output_dir + "/tempFileGT_PP.txt"):
        os.remove(output_dir + "/tempFileGT_PP.txt")

    if os.path.isfile(output_dir + "/GT_PP.obj"):
        os.remove(output_dir + "/GT_PP.obj")

    if os.path.isfile(output_dir + "/tempFilePR_PP.txt"):
        os.remove(output_dir + "/tempFilePR_PP.txt")

    if os.path.isfile(output_dir + "/PR_PP.obj"):
        os.remove(output_dir + "/PR_PP.obj")

    if os.path.isfile(output_dir + "/GT_PP.asm"):
        os.remove(output_dir + "/GT_PP.asm")

    if os.path.isfile(output_dir + "/PR_PP.asm"):
        os.remove(output_dir + "/PR_PP.asm")

    return changeScore
        
def postProcessingL(str_GT, str_PR, output_dir):
    
    changeScore = False
    
    checkGTSymbols = True
    checkPRSymbols = True
    
    interrupt = False
    
    fil_str_gt = str_GT.replace("[", " ").replace("]"," ").replace(",", " ").replace("+"," ").replace("-"," ").replace("  "," ")
    fil_str_pr = str_PR.replace("[", " ").replace("]"," ").replace(",", " ").replace("+"," ").replace("-"," ").replace("  "," ")
    
    list_fil_str_gt = fil_str_gt.split(" ")
    list_fil_str_pr = fil_str_pr.split(" ")
    
    listSymExeSymbols = ["eax", "rax", "ax", "ah", "al",
                         "ebx", "rbx", "bx", "bh", "bl",
                         "ecx", "rcx", "cx", "ch", "cl",
                         "edx", "rdx", "dx", "dh", "dl",
                         "esp", "rsp", "sp", "spl",
                         "edi", "rdi", "di", "dil",
                         "esi", "rsi", "si", "sil",
                         "ebp", "rbp", "bp", "bpl",
                         "push", "pop"]
    
    checkGTSymbols = any(item in list_fil_str_gt for item in listSymExeSymbols)
    checkPRSymbols = any(item in list_fil_str_pr for item in listSymExeSymbols)
            
    ###Gestione interruzioni

    addrintGT = ""
    addrintPR = ""
    addrintGTclean = ""
    addrintPRclean = ""
        
    
    list_snippetsGT_spllited_by_backslash = []
    list_snippetsGT_spllited_by_backslash = str_GT.split('\\n ')    
    
    for j in range(len(list_snippetsGT_spllited_by_backslash)):
        list_snippetsGT_spllited_by_backslash[j] = list_snippetsGT_spllited_by_backslash[j].replace('\\', '')
    
    for k in range(len(list_snippetsGT_spllited_by_backslash)):
        
        if(str(list_snippetsGT_spllited_by_backslash[k]).split(" ")[0] == "int"):
            addrintGT = str(list_snippetsGT_spllited_by_backslash[k]).split(" ")[1]
            if(addrintGT[:2] == '0x'):
                addrintGTclean = addrintGT.replace("0x","")
            elif(addrintGT[-1:] == 'h'):
                addrintGTclean = addrintGT.replace("h","")
                 
    list_snippetsPR_spllited_by_backslash = []
    list_snippetsPR_spllited_by_backslash = str_PR.split('\\n ')    
    
    for j in range(len(list_snippetsPR_spllited_by_backslash)):
        list_snippetsPR_spllited_by_backslash[j] = list_snippetsPR_spllited_by_backslash[j].replace('\\', '')
    
    for k in range(len(list_snippetsPR_spllited_by_backslash)):
        
        if(str(list_snippetsPR_spllited_by_backslash[k]).split(" ")[0] == "int"):
            addrintPR = str(list_snippetsPR_spllited_by_backslash[k]).split(" ")[1]
            if(addrintPR[:2] == '0x'):
                addrintPRclean = addrintPR.replace("0x","")
            elif(addrintPR[-1:] == 'h'):
                addrintPRclean = addrintPR.replace("h","")

    if(addrintGTclean != "" or addrintPRclean != ""):
        
        interrupt = True
        
        if(addrintGTclean != addrintPRclean):
            print("changeScore")
            changeScore = True
        else:
            changeScore = False

    ###################

    if(interrupt == False):
        
        if(checkGTSymbols == True and checkPRSymbols == True):
        
            changeScore = False
        
        else:
            
            list_str_GT = str_GT.split(" ")
            list_str_PR = str_PR.split(" ")
    
            if(len(list_str_GT) == len(list_str_PR)):
                
                for l in range(len(list_str_GT)):
                    
                    if(list_str_GT[l] != list_str_PR[l] and "_"+list_str_GT[l] != list_str_PR[l] and list_str_GT[l] != "_"+list_str_PR[l]):
                        changeScore = True
                        
            else:
                changeScore = True
    
    return changeScore
    
def verifySND(nameEXE, str_symbol, list_snippetsGR_spllited_by_backslash, elf64, output_dir):
    
    error = False
    
    if os.path.isfile(output_dir + "/tempFile.txt"):
        os.remove(output_dir + "/tempFile.txt")
    
    os.chdir(output_dir)
    if(elf64 == False):
        os.system("nasm -f elf32 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")
    else:
        os.system("nasm -f elf64 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")    

    if(os.stat("tempFile.txt").st_size == 0):
        
        if(elf64 == False):
            os.system("ld -m i386pe -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj.txt")
        else:
            os.system("ld -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj.txt")
    
        if(os.stat("debugObj.txt").st_size != 0):
            
            os.remove(output_dir + "/"+ nameEXE + ".asm")
            
            os.remove(output_dir + "/debugObj.txt")
            
            if os.path.isfile(output_dir + "/tempFile.txt"):
                os.remove(output_dir + "/tempFile.txt")
            
            with open(output_dir + '/'+ nameEXE +'.txt', 'w') as f:
                                
                f.write('section .data')
                f.write('\n\n')
                f.write(str_symbol + " equ 0x42")
                f.write("\n")
                f.write('myExitAddr db 0x56')
                f.write('\n\n')
                f.write('section .text')
                f.write('\n\n')
                f.write('global my_start')
                f.write('\n\n')
                f.write('my_start:')
                f.write('\n\n')
                
                for z in range(len(list_snippetsGR_spllited_by_backslash)):
                    f.write("        "+list_snippetsGR_spllited_by_backslash[z])
                    f.write("\n")
                      
                f.write("        jmp myExitAddr")
                f.close()
                
                p = Path(output_dir + '/'+ nameEXE +'.txt')
                p.rename(p.with_suffix('.asm'))
                
                if(elf64 == False):
                    os.system("nasm -f elf32 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile1.txt")
                else:
                    os.system("nasm -f elf64 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile1.txt")    

                if(os.stat("tempFile1.txt").st_size != 0):
                    error = True
                else:
                                        
                    if(elf64 == False):
                        os.system("ld -m i386pe -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj1.txt")
                    else:
                        os.system("ld -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj1.txt")
                
                    if(os.stat("debugObj1.txt").st_size != 0):
                        error = True
                               
                    if os.path.isfile(output_dir + "/tempFile1.txt"):
                        os.remove(output_dir + "/tempFile1.txt")
                
                    if os.path.isfile(output_dir + "/debugObj1.txt"):
                        os.remove(output_dir + "/debugObj1.txt")
                                                            
    else:
        error = True
                        
    return error

def genEXE(snippet, nameEXE, output_dir):
    
    esecuzioneTerminata = True
        
    list_snippetsGR_spllited_by_backslash = []
    list_snippetsGR_spllited_by_backslash = snippet.split('\\n ')    
    
    for j in range(len(list_snippetsGR_spllited_by_backslash)):
        list_snippetsGR_spllited_by_backslash[j] = list_snippetsGR_spllited_by_backslash[j].replace('\\', '')

    #Creazione scrittura su un file di testo e conversione a .asm
    
    with open(output_dir + '/'+ nameEXE +'.txt', 'w') as f:
        
        f.write('section .data')
        f.write('\n\n')
        f.write('myExitAddr db 0x56')
        f.write('\n\n')
        f.write('section .text')
        f.write('\n\n')
        f.write('global my_start')
        f.write('\n\n')
        f.write('my_start:')
        f.write('\n\n')
        
        for z in range(len(list_snippetsGR_spllited_by_backslash)):
            if(str(list_snippetsGR_spllited_by_backslash[z]).split(" ")[0] != "int"):
                f.write("        "+list_snippetsGR_spllited_by_backslash[z])
                f.write("\n")
              
        f.write("        jmp myExitAddr")
        f.close()

    p = Path(output_dir + '/'+ nameEXE +'.txt')
    p.rename(p.with_suffix('.asm'))

    elf64 = False
        
    #Lancio del compilatore da shell (l'output è salvato in un file .txt temporaneo)
    os.chdir(output_dir)
    os.system("nasm -f elf32 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")
    
    #Controllo se .asm fa riferimento ad un'architettura 64bit
    if(os.stat("tempFile.txt").st_size != 0):
        
        output_NASMcompiler = open(output_dir+"/tempFile.txt", 'r')
        str_output_NASMcompiler = output_NASMcompiler.read()
        output_NASMcompiler.close()
        
        str_output_NASMcompiler = str_output_NASMcompiler.split(' ', 1)[1]
        
        if(str_output_NASMcompiler.replace("\n","") == "error: instruction not supported in 32-bit mode"):            
            elf64 = True
                        
            #os.remove(output_dir + "/tempFile.txt")
            
            os.system("nasm -f elf64 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")            
                   
    if(os.stat("tempFile.txt").st_size == 0):
        
        os.chdir(output_dir)
        if(elf64 == False):
            os.system("ld -m i386pe -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj.txt")
        else:
            os.system("ld -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj.txt")
            
        #debug.obj
        if(os.stat("debugObj.txt").st_size != 0):
            # debugObj = open(output_dir +"/debugObj.txt", 'r')
            # print("\n")
            # print(i)
            # print(debugObj.read())
            # prova.append(str_output_NASMcompiler)
            # debugObj.close()
            esecuzioneTerminata = False
            
    else:
        
        #Lettura del contenuto del file temporaneo e conversione in lista di output
        
        output_NASMcompiler = open(output_dir+"/tempFile.txt", 'r')
        list_output_NASMcompiler = output_NASMcompiler.readlines()
        output_NASMcompiler.close()
    
        #Variabile booleana di controllo
        error = False
        
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
                            str_symbol = list_splitted_output_NASMcompiler[3]
                            str_symbol = str_symbol.replace("'","")
                            str_symbol = str_symbol[1:]
                            with open(output_dir + "/"+nameEXE+".asm", "a+") as f:
                                f.write('\n')
                                f.write(str_symbol + ":")
                                f.write('\n\n')
                                f.write('inc eax')
                                f.write('\n\n')
                                f.write('jmp myExitAddr')
                                f.close()
                            error = verifySND(nameEXE, str_symbol, list_snippetsGR_spllited_by_backslash, elf64, output_dir)
                    else:
                        error = True
                else :
                    error = True

        #Verifica della presenza di errori e calcolo dei risultati
        
        if(error == False):
            
            os.chdir(output_dir)
            
            if(elf64 == False):
                os.system("nasm -f elf32 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")
            
                #Controllo nuovamente se .asm fa riferimento ad un'architettura 64bit
                if(os.stat("tempFile.txt").st_size != 0):
                    
                    output_NASMcompiler = open(output_dir+"/tempFile.txt", 'r')
                    str_output_NASMcompiler = output_NASMcompiler.read()
                    output_NASMcompiler.close()
                    
                    str_output_NASMcompiler = str_output_NASMcompiler.split(' ', 1)[1]
                    
                    if(str_output_NASMcompiler == "error: instruction not supported in 32-bit mode\n"):
                        
                        os.remove(output_dir + "/tempFile.txt") 
                        os.remove(output_dir + "/debugObj.txt")
                        
                        os.system("nasm -f elf64 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")            
            else:
                os.system("nasm -f elf64 "+ nameEXE + ".asm -o "+ nameEXE +".obj 2>> tempFile.txt")
                
            if(elf64 == False):
                os.system("ld -m i386pe -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj.txt")
            else:
                os.system("ld -o "+ nameEXE + ".exe "+ nameEXE +".obj 2>> debugObj.txt")

            #debug.obj
            if(os.stat("debugObj.txt").st_size != 0):
                # debugObj = open(output_dir +"/debugObj.txt", 'r')
                # print("\n")
                # print(i)
                # print(debugObj.read())
                # prova.append(str_output_NASMcompiler)
                # debugObj.close()
                esecuzioneTerminata = False
        else:
            #print("\n")
            #print(snippet)
            esecuzioneTerminata = False
        
        #Chiusura e rimozione del file temporaneo            
        output_NASMcompiler.close()
                    
    #Rimozione dei file precedentemente creati            
    # if os.path.isfile(output_dir + "/"+ nameEXE +".asm"):
    #     os.remove(output_dir + "/"+ nameEXE +".asm")

    # if os.path.isfile(output_dir + "/"+ nameEXE +".obj"):
    #     os.remove(output_dir + "/"+ nameEXE +".obj")
    
    # if os.path.isfile(output_dir + "/tempFile.txt"):
    #     os.remove(output_dir + "/tempFile.txt")

    # if os.path.isfile(output_dir + "/debugObj.txt"):
    #     os.remove(output_dir + "/debugObj.txt")
    
    return esecuzioneTerminata
       
def print_state(simgr):
       
    for i in range(len(simgr.active)):
        print("RAMO '" + str(i+1) +"': "+ str(simgr.active[i]))
        print("Contenuto di eax: " + str(simgr.active[i].regs.eax))
        print("Contenuto di ecx: " + str(simgr.active[i].regs.ecx))
        print("Contenuto di esp: " + str(simgr.active[i].regs.esp))
        print("Contenuto di esi: " + str(simgr.active[i].regs.esi))
        print("Contenuto di ebp: " + str(simgr.active[i].regs.ebp))
        print("Contenuto di edi: " + str(simgr.active[i].regs.edi))
        print("Flags cc_op: " + str(simgr.active[i].regs.cc_op))
        print("Flags cc_dep1: " + str(simgr.active[i].regs.cc_dep1))
        print("Flags cc_dep2: " + str(simgr.active[i].regs.cc_dep2))
        print("Constraint: "+ str(simgr.active[i].solver.constraints))
        print("History: "+ str(simgr.active[i].history))
        print("\n")

def stepAll(simgr, MaxStep):
    
    notFinished = True
    count = 0

    while(notFinished and count < MaxStep):
        
        count = count + 1
        
        result = all(str(element) == '<SimState @ 0x402000>' for element in simgr.active)
        
        if(result):
            notFinished = False
        else:
            simgr.step()
  
def checkSimilarity(simgr1, simgr2, state1, state2, initialSP_simgr1, initialSP_simgr2):
        
    check = True
    
    for i in range(len(simgr2.active)):
        
        listRegistersAndConstraints2 = []
        listFlags2 = []
        listStack2 = []
        
        for k in range(len(simgr2.active[i].solver.constraints)):
            listRegistersAndConstraints2.append(simgr2.active[i].solver.constraints[k])
                
        if(state1.arch.name == 'X86' and state2.arch.name == 'X86'):
            listRegistersAndConstraints2.append(simgr2.active[i].regs.eax)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.ebx)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.ecx)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.edx)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.esi)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.ebp)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.edi)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.esp)
            listFlags2.append(simgr2.active[i].regs.cc_dep1)
            listFlags2.append(simgr2.active[i].regs.cc_dep2)

        else:
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rax)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rbx)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rcx)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rdx)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rsi)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rbp)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rdi)
            listRegistersAndConstraints2.append(simgr2.active[i].regs.rsp)
            listFlags2.append(simgr2.active[i].regs.cc_dep1)
            listFlags2.append(simgr2.active[i].regs.cc_dep2)

            
        listComparisonRegisterAndConstraints = []
        listComparisonFlag = []
        listComparisonStack = []
        
        finalSP_simgr2 = simgr2.active[i].regs.esp
        
        if(finalSP_simgr2.symbolic == False):
            
            finalSP_simgr2 = ((str(finalSP_simgr2).split(" "))[1].replace("]", "").replace(">", ""))
            
            if(initialSP_simgr2 != finalSP_simgr2):
                        
                maxSPIndex = max(int(initialSP_simgr2,0), int(finalSP_simgr2,0))
                minSPIndex = min(int(initialSP_simgr2,0), int(finalSP_simgr2,0))
            
                outStack = 0
            
                for h in range(minSPIndex, maxSPIndex+1):
                    outStack = outStack + 1
                    listStack2.append(simgr2.active[i].mem[h].int.resolved)
                    if(outStack > 1000):
                        break
                
        for j in range(len(simgr1.active)):
                
            listRegistersAndConstraints1 = []
            listFlags1 = []
            listStack1 = []
            
            for l in range(len(simgr1.active[j].solver.constraints)):
                listRegistersAndConstraints1.append(simgr1.active[j].solver.constraints[l])
            
            if(state1.arch.name == 'X86' and state2.arch.name == 'X86'):
                listRegistersAndConstraints1.append(simgr1.active[j].regs.eax)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.ebx)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.ecx)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.edx)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.esi)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.ebp)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.edi)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.esp)
                listFlags1.append(simgr1.active[j].regs.cc_dep1)
                listFlags1.append(simgr1.active[j].regs.cc_dep2)

            else:
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rax)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rbx)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rcx)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rdx)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rsi)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rbp)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rdi)
                listRegistersAndConstraints1.append(simgr1.active[j].regs.rsp)
                listFlags1.append(simgr1.active[j].regs.cc_dep1)
                listFlags1.append(simgr1.active[j].regs.cc_dep2)

            finalSP_simgr1 = simgr1.active[j].regs.esp
            
            if(finalSP_simgr1.symbolic == False):
                
                finalSP_simgr1 = ((str(finalSP_simgr1).split(" "))[1].replace("]", "").replace(">", ""))
                
                if(initialSP_simgr1 != finalSP_simgr1):
                
                    maxSPIndex = max(int(initialSP_simgr1,0), int(finalSP_simgr1,0))
                    minSPIndex = min(int(initialSP_simgr1,0), int(finalSP_simgr1,0))
                
                    outStack = 0

                    for h in range(minSPIndex, maxSPIndex+1):
                        outStack = outStack + 1
                        listStack1.append(simgr1.active[j].mem[h].int.resolved)
                        if(outStack > 1000):
                            break
                            
            listComparisonRegisterAndConstraints.append(collections.Counter(listRegistersAndConstraints1) == collections.Counter(listRegistersAndConstraints2))
            listComparisonFlag.append(collections.Counter(listFlags1) == collections.Counter(listFlags2))
            listComparisonStack.append(collections.Counter(listStack1) == collections.Counter(listStack2))

        if(not(True in listComparisonRegisterAndConstraints) or 
           not(True in listComparisonFlag) or
           not(True in listComparisonStack)):
            check = False
            break

    return check    

def semantic_similarity(dir1, dir2):

    proj1 = angr.Project(dir1)
    proj2 = angr.Project(dir2)
    
    state1 = proj1.factory.entry_state()
    state2 = proj2.factory.entry_state()
    
    simgr1 = proj1.factory.simulation_manager()
    simgr2 = proj2.factory.simulation_manager()
    
    #Inizializzazioni in base all'architettura dei due snippet
    if(state1.arch.name == 'X86' and state2.arch.name == 'X86'):
        
        eax = claripy.BVS("eax", 32)
        simgr1.active[0].regs.eax = eax
        simgr2.active[0].regs.eax = eax
        
        ebx = claripy.BVS("ebx", 32)
        simgr1.active[0].regs.ebx = ebx
        simgr2.active[0].regs.ebx = ebx
        
        ecx = claripy.BVS("ecx", 32)
        simgr1.active[0].regs.ecx = ecx
        simgr2.active[0].regs.ecx = ecx
        
        edx = claripy.BVS("edx", 32)
        simgr1.active[0].regs.edx = edx
        simgr2.active[0].regs.edx = edx
    
        esi = claripy.BVS("esi", 32)
        simgr1.active[0].regs.esi = esi
        simgr2.active[0].regs.esi = esi
        
        ebp = claripy.BVS("ebp", 32)
        simgr1.active[0].regs.ebp = ebp
        simgr2.active[0].regs.ebp = ebp
        
        edi = claripy.BVS("edi", 32)
        simgr1.active[0].regs.edi = edi
        simgr2.active[0].regs.edi = edi
        
        cc_dep1 = claripy.BVS("cc_dep1", 32)
        simgr1.active[0].regs.cc_dep1 = cc_dep1
        simgr2.active[0].regs.cc_dep1 = cc_dep1

        cc_dep2 = claripy.BVS("cc_dep2", 32)
        simgr1.active[0].regs.cc_dep2 = cc_dep2
        simgr2.active[0].regs.cc_dep2 = cc_dep2
        
        # cc_op = claripy.BVS("cc_op", 32)
        # simgr1.active[0].regs.cc_op = cc_op
        # simgr2.active[0].regs.cc_op = cc_op
        
    else:
        
        rax = claripy.BVS("rax", 64)
        simgr1.active[0].regs.rax = rax
        simgr2.active[0].regs.rax = rax
        
        rbx = claripy.BVS("rbx", 64)
        simgr1.active[0].regs.rbx = rbx
        simgr2.active[0].regs.rbx = rbx
        
        rcx = claripy.BVS("rcx", 64)
        simgr1.active[0].regs.rcx = rcx
        simgr2.active[0].regs.rcx = rcx
        
        rdx = claripy.BVS("rdx", 64)
        simgr1.active[0].regs.rdx = rdx
        simgr2.active[0].regs.rdx = rdx
        
        rsi = claripy.BVS("rsi", 64)
        simgr1.active[0].regs.rsi = rsi
        simgr2.active[0].regs.rsi = rsi
            
        rbp = claripy.BVS("rbp", 64)
        simgr1.active[0].regs.rbp = rbp
        simgr2.active[0].regs.rbp = rbp
        
        rdi = claripy.BVS("rdi", 64)
        simgr1.active[0].regs.rdi = rdi
        simgr2.active[0].regs.rdi = rdi
        
        cc_dep1 = claripy.BVS("cc_dep1", 64)
        simgr1.active[0].regs.cc_dep1 = cc_dep1
        simgr2.active[0].regs.cc_dep1 = cc_dep1

        cc_dep2 = claripy.BVS("cc_dep2", 64)
        simgr1.active[0].regs.cc_dep2 = cc_dep2
        simgr2.active[0].regs.cc_dep2 = cc_dep2
        
        # cc_op = claripy.BVS("cc_op", 64)
        # simgr1.active[0].regs.cc_op = cc_op
        # simgr2.active[0].regs.cc_op = cc_op
    
    initialSP_simgr1 = ((str(simgr1.active[0].regs.esp).split(" "))[1].replace("]", "").replace(">", ""))
    initialSP_simgr2 = ((str(simgr2.active[0].regs.esp).split(" "))[1].replace("]", "").replace(">", ""))
    
    MaxStep = 100
    
    #Esecuzione simgr1
    stepAll(simgr1, MaxStep)
    #print_state(simgr1)
    
    #Esecuzione simgr2
    stepAll(simgr2, MaxStep)
    #print_state(simgr2)
    
    #print("Check Constraints: " + str(checkConstraints(simgr1, simgr2)))
    #print("Check Registers: " + str(checkRegisters(simgr1, simgr2)))
    
    if(checkSimilarity(simgr1, simgr2, state1, state2, initialSP_simgr1, initialSP_simgr2) == True):
        #print("Similarità semantica verificata")
        return True
    else:
        #print("Similarità semantica non verificata")
        return False
   
this_directory = os.getcwd()

root = tk.Tk()
root.withdraw()

input_file = filedialog.askopenfile(initialdir= os.path.join(this_directory, os.path.join("Output", "Output_Syntactic_Analysis")), 
                                          title = "Select the Syntactic Correctness results file")

output_Folder = "Output_Semantic_Analysis"
output_dir = os.path.join(this_directory, os.path.join("Output", output_Folder))

syntactic_results = os.path.join(this_directory, input_file.name)

data = pd.read_csv(syntactic_results, sep = ";", engine='python')

#Inizializzazioni
num_semantic_correct = 0
total = 0

list_gt = []
list_pr = []

list_errorGenEXEGT = []
list_errorGenEXEPR = []

score = []

nameFile = "_".join((((input_file.name).split("/")[-1]).split(".")[0]).split("_")[3:])

results_folder = os.path.join(output_dir, nameFile)

if not os.path.exists(results_folder):
    os.mkdir(results_folder)

genEXE_folder = os.path.join(results_folder, "GenEXE Errors")

if not os.path.exists(genEXE_folder):
    os.mkdir(genEXE_folder)

####### Operazioni preliminari #######

for i in tqdm(range(data["Ground Truth Snippets"].size)):
        
    list_gt.append(str(data["Ground Truth Snippets"][i]))
    list_pr.append(str(data["Predicted Snippets"][i]))
    
    if(str(data["Score Syntax"][i]) == "0"):
        total = total + 1
        score.append(0)
        
    elif((str(data["Ground Truth Snippets"][i]) == str(data["Predicted Snippets"][i])) or
         (str(data["Ground Truth Snippets"][i]).replace(" ","").replace("\\n", "").replace("\n","") == str(data["Predicted Snippets"][i]).replace(" ","").replace("\\n", "").replace("\n",""))):
        num_semantic_correct = num_semantic_correct + 1 
        total = total + 1
        
        score.append(1)
        
    else:
        
        str_snippetGT = str(data["Ground Truth Snippets"][i])
        str_snippetPR = str(data["Predicted Snippets"][i])
        
        path = os.path.join(genEXE_folder, "executables")
        
        if(not(os.path.exists(path))):
            os.mkdir(path)

        checkGenEXEGT = genEXE(str_snippetGT, "GT_"+str(i+1), path)
        checkGenEXEPR = genEXE(str_snippetPR, "PR_"+str(i+1), path)

        #print(str_snippetGT, " + ", checkGenEXEGT)
        #print(str_snippetPR, " + ", checkGenEXEPR)

        
        if(checkGenEXEGT == checkGenEXEPR == True):
            total = total + 1
                
            if(semantic_similarity(path+"/GT_"+str(i+1)+".exe", path+"/PR_"+str(i+1)+".exe") == True):
                num_semantic_correct = num_semantic_correct + 1 
                score.append(1)
            else:
                score.append(0)
        else:
             list_errorGenEXEGT.append(str(data["Ground Truth Snippets"][i]))
             list_errorGenEXEPR.append(str(data["Predicted Snippets"][i]))
                   
             if(checkGenEXEGT == False):
                 score.append("GT: errorGenEXE")
             else:
                 score.append("PR: errorGenEXE")
        
dict_ris = {'Ground Truth Snippets' : list_gt, 'Predicted Snippets' : list_pr, 'Score Semantic Equivalence' : score}
df_ris = pd.DataFrame(dict_ris)

#shutil.rmtree(path, ignore_errors = True)

print("Start of post-processing operations...")

for i in tqdm(range(df_ris["Ground Truth Snippets"].size)):
    
    if(str(df_ris['Score Semantic Equivalence'][i]) == str('1')):
    
        changeScore = postProcessingSND(str(df_ris['Ground Truth Snippets'][i]), str(df_ris['Predicted Snippets'][i]), output_dir)

        if(changeScore == True):
            print(df_ris["Ground Truth Snippets"][i])
            df_ris['Score Semantic Equivalence'][i] = 0  
            num_semantic_correct = num_semantic_correct - 1
                
for i in tqdm(range(df_ris["Ground Truth Snippets"].size)):
    
    if(str(df_ris['Score Semantic Equivalence'][i]) == str('1')):
    
        changeScore = postProcessingL(str(df_ris['Ground Truth Snippets'][i]), str(df_ris['Predicted Snippets'][i]), output_dir)

        if(changeScore == True):
            df_ris['Score Semantic Equivalence'][i] = 0    
            num_semantic_correct = num_semantic_correct - 1            
            
sum_ris = 0

for i in range(df_ris["Ground Truth Snippets"].size):
    
    if(str(df_ris['Score Semantic Equivalence'][i]) == str('1') or
       str(df_ris['Score Semantic Equivalence'][i]) == str('0')):
        
        sum_ris = sum_ris + int(df_ris['Score Semantic Equivalence'][i])

total_size=df_ris["Ground Truth Snippets"].size

print("\n\n")        
print("Semantic Equivalence = " +str((sum_ris/total_size)*100)+"%")

dict_error = {'Ground Truth Snippets ErrorGENEXE' : list_errorGenEXEGT, 'Predicted Snippets ErrorGENEXE' : list_errorGenEXEPR}
df_error = pd.DataFrame(dict_error)
df_error.to_csv(os.path.join(genEXE_folder, "Errors GenEXE.csv"), index=False, sep = ";")

df_ris.to_csv(os.path.join(results_folder, "output_semantic_equivalence_"+str(nameFile)+".csv"), index=False, sep = ";")
