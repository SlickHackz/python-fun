import codecs
import glob
import hashlib
import os
import re
import sys
import shutil
import subprocess
import tempfile
import time
import _winreg
import logging
import ctypes
from ctypes import wintypes, windll

##  CONSTANTS DEFINITION

WORKING_INPUT_DIR=r"C:\working\input"
WORKING_OUTPUT_DIR=r"C:\working\output"
WORKING_DIR=r"C:\working"

##  Please use the below template for Documenting the usage of the function
"""
=====================================================================================================
 @brief                        

 @param   

 @returns 

 @exception
======================================================================================================
"""


class DINGUTL(object):
## Data member

## Function member

    def __init__ (self):
        self.Infile=Infile
        self.Outfile=Outfile
		
	## Registry Operations
	
    def GetRegistryKeyData(self, MainKey, SubKey, KeyName):
        return self.GetRegistryKeyData(MainKey, SubKey, KeyName)

    def SetRegistryKeyData(self, MainKey, SubKey, KeyName, KeyType, KeyData):
        return self.SetRegistryKeyData(MainKey, SubKey, KeyName, KeyType, KeyData)

    def DeleteRegistryKey(self, MainKey, KeyNamePath, KeyNameDel):
        return self.DeleteRegistryKey(MainKey, KeyNamePath, KeyNameDel)

    def CreateRegistryKey(self, MainKey, SubKey, KeyName):
        return self.CreateRegistryKey(MainKey, SubKey, KeyName)	
        
    def UniToAnsi(self, Infile, Outfile):
        return self.UniToAnsi(self.Infile, self.Outfile)

    def SplitUrlLine(self, Outfile):
        return self.SplitUrlLine(self.Outfile)

    def DefaultToDesktop(self):
        return self.DefaultToDesktop()



    def GetSingleProdSiloKey(self):
        return self.GetSingleProdSiloKey()
	
	## Finding OS Nomenclature

    def WinOSInfo(self):
        return self.WinOSInfo()

    def Is32Bit(self):
        return self.Is32Bit()

    def Is64Bit(self):
        return self.Is64Bit()

    def IsWinXP(self):
        return self.IsWinXP()

    def IsWinVista(self):
        return self.IsWinVista()

    def IsWin7(self):
        return self.IsWin7()

    def IsWin8(self):
        return self.IsWin8()

    def IsWin8_1(self):
        return self.IsWin8_1()
	
	## Killing Products

    def KillNTPUser(self):
        return self.KillNTPUser()

    def KillNTPSystem(self):
        return self.KillNTPSystem()

    def KillProductUser(self):
        return self.KillProductUser()

    def KillProductSystem(self):
        return self.KillProductSystem()

    def LatInstLog(self,dest):
        return self.LatInstLog()

    def IsEmpty(self,dir):
        return self.IsEmpty()

    def GetDatafromPathExpansionMap(self,KeyName):
        return self.GetDatafromPathExpansionMap(KeyName)

    def GetMD5FileHash(self,fPath):
        return self.GetMD5FileHash(fPath)

    def GetInstallBrandMD5FileHash(self):
        return self.GetInstallBrandMD5FileHash()

    def GetNTPProductBrandMD5FileHash(self):
        return self.GetNTPProductBrandMD5FileHash()

    def RootCertUpdOnXP(self):
        return self.RootCertUpdOnXP()

    def GetCommonAppDataPath(self):
        return self.GetCommonAppDataPath()

    def GetCommonProgramFilesPath(self):
        return self.GetCommonProgramFilesPath()

    def GetDefaultWindowsOSDriver(self):
        return self.GetDefaultWindowsOSDriver()

    def CopyNortonLogs(self):
        return self.CopyNortonLogs()

    def DisableNetworkAdapter(self):
        return self.DisableNetworkAdapter()

    def EnableNetworkAdapter(self):
        return self.EnableNetworkAdapter()
        
    def GetFileSize(self,file):
        return self.GetFileSize(file)

    def StartNTPService(self):
        return self.StartNTPService()
    
    def GetAnyWindowsPath(self,num):
        return self.GetAnyWindowsPath(num)
       
    def CreateNTPIsolateINI(self,folder):
        return self.CreateNTPIsolateINI(folder)

    def CreateProductIsolateINI(self,folder):
        return self.CreateProductIsolateINI(folder)

    def RegExSearchInStringOrFile(self,pattern, file_or_string_to_search):
        return self.RegExSearchInStringOrFile(pattern, file_or_string_to_search)

    def RegExMatchInStringOrFile(self, pattern, file_or_string_to_search):
        return self.RegExMatchInStringOrFile(pattern, file_or_string_to_search)

    def SearchRecurforCount(self,FolderPath,SearchStr):
        return self.SearchRecurforCount(FolderPath,SearchStr)


		
	## Norton Product Specific Functions! You can't try them! Sorry! I haven't exposed the implemention here
	
	
	def TestModeExtractor(self,SetupPath):
        return self.TestModeExtractor(SetupPath)
	
    def VerifyAppliedCustomPackage(self):
        return self.VerifyAppliedCustomPackage()

    def ApplyCustomPackageFlavor(self):
        return self.ApplyCustomPackageFlavor()
		
    def IsLiveInstallPing(self, Url):
        return self.IsLiveInstallPing(Url)

    def IsCustomPackagePing(self,Url):
        return self.IsCustomPackagePing(Url)	

    def DumpInstallDATtoTextFile(self):
        return self.DumpInstallDATtoTextFile()

    def ParseInstallDAT(self,Key):
        return self.ParseInstallDAT(Key)		
		
    def SymProtectStatus(self):
        return self.SymProtectStatus()

    def SymProtectON(self):
        return self.SymProtectON()

    def SymProtectOFF(self):
        return self.SymProtectOFF()		
		
    def StagePatchWithInstallEngineTest(self, InstEngTest, ENGPatch7z, MUIPatch7z, MUIimagePatch7z, BRANDPatch7z):
        return self.StagePatchWithInstallEngineTest(InstEngTest, ENGPatch7z, MUIPatch7z, MUIimagePatch7z, BRANDPatch7z)

    def ApplyPatch(self):
        return self.ApplyPatch()

    def ApplyUpgradeInstall(self):
        return self.ApplyUpgradeInstall()

    def IsNTPServicePluginLoaded(self):
        return self.IsNTPServicePluginLoaded()	

    def SupressDingTestProductCallbackMsg(self):
        return self.SupressDingTestProductCallbackMsg()

    def SilentInstall(self, sPath):
        return self.SilentInstall(sPath)

    def RebootlessUpgrade(self, sPath1, sPath2):
        return self.RebootlessUpgrade(sPath1, sPath2)

    def SeamlessUpgrade(self, sPath1, sPath2):
        return self.SeamlessUpgrade(sPath1, sPath2)

    def IsInstallPing(self, Url):
        return self.IsInstall(Url)

    def IsUnInstallPing(self, Url):
        return self.IsUnInstall(Url)

    def IsPatchPing(self, Url):
        return self.IsPatchPing(Url)

    def IsUpgradePing(self, Url):
        return self.IsUpgradePing(Url)

    def SearchRecurNortonLogsforCount(self,SearchStr):
        return self.SearchRecurNortonLogsforCount(SearchStr)

    def SearchRecurRebootlessLogsforCount(self,SearchStr):
        return self.SearchRecurRebootlessLogsforCount(SearchStr)

    def SearchRecurPatchLogsforCount(self,SearchStr):
        return self.SearchRecurPatchLogsforCount(SearchStr)

    def SearchRecurFlavorLogsforCount(self,SearchStr):
        return self.SearchRecurFlavorLogsforCount(SearchStr)

##=====================================================================================================
## @brief           Initialize_Logger
##                  debug
##                  info
##                  warning
##                  error
##                  critical
##
## @param           Output_Dir  
##
## @returns         
##
## @exception       
##======================================================================================================

def Initialize_Logger(Output_dir=WORKING_OUTPUT_DIR):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG) 
    # create debug file handler and set level to debug
    handler = logging.FileHandler(os.path.join(Output_dir, "DINGUTL.log"),"a")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

##================================================================================================================================
## @brief           VerifyFileSignature verifies signature of a File
##
##                  Require sigcheck.exe tool is under c:\working\input                       
##
## @param           File to be verified  
##
## @returns         True
##                  False 
##
## @exception       return str(e)   = Exception Error
##================================================================================================================================
def VerifyFileSignature(File):
    try:
        logging.info("DINGUTL:"+"---START VerifyFileSignature()---")
        SigCheckfile = tempfile.gettempdir() + "\\SigCheck.txt"
        if os.path.exists(SigCheckfile):
            os.remove(SigCheckfile)
        if File and os.path.exists(File):
            if os.path.exists(WORKING_INPUT_DIR+"\\"+ "sigcheck.exe"):    
                cmd=r"C:\working\input\sigcheck.exe" +" -q"+ " -e " + File+ " >>" + SigCheckfile
                RetCode=subprocess.call(cmd,shell=True)
                if RetCode!=0:
                    logging.info("DINGUTL:"+"VerifyFileSignature() Fails")
                    logging.info("DINGUTL:"+"---END VerifyFileSignature()---")
                    logging.info("------------------------")
                    return False

                if DINGUTL.RegExSearchInStringOrFile("Signed",SigCheckfile):
                    logging.info("DINGUTL:"+"VerifyFileSignature() Successfully")
                    logging.info("DINGUTL:"+"---END VerifyFileSignature()---")
                    logging.info("------------------------")
                    return True
                else:
                    logging.info("DINGUTL:"+"VerifyFileSignature() Fails")
                    logging.info("DINGUTL:"+"---END VerifyFileSignature()---")
                    logging.info("------------------------")
                    return False
            else:
                logging.info("DINGUTL:"+"VerifyFileSignature() Tool sigcheck.exe is not found")
                logging.info("DINGUTL:"+"---END VerifyFileSignature()---")
                logging.info("------------------------")
                return False

        logging.info("DINGUTL:"+"VerifyFileSignature() Missing Parameter. File Parameter-not found")
        logging.info("DINGUTL:"+"---END VerifyFileSignature()---")
        logging.info("------------------------")
        return False
    except IOError as e:
        logging.error("DINGUTL:"+"VerifyFileSignature(): Exception Error occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END VerifyFileSignature()---")
        logging.info("------------------------")
        return str(e)

##================================================================================================================================
## @brief           RegExSearchInStringOrFile(pattern, file_or_string_to_search)
##
##                  RegExSearchInStringOrFile checks for a match anywhere in an ANSI STRING or in an ANSI FILE
##                  IF file_or_string_to_search is UNICODE, please call UniToAnsi() to convert this file from Unicode to ANSI
##
## @param           pattern (the regular expression to be matched. Google to learn how to create a pettern search)
##                  file_or_string_to_search (This is a location of file (or a string) which would be searched to match the pattern anywhere in File or String)
##                  i.e: file_or_string_to_search= r"C:\working\input\url.txt"   Note url.txt must be ANSI file.
##                       file_or_string_to_search = "Cats are smarter than dogs"
##                  
## @returns                 True    SUCCESS to find a pattern on a String or on a File
#                           False   FAILURE to find a pattern on a String or on a File / Invalid Input Parameters
##
## @exception               return str(e)   = Exception Error
##================================================================================================================================
def RegExSearchInStringOrFile(pattern, file_or_string_to_search):
    try:
        found=False
        logging.info("DINGUTL:"+"---START RegExSearchInStringOrFile()---")
        if os.path.exists(file_or_string_to_search)==True: # Check for file and directory
            try:
                lines=codecs.open(file_or_string_to_search, mode="r")
            except IOError as e:
                logging.error("DINGUTL:"+"RegExSearchInStringOrFile(): Fail to Open File for Reading **Error = %s" % str(e))
                return str(e)

            for line in lines:
                if re.search(pattern, line):
                    logging.info("DINGUTL:"+ "RegExSearchInStringOrFile() Search found = %s %s" %(pattern, line))
                    logging.info("DINGUTL:"+"---END RegExSearchInStringOrFile()---")
                    logging.info("------------------------")   
                    found=True
                    break
            lines.close()
            if found==True:
                return True 
        else:
            if re.search(pattern, file_or_string_to_search):
                logging.info("DINGUTL:"+ "RegExSearchInStringOrFile() Search found = %s%s" %(pattern, file_or_string_to_search))
                logging.info("DINGUTL:"+"---END RegExSearchInStringOrFile()---")
                logging.info("------------------------")   
                return True

        logging.info("DINGUTL:"+ "RegExSearchInStringOrFile() Fail To Search a Pattern on a String or on a File / Or Invalid Input Parameters")
        logging.info("DINGUTL:"+ "RegExSearchInStringOrFile() Not found = %s%s" %(pattern, file_or_string_to_search))
        logging.info("DINGUTL:"+"---END RegExSearchInStringOrFile()---")
        logging.info("------------------------")  
        return False

    except IOError as e:
        logging.error("DINGUTL:"+"RegExSearchInStringOrFile(): Exception Error occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END RegExSearchInStringOrFile()---")
        logging.info("------------------------")
        return str(e)

##================================================================================================================================
## @brief           RegExMatchInStringOrFile(pattern, file_or_string_to_search)
##
##                  RegExMatchInStringOrFile checks for a match only at the beginning of the ANSI STRING or of the ANSI FILE
##                  IF file_or_string_to_search is UNICODE, please call UniToAnsi() to convert this file from Unicode to ANSI
##
## @param           pattern (the regular expression to be matched)
##                  file_or_string_to_search (This is a location of file (or a string) which would be searched to match the pattern in File or in String)
##                  i.e: file_or_string_to_search= r"C:\working\input\url.txt"   Note url.txt must be ANSI file.
##                       file_or_string_to_search = "Cats are smarter than dogs"
##
## @returns                 True
#                           False 
## @exception               return str(e)   = Exception Error
##================================================================================================================================
def RegExMatchInStringOrFile(pattern, file_or_string_to_search):
    try:
        found=False
        logging.info("DINGUTL:"+"---START RegExMatchInStringOrFile()---")
        if os.path.exists(file_or_string_to_search)==True: # Check for file and directory
            try:
                lines=codecs.open(file_or_string_to_search, mode="r")
            except IOError as e:
                logging.error("DINGUTL:"+"RegExMatchInStringOrFile(): Fail to Open File for Reading **Error = %s" % str(e))
                return str(e)

            for line in lines:
                if re.match(pattern, line):
                    logging.info("DINGUTL:"+ "RegExMatchInStringOrFile() Match found = %s %s" %(pattern,line))
                    logging.info("DINGUTL:"+"---END RegExMatchInStringOrFile()---")
                    logging.info("------------------------")   
                    found=True
                    break
            lines.close()
            if found==True:
                return True 
        else:
            if re.match(pattern, file_or_string_to_search):
                logging.info("DINGUTL:"+ "RegExMatchInStringOrFile() Match found = %s%s" %(pattern, file_or_string_to_search))
                logging.info("DINGUTL:"+"---END RegExMatchInStringOrFile()---")
                logging.info("------------------------")  
                return True
        
        logging.info("DINGUTL:"+ "RegExMatchInStringOrFile() Fail To Search a Pattern on a String or on a File / Or Invalid Input Parameters")
        logging.info("DINGUTL:"+ "RegExMatchInStringOrFile() Match Not found = %s%s" %(pattern, file_or_string_to_search))
        logging.info("DINGUTL:"+"---END RegExMatchInStringOrFile()---")
        logging.info("------------------------")  
        return False

    except IOError as e:
        logging.error("DINGUTL:"+"RegExMatchInStringOrFile(): Exception Error occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END RegExMatchInStringOrFile()---")
        logging.info("------------------------")
        return str(e)


##================================================================================================================================
## @brief               RootCertUpdOnXP()
##                      Require: C:\working\input\rootsupd.exe
##                  
## @param            
##
## @returns             True            = Success
##                      False           = rootsupd.exe is not found or Not Win XP
##
## @exception           return str(e)   = Exception Error
##================================================================================================================================
def RootCertUpdOnXP():
    try:

        logging.info("DINGUTL:"+"---START RootCertUpdOnXP()---")
        if sys.getwindowsversion()<(6,):
            sPath=WORKING_INPUT_DIR + "\\"+ "rootsupd.exe"
            if os.path.isfile(sPath)==True:
                if subprocess.call([sPath,"/q"])==0:
                    logging.info("DINGUTL:"+"---END RootCertUpdOnXP()---")
                    return True
                else:
                    logging.info("DINGUTL:"+"Fail to install rootsupd.exe in Win XP")
                    logging.info("DINGUTL:"+"---END RootCertUpdOnXP()---")
                    logging.info("-----------------------")
                    return False
            else:
                logging.info("DINGUTL:"+"rootsupd.exe is not found. sPath = %s" %sPath)
                logging.info("DINGUTL:"+"---END RootCertUpdOnXP()---")
                logging.info("-----------------------")
        else:
            logging.info("DINGUTL:"+"Not Win XP*** Exit")
            logging.info("DINGUTL:"+"---END RootCertUpdOnXP()---")
            logging.info("-----------------------")
            return False
    except Exception as e:
        logging.error("DINGUTL:"+"RootCertUpdOnXP(): Exception Error occurs **Error = %s" % str(e))
        logging.info("DINGUTL:"+"---END RootCertUpdOnXP()---")
        logging.info("-----------------------")
        return str(e)

##================================================================================================================================
## @brief                   Converting Unicode 'utf-16' file to Ansi file.
##               
##
## @param                   Infile  (Location of unicode file to convert)      C:\\working\\output\\url.txt
##                          Outfile (Location of ansi file to write)           C:\\working\\output\\url_temp.txt
##
## @returns                 return True  (ansi file url_temp.txt is created)
##
## @exception               return str(e) = Exception Error
##================================================================================================================================
def UniToAnsi(Infile, Outfile):
    try:
        logging.info("DINGUTL:"+"---START UniToAnsi()---")
        try:
            ReadFile= codecs.open(Infile, mode="r", encoding='utf-16')
        except IOError as e:
            logging.error("DINGUTL:"+"UniToAnsi(): Fail to Open File for reading **Error = %s" % str(e))
            return str(e)
        try:
            WriteFile= open(Outfile, mode="w")
        except IOError as e:
            logging.error("DINGUTL:"+"UniToAnsi(): Fail to Open File for Writing **Error = %s" % str(e))
            return str(e)

        lines=ReadFile.readlines()
        for line in lines:
            WriteFile.write(line)

        ReadFile.close()
        WriteFile.close()

        logging.info("DINGUTL:"+"---END UniToAnsi()---")
        logging.info("-----------------------")
        return True
    except IOError as e:
        logging.error("DINGUTL:"+"UniToAnsi(): exception IOError Occurs during Read and Write file **Error = %s" % str(e))
        logging.info("DINGUTL:"+"---END UniToAnsi()---")
        logging.info("-----------------------")
        return str(e)


        
##================================================================================================================================
## @brief           GetCommonAppDataPath(): give the location of Program Data / AppData regardless of OS context!
##                  
##                 
##                  
## @param         
##
## @returns          full path of common app data
##                   1 = Fail to get common app data path
##
## @exception        return str(e) = Exception Error
##=================================================================================================================================
def GetCommonAppDataPath():
    try:
        logging.info("DINGUTL:"+"---START GetCommonAppDataPath()---")
        CSIDL_COMMON_APPDATA = 35
        _SHGetFolderPath = windll.shell32.SHGetFolderPathW
        _SHGetFolderPath.argtypes = [wintypes.HWND,
                    ctypes.c_int,
                    wintypes.HANDLE,
                    wintypes.DWORD, wintypes.LPCWSTR]

        path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
        result = _SHGetFolderPath(0, CSIDL_COMMON_APPDATA, 0, 0, path_buf)
        if result==0:
            logging.info("DINGUTL:"+"Return Value= %s" % path_buf.value)
            logging.info("DINGUTL:"+"---END GetCommonAppDataPath()---")
            logging.info("------------------------")
            return path_buf.value
        else:
            logging.info("DINGUTL:"+"GetCommonAppDataPath(): Fail to get common App folder. Return Value= %s" % result)
            logging.info("DINGUTL:"+"---END GetCommonAppDataPath()---")
            logging.info("------------------------")
            return result
    except Exception as e:
        logging.error("DINGUTL:"+"GetCommonAppDataPath(): Exception Error Occurs. Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END GetCommonAppDataPath()---")
        logging.info("------------------------")
        return str(e)

"""
================================================================================================================================
 @brief           DefaultToDesktop(): Boot to Desktop on Win 8
                  to bypass metro UI.
                  This function wil create ToggleDesktop key name of 
                  HKLM\Software\Microsoft\Windows\CurrentVersion\Run
 @param         

 @returns         0 / 1 (SUCCESS / FAILURE)
                   
 @exception       return str(e) = Exception Error
=================================================================================================================================
"""
def DefaultToDesktop():
    try:
        
        #Win 8 / 8.1
        if ((sys.getwindowsversion()[2]==9200 or sys.getwindowsversion()[2]==9600) and sys.getwindowsversion()[0]==6):
            logging.info("DINGUTL:"+"---START DefaultToDesktop()---")

            ## Files need to be created
            if True != GenScfToggleDesktopFile():
                logging.info("DINGUTL:"+"GenScfToggleDesktopFile(): Fail to Generate file ToggleDesktop.scf" )
                logging.info("DINGUTL:"+"---END DefaultToDesktop()---")
                logging.info("------------------------")
                return False;

            # generate file ToggleDesktopKey.reg
            ToggleDesktopKey=WORKING_INPUT_DIR+"\\"+"ToggleDesktopKey.reg"
            if True != GenKeyNameForRunKey(ToggleDesktopKey):
                logging.info("DINGUTL:"+"GenKeyNameForRunKey(): Fail to Generate file ToggleDesktopKey.reg" )
                logging.info("DINGUTL:"+"---END DefaultToDesktop()---")
                logging.info("------------------------")
                return False;

            # Adding key name
            Win_Info= WinOSInfo()
            if Win_Info[2]=='32Bit': 
                RegPlatform = "/reg:32"
            else:
                RegPlatform = "/reg:64"

            retcode=subprocess.call([os.environ['windir']+ r"\system32\reg.exe","import",ToggleDesktopKey,RegPlatform],shell=True)
            logging.info("DINGUTL:"+"DefaultToDesktop(): Return Value= %s" % retcode)
            logging.info("DINGUTL:"+"---END DefaultToDesktop()---")
            logging.info("------------------------")
            return retcode
         
    except EnvironmentError as e:    
        logging.error("DINGUTL:"+"DefaultToDesktop(): Exception EnvironmentError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END DefaultToDesktop()---")
        logging.info("------------------------")                                           
        return str(e) 

##================================================================================================================================
## @brief               GenerateSCFToggleDesktopFile: Not a Method is being used by DefaultToDesktop() function
##                      generate OutFile1
##                  
## @param          
##
## @returns             True after generating OutFile1
##
## @exception           return str(e) = Exception Error
##=================================================================================================================================
def GenScfToggleDesktopFile():
    try:
        logging.info("DINGUTL:"+"---START GenScfToggleDesktopFile()---")
        #generate file ToggleDesktop.scf
        OutFile1= WORKING_INPUT_DIR+ "\\"+ r"ToggleDesktop.scf"    
        if not os.path.exists(OutFile1):  
            try:   
                WriteFile   = open(OutFile1, mode="w")
            except IOError as e:
                logging.info("DINGUTL:"+"GenScfToggleDesktopFile(): Exception errors occurs during open File for writing ****Return Value= %s" % str(e))
                logging.info("DINGUTL:"+"---END GenScfToggleDesktopFile()---")
                logging.info("------------------------") 
                return str(e)

            WriteFile.write("[Shell]" +"\n")
            WriteFile.write("Command=2" +"\n")
            WriteFile.write("IconFile=Explorer.exe,3" +"\n")
            WriteFile.write("[Taskbar]" +"\n")
            WriteFile.write("Command=ToggleDesktop"+"\n")
            WriteFile.close()
        logging.info("DINGUTL:"+"Generate File ToggleDesktop.scf Successfully")
        logging.info("DINGUTL:"+"---END GenScfToggleDesktopFile()---")
        logging.info("------------------------")
        return True
    except IOError as e:
        logging.error("DINGUTL:"+"GenScfToggleDesktopFile(): Exception IOError occurs during writing data to File ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END GenScfToggleDesktopFile()---")
        logging.info("------------------------") 
        return str(e)

##================================================================================================================================
## @brief          GenKeyNameForRunKey(): Not a Method is being used by DefaultToDesktop() function
##                  generate OutFile2
##                  
## @param           OutFile2
##
## @returns         True after generating OutFile2 
##
## @exception       return str(e) = Exception Error
## 
##=================================================================================================================================
def GenKeyNameForRunKey(OutFile2):
    try:   
        logging.info("DINGUTL:"+"---START GenKeyNameForRunKey()---")  
        try:    
            WriteFile = codecs.open(OutFile2, mode="w", encoding='utf-16')
        except IOError as e:
            logging.info("DINGUTL:"+"GenKeyNameForRunKey(): Exception errors occurs during open File for writing ****Return Value= %s" % str(e))
            logging.info("DINGUTL:"+"---END GenKeyNameForRunKey()---")
            logging.info("------------------------")
            return str(e) 

        WriteFile.write("Windows Registry Editor Version 5.00" )
        WriteFile.write(u"\r\n")
        WriteFile.write(u"\r\n")
        WriteFile.write("[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]")
        WriteFile.write(u"\r\n")
        WriteFile.write('"ToggleDesktop"=')
        WriteFile.write('"'+r"C:\\working\\input\\ToggleDesktop.scf"+'"')
        WriteFile.write(u"\r\n")
        WriteFile.write(u"\r\n")
        WriteFile.close()

        logging.info("DINGUTL:"+"GenKeyNameForRunKey(): Generate File ToggleDesktopKey.reg Successfully")
        logging.info("DINGUTL:"+"---END GenKeyNameForRunKey()---")
        logging.info("------------------------") 
        return True
    except IOError as e:
        logging.error("DINGUTL:"+"GenKeyNameForRunKey(): Exception IOError occurs during writing data to a file ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END GenKeyNameForRunKey()---")
        logging.info("------------------------") 
        return str(e)

##=====================================================================================================
## @brief                   GetRootKey    
##
## @param                   MainKey
##
## @returns                 one of the key in the below list:
##                          HKEY_USERS          = HKU
##                          HKEY_CURRENT_CONFIG = HKCC
##                          HKEY_CLASSES_ROOT   = HKCR 
##                          HKEY_LOCAL_MACHINE  = HKLM
##                          HKEY_CURRENT_USER   = HKCU 
##
##                          null if not found
## @exception               return str(e)      = exception error
##======================================================================================================
def GetRootKey(MainKey):
    try:
        KeyList ={
                    'HKLM': _winreg.HKEY_LOCAL_MACHINE, 
                    'HKCU': _winreg.HKEY_CURRENT_USER, 
                    'HKU' : _winreg.HKEY_USERS, 
                    'HKCR': _winreg.HKEY_CLASSES_ROOT, 
                    'HKCC': _winreg.HKEY_CURRENT_CONFIG
                    }

        logging.info("DINGUTL:"+"---START GetRootKey()---")
        if MainKey in KeyList:
            logging.info("DINGUTL:"+"RootKey found. = %s" %KeyList[MainKey])
            logging.info("DINGUTL:"+"---END GetRootKey()---")
            logging.info("------------------------")
            return KeyList[MainKey]
        else:
            logging.info("DINGUTL:"+"GetRootKey(): RootKey Not found = %s" %KeyList[MainKey])
            logging.info("------------------------")
            return KeyList[MainKey]
    except WindowsError as e: 
        logging.error("DINGUTL:"+"GetRootKey(): Exception WindowsError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END GetRootKey()---")
        logging.info("------------------------")                                               
        return str(e) 

##=====================================================================================================
## @brief               OpenRegKey           
##
## @param               RootKey
##                      SubKey
##
##
## @returns             aKey
##
## @exception           return str(e)      = exception error
##======================================================================================================
def OpenRegKey(RootKey, SubKey):
    try:

        logging.info("DINGUTL:"+"---START GetRootKey()---")
        Win_Info= WinOSInfo()           
        if Win_Info[2]=='32Bit':
            REGKEY_PLATFORM_FLAG=0x0200
        else:
            REGKEY_PLATFORM_FLAG=0x0100
        aReg = _winreg.ConnectRegistry(None, RootKey)   
        aKey = _winreg.OpenKey(aReg, SubKey,0, _winreg.KEY_SET_VALUE | REGKEY_PLATFORM_FLAG) 
        logging.info("DINGUTL:"+"OpenRegKey(): Successfully. = %s" %SubKey)
        logging.info("DINGUTL:"+"---END OpenRegKey()---")
        logging.info("------------------------")  
        return aKey
    except WindowsError as e: 
        logging.error("DINGUTL:"+"OpenRegKey(): Exception WindowsError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END OpenRegKey()---")
        logging.info("------------------------")                                               
        return str(e) 

##================================================================================================================================
## @brief               This function will return Name, Data, type of a registry key used as input parameters (MainKey, its SubKey and KeyName)
##                      Validate input data (MainKey, its SubKey, KeyName) before running.
## 
##           
## @param               MainKey is one of the below keys. ----- i.e MainKey = "HKLM"
##                      HKEY_USERS          = HKU
##                      HKEY_CURRENT_CONFIG = HKCC
##                      HKEY_CLASSES_ROOT   = HKCR 
##                      HKEY_LOCAL_MACHINE  = HKLM
##                      HKEY_CURRENT_USER   = HKCU 
##
##                   SubKey  = r"SOFTWARE\Wow6432Node\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"
##                   KeyName = r"APPDATA"
##
## @returns          KeyArr (array) for use which stores KeyName, KeyData, KeyType 
##                            KeyArr[0]=KeyName
##                            KeyArr[1]=KeyData 
##                            KeyArr[2]=KeyType
##                   KeyArr[]    = parameter validation error
##
## @exception        return str(e)      = exception error
##=================================================================================================================================
def GetRegistryKeyData(MainKey, SubKey, KeyName):
    try:
        KeyArr=[]

        logging.info("DINGUTL:"+"---START GetRegistryKeyData()---")
        RootKey = GetRootKey(MainKey)
        if False!= RootKey and len(SubKey) != 0 and (len(KeyName) != 0):
            aReg = _winreg.ConnectRegistry(None, RootKey)
            aKey = _winreg.OpenKey(aReg, SubKey)
            valueData,valueType = _winreg.QueryValueEx(aKey, KeyName)
            KeyArr.append(KeyName)
            KeyArr.append(valueData)
            KeyArr.append(valueType)
            _winreg.CloseKey(aKey)
            logging.info("DINGUTL:"+"GetRegistryKeyData() Successfully. KeyName = %s %s %s" %(KeyArr[0], KeyArr[1],KeyArr[2]))
            logging.info("DINGUTL:"+"---END GetRegistryKeyData()---")
            logging.info("------------------------") 
            return KeyArr
        else:
            logging.info("DINGUTL:"+"GetRegistryKeyData(): MainKey, SubKey, KeyName parameters are invalid. = %s %s %s" %(MainKey, SubKey, KeyName))
            logging.info("DINGUTL:"+"---END GetRegistryKeyData()---")
            logging.info("------------------------") 
            return KeyArr
    except WindowsError as e: 
        logging.error("DINGUTL:"+"GetRegistryKeyData(): Exception WindowsError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END GetRegistryKeyData()---")
        logging.info("------------------------")                                               
        return str(e) 

##================================================================================================================================
## @brief               CreateRegistryKey
##              
## @param               MainKey is one of the below keys. ----- i.e MainKey = "HKLM"
##                      HKEY_USERS          = HKU
##                      HKEY_CURRENT_CONFIG = HKCC
##                      HKEY_CLASSES_ROOT   = HKCR 
##                      HKEY_LOCAL_MACHINE  = HKLM
##                      HKEY_CURRENT_USER   = HKCU 
##
##                   SubKey  = r"Software\Microsoft\Windows\CurrentVersion\Run"
##                   KeyName = r"ToggleDesktop"
##
## @returns             True            = Success
##                      False           = parameter validation error
## @exception           return str(e)   = exception error
##=================================================================================================================================
def CreateRegistryKey(MainKey, SubKey, KeyName):
    try:

        logging.info("DINGUTL:"+"---START CreateRegistryKey()---")
        RootKey = GetRootKey(MainKey)
        if False != RootKey and len(SubKey) != 0 and len(KeyName) != 0:         # Validating Input key
            aKey=OpenRegKey(RootKey, SubKey)
            if aKey:
                _winreg.CreateKey(aKey, KeyName)
                _winreg.CloseKey(aKey)
                logging.info("DINGUTL:"+"CreateRegistryKey() Successfully. KeyName= %s" %KeyName)
                logging.info("DINGUTL:"+"---END CreateRegistryKey()---")
                logging.info("------------------------")  
                return True
        else:
            logging.info("DINGUTL:"+"CreateRegistryKey(): MainKey, SubKey, KeyName parameters are invalid = %s %s %s" %(MainKey, SubKey, KeyName))
            logging.info("DINGUTL:"+"---END CreateRegistryKey()---")
            logging.info("------------------------")  
            return False 

    except WindowsError as e:  
        logging.error("DINGUTL:"+"CreateRegistryKey(): Exception WindowsError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END CreateRegistryKey()---")
        logging.info("------------------------")                                                    
        return str(e)     

##================================================================================================================================
## @brief           This function returns True when KeyData is modified successfully and vice verca it returns False
##              
## @param           MainKey is one of the below keys. ----- i.e MainKey = "HKLM"
##                      HKEY_USERS          = HKU
##                      HKEY_CURRENT_CONFIG = HKCC
##                      HKEY_CLASSES_ROOT   = HKCR 
##                      HKEY_LOCAL_MACHINE  = HKLM
##                      HKEY_CURRENT_USER   = HKCU 
##
##                   SubKey  = r"SYSTEM\CurrentControlSet\services\MemoryEnquiry"
##                   KeyName = r"Start"
##                   KeyType = _winreg.REG_DWORD (_winreg.REG_EXPAND_SZ/ _winreg.REG_BINARY....)                               
##                   KeyData = 4              MemoryEnquiry has Start value is 2. 
##                   
##
## @returns          True           = Success
##                   False          = parameter validation error
##
##
## @exception        return str(e)  = exception error
##=================================================================================================================================
def SetRegistryKeyData(MainKey, SubKey, KeyName, KeyType, KeyData):
    try:
        
        RootKey = GetRootKey(MainKey)
        if False!= RootKey and len(SubKey) != 0 and len(KeyName) != 0:         # Validating Input key
            logging.info("DINGUTL:"+"---START SetRegistryKeyData()---")
            aKey=OpenRegKey(RootKey, SubKey)
            if aKey:
                _winreg.SetValueEx(aKey, KeyName, 0, KeyType, KeyData)               #SubKey,KeyName, 0, _winreg.REG_DWORD, str(4)
                _winreg.CloseKey(aKey)
                logging.info("DINGUTL:"+"SetRegistryKeyData() Successfully. KeyName is Modified = %s" %KeyName)
                logging.info("DINGUTL:"+"---END SetRegistryKeyData()---")
                logging.info("------------------------") 
                return True
        else:
            logging.info("DINGUTL:"+"SetRegistryKeyData(): MainKey, SubKey, KeyName, KeyType, KeyData parameters are invalid %s %s %s %s %s = "%(MainKey,SubKey,KeyName,KeyType,KeyData))
            logging.info("DINGUTL:"+"---END SetRegistryKeyData()---")
            logging.info("------------------------") 
            return False

    except WindowsError as e:  
        logging.error("DINGUTL:"+"SetRegistryKeyData(): Exception WindowsError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END SetRegistryKeyData()---")
        logging.info("------------------------")                                                    
        return str(e)     
          

##================================================================================================================================
## @brief               This function returns True when KeyNameDel is deleted successfully and vice verca it returns False
##              
## @param               MainKey is one of the below keys. ----- i.e MainKey = "HKLM"
##                      HKEY_USERS          = HKU
##                      HKEY_CURRENT_CONFIG = HKCC
##                      HKEY_CLASSES_ROOT   = HKCR 
##                      HKEY_LOCAL_MACHINE  = HKLM
##                      HKEY_CURRENT_USER   = HKCU 
##
##                   KeyNamePath    = r"SOFTWARE\Wow6432Node\Norton\{11111111-1111-1111-1111-111111111111}\DING"
##                   KeyNameDel     = r"PatchTracker"
##                                               
##                   
##                   
##
## @returns          True               = success
##                   False              = parameter validation error
##
## @exception        return str(e)      = Exception = win32 error
##=================================================================================================================================
def DeleteRegistryKey(MainKey, KeyNamePath, KeyNameDel):
    try:
        RootKey = GetRootKey(MainKey)
        if False!=RootKey and len(KeyNamePath) != 0 and len(KeyNameDel) != 0:         # Validating Input key
            logging.info("DINGUTL:"+"---START DeleteRegistryKey()---")
            aKey=OpenRegKey(RootKey, KeyNamePath)
            if aKey:
                _winreg.DeleteKey(aKey, KeyNameDel)
                _winreg.CloseKey(aKey)
                logging.info("DINGUTL:"+"DeleteRegistryKey() Successfully. Key is Deleted  = %s" %KeyNameDel)
                logging.info("DINGUTL:"+"---END DeleteRegistryKey()---")
                logging.info("------------------------") 
                return True     
        else:
            logging.info("DINGUTL:"+"DeleteRegistryKey(): MainKey, KeyNamePath, KeyNameDel parameters are Invalid.%s %s %s =" %(sMainKey, sKeyNamePath, KeyNameDel))
            logging.info("DINGUTL:"+"---END SetRegistryKeyData()---")
            logging.info("------------------------") 
            return False
 
    except WindowsError as e:  
        logging.error("DINGUTL:"+"DeleteRegistryKey(): Exception WindowsError occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END DeleteRegistryKey()---")
        logging.info("------------------------")                                                    
        return str(e)

##=====================================================================================================
## @brief       WinOSInfo() generates OS information and returns a list                       
##
## @param       NONE  
##
## @returns     A List (Ex.,  WinInfo = ['Win7','SP1','64Bit'] , in success case)
##
## @exception   A string (A generic exception)
##======================================================================================================

def WinOSInfo():

    try :

        global WinInfo
        WinWeight=0
        SPWeight=0
        Win=[]
        sp=[]
        WinInfo=[0,0,0]

        if os.path.exists('C:\\WinOSInfo.txt')==False:
            GetOSInfo()
         
        cmd1='Type "C:\WinOSInfo.txt" | find "Microsoft"'
        cmd2='Type "C:\WinOSInfo.txt" | find "Service Pack"'
        cmd3='Type "C:\WinOSInfo.txt" | find "-based PC"'

        Win.append(subprocess.check_output(cmd1,shell=True)) 
        Win.append(subprocess.call(cmd2,shell=True))
        Win.append(subprocess.check_output(cmd3,shell=True))

        if 'XP' in Win[0]:
            WinInfo[0]='WinXP'
            WinWeight=1
        if 'Vista' in Win[0]:
            WinInfo[0]='WinVista'
            WinWeight=2
        if 'Windows 7' in Win[0]:
            WinInfo[0]='Win7'
            WinWeight=3
        if 'Windows 8' in Win[0]:
            WinInfo[0]='Win8'
            WinWeight=4
        if 'Windows 8.1' in Win[0]:
            WinInfo[0]='Win8.1'
            WinWeight=5
    
        if not Win[1]:
            sp.append(subprocess.check_output(cmd2,shell=True))
            if 'Service Pack 1' in sp[0]:
                WinInfo[1]='SP1'
                SPWeight=2
            if 'Service Pack 2' in sp[0]:
                WinInfo[1]='SP2'
                SPWeight=3
            if 'Service Pack 3' in sp[0]:
                WinInfo[1]='SP3'
                SPWeight=4
        else:
            WinInfo[1]='SP0'
            SPWeight=1

        if "x64" in Win[2] :
            WinInfo[2]='64Bit'
        else:
            WinInfo[2]='32Bit'

        return WinInfo

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief       GetOSInfo() generates the System Information, this is not part of DING Class!
##
## @param   
##
## @returns 
##
## @exception
##======================================================================================================

def GetOSInfo(): 
    cmd='systeminfo >C:\WinOSInfo.txt'
    try:
        res=subprocess.check_output(cmd,shell=True)
        #log - res
        return True
    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief        Below are a deck Windows OS related functions                       
##
## @param           None   
##
## @returns         True or False
##
## @exception       A string (catches all exceptions)
##======================================================================================================

def Is32Bit():

    try:        
        WinLis=WinOSInfo()
        if WinLis[2]=='32Bit':
            return True
        else:
            return False

    except Exception as e:
        return str(e)

def Is64Bit():

    try:        
        WinLis=WinOSInfo()
        if WinLis[2]=='64Bit':
            return True
        else:
            return False


    except Exception as e:
        return str(e)

def IsWinXP():


    try:
        Win=WinOSInfo()
        if 'WinXP' in Win[0]:
            return True
        else:
            return False

    except Exception as e:
        return str(e)

def IsWinVista():

    try:
        Win=WinOSInfo()
        if 'WinVista' in Win[0]:
            return True
        else:
            return False
        
    except Exception as e:
        return str(e)
    

def IsWin7():

    try:
        Win=WinOSInfo()
        if 'Win7' in Win[0]:
            return True
        else:
            return False
    except Exception as e:
        return str(e)
    

def IsWin8():

    try:
        Win=WinOSInfo()
        if 'Win8' in Win[0]:
            return True
        else:
            return False
    except Exception as e:
        return str(e)

def IsWin8_1():

    try:
        Win=WinOSInfo()
        if 'Win8.1' in Win[0]:
            return True
        else:
            return False
    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief       Kills the User Session of Harness                   
##
## @param       NONE
##
## @returns     True (in success case)
##              A string (in failure case, i.e, output of subprocess.check_output() )
##
## @exception
##======================================================================================================

def KillNTPUser():

    try :

        WinInfo=[]
        WinInfo=WinOSInfo()
        Key=""
        Silo="Harness"
        if (Silo=="Harness") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Harness") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        #print "The Key to check is " +Key
        KeyInfo=GetRegistryKeyData(MainKey="HKLM",SubKey=Key,KeyName=r"SERVICEFILENAME")
        #print KeyInfo

        cmd='TASKKILL /FI "IMAGENAME eq '+KeyInfo[1]+'" /FI "USERNAME ne SYSTEM" /F'
        Msg=[]
        Msg=subprocess.check_output(cmd,shell=True)
        if "SUCCESS" in Msg:
            return True
        else:
            return Msg

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           Kills the System Session of Harness                        
##
## @param           NONE
##
## @returns         True (in success case)
##                  A string (in failure case, i.e, output of subprocess.check_output() )         
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def KillNTPSystem():

    try :

        WinInfo=[]
        WinInfo=WinOSInfo()
        Key=""
        Silo="Harness"
        if (Silo=="Harness") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Harness") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        #print "The Key to check is " +Key
        KeyInfo=GetRegistryKeyData(MainKey="HKLM",SubKey=Key,KeyName=r"SERVICEFILENAME")
        #print KeyInfo

        cmd='TASKKILL /FI "IMAGENAME eq '+KeyInfo[1]+'" /FI "USERNAME eq SYSTEM" /F'
        Msg=[]
        Msg=subprocess.check_output(cmd,shell=True)
        if "SUCCESS" in Msg:
            return True
        else:
            return Msg

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           Kills the User Session of Product               
##
## @param           NONE
##
## @returns         True (in success case)
##                  A string (in failure case, i.e, output of subprocess.check_output() )  
##
## @exception		A string (catches all exceptions)
##======================================================================================================


def KillProductUser():

    try :
        WinInfo=[]
        WinInfo=WinOSInfo()
        Key=""
        Silo="Product"
        if (Silo=="Harness") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Harness") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        #print "The Key to check is " +Key
        KeyInfo=GetRegistryKeyData(MainKey="HKLM",SubKey=Key,KeyName=r"SERVICEFILENAME")
        #print KeyInfo

        cmd='TASKKILL /FI "IMAGENAME eq '  +  KeyInfo[1]  +  '" /FI "USERNAME ne SYSTEM" /F'
        Msg=[]
        Msg=subprocess.check_output(cmd,shell=True)
        if "SUCCESS" in Msg:
            return True
        else:
            return Msg

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           Kills the System Session of Product                     
##
## @param           NONE
##
## @returns         True (in success case)
##                  A string (in failure case, i.e, output of subprocess.check_output() )   
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def KillProductSystem():

    try :
        WinInfo=[]
        WinInfo=WinOSInfo()
        Key=""
        Silo="Product"
        if (Silo=="Harness") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Harness") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{11111111-1111-1111-1111-111111111111}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='64Bit'):
            Key=r"SOFTWARE\Wow6432Node\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        if (Silo=="Product") and (WinInfo[2]=='32Bit'):
            Key=r"SOFTWARE\Norton\{0C55C096-0F1D-4F28-AAA2-85EF591126E7}\Common Client\PathExpansionMap"

        #print "The Key to check is " +Key
        KeyInfo=GetRegistryKeyData(MainKey="HKLM",SubKey=Key,KeyName=r"SERVICEFILENAME")
        #print KeyInfo

        cmd='TASKKILL /FI "IMAGENAME eq '+KeyInfo[1]+'" /FI "USERNAME eq SYSTEM" /F'
        Msg=[]
        Msg=subprocess.check_output(cmd,shell=True)
        if "SUCCESS" in Msg:
            return True
        else:
            return Msg

    except Exception as e:
        return str(e)

##=============================================================================================================================
## @brief           Finds the Latest Norton Install Log                 
##
## @param           A path to store the Latest log (Ex., C:\working, by default it is WORKING_OUTPUT_DIR)
##
## @returns         The path to latest log (Ex., C:\\working\\Output\\NortonInstall-2014-08-11-12h56m28s.log in success case)
##                  A string (in failure case)
##
## @exception		A string (catches all exceptions)
##==============================================================================================================================

def LatInstLog(dest=WORKING_OUTPUT_DIR):

    try :
        WinInfo=[]
        WinInfo=WinOSInfo()
        Bit=WinInfo[2]

        Path1=GetCommonAppDataPath()  
        LogPath=os.path.join(Path1,r'NortonInstaller',r'Logs')    
        root=str(LogPath)+'\\*'
        date_file_list = []
    
        for folder in glob.glob(root):
            for file in glob.glob(folder + '/NortonInstall*.log'):
                date_file_list.append(file)

        if date_file_list==[]:
            MsgW="Can't find NortonInstall.Log because No folder has logs or All the Folders have been archived"
            return MsgW

        else :
            date_file_list.sort()
            for file in date_file_list:
                source=file        
            if dest[len(dest)-1] != '\\':
                dest=dest+'\\'
            shutil.copy(str(source),dest)
            sourcefile=os.path.basename(source)
            #MsgS="Latest Norton Install Log location = "+dest+sourcefile
            return dest+sourcefile

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           checks if a folder and its subfolders are empty                 
##
## @param           A path (Ex., r"C:\Python27\a_Gp\New folder")
##
## @returns         True (success case) and False (failure case)
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def IsEmpty(dir):

    try :
        files=[]
        folders=[]

        if not dir:
            MsgW="No Path specified"
            return MsgW        

        for (dirpath,dirnames,filenames) in os.walk(dir):
            files.extend(filenames)
            folders.extend(dirnames)
        if not files:
            return True
        else:
            return False

    except Exception as e:
        return str(e)

##======================================================================================================================================
## @brief           SymProtectStatus() returns the status of Norton Tamper Protection                  
##
## @param           NONE
##
## @returns         Windows Error Code in http://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description
##                  (Ex., 0 = Success Case)
##
## @exception		A string (catches all exceptions)
##=======================================================================================================================================

def SymProtectStatus():

    try:
	
		res = "Sorry! This function's implementation is Private to Symantec"
        return res

    except Exception as e:
        return str(e)

##======================================================================================================================================
## @brief           SymProtectON() turns ON the Norton Tamper Protection                
##
## @param           NONE
##
## @returns         Windows Error Code in http://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description
##                  (Ex., 0 = Success Case)
##
## @exception		A string (catches all exceptions)
##=======================================================================================================================================

def SymProtectON():

    try:
	
		res = "Sorry! This function's implementation is Private to Symantec"
        return res
        
    except Exception as e:
        return str(e)

##======================================================================================================================================
## @brief           SymProtectOFF() turns OFF the Norton Tamper Protection               
##
## @param           NONE
##
## @returns         Windows Error Code in http://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description
##                  (Ex., 0 = Success Case)
##
## @exception		A string (catches all exceptions)
##=======================================================================================================================================

def SymProtectOFF():

    try:
	
		res = "Sorry! This function's implementation is Private to Symantec"
        return res

    except Exception as e:
        return str(e)

##===================================================================================================================
## @brief           GetDatafromPathExpansionMap() is used get KeyValue from PathExpansion Map when KeyName
##                  is specified                      
##
## @param           KeyName  [Ex., DINGUTL.GetDatafromPathExpansionMap('INSTALLCACHEDIR') ]
##
## @returns         A string which is KeyValue  [Ex., C:\Program Files (x86)\Norton Test Product\Engine\10.0.1.150 ]
##
## @exception		A string (catches all exceptions)
##====================================================================================================================
 
def GetDatafromPathExpansionMap(KeyName):
    try :
        silo = GetSingleProdSiloKey()
        if Is32Bit():
            path = "SOFTWARE\\Norton\\" + silo + "\\Common Client\\PathExpansionMap"
        else:
            path = "SOFTWARE\\Wow6432Node\\Norton\\" + silo + "\\Common Client\\PathExpansionMap"
        KeyArr = GetRegistryKeyData("HKLM", path,KeyName)
        KeyVal=KeyArr[1]
        return KeyVal
    except Exception as e:
        return str(e)
    
##=====================================================================================================
## @brief           GetMD5FileHash() is used to get the MD5 File Hash Value of a given File                    
##
## @param           Full path to the .loc file of any file,
##                  Ex., Path=r'C:\\working\\Output\\A\\InstallBranding\\09\\01\\InsBrand.loc'        
##
## @returns         A string which is a Hash Value of the file
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def GetMD5FileHash(fPath):
    try:
        Hash=hashlib.md5(open(fPath).read()).hexdigest()
        return Hash
    except Exception as e:
        return str(e)

##=====================================================================================================================================
## @brief           GetInstallBrandMD5FileHash() is used to get the MD5 File Hash Value of 
##                  InsBrand.loc file present inside Install Cache                      
##
## @param           NONE
##
## @returns         A List which has the path of LOC file and Hash Value of the InsBrand.loc file present inside Install Cache
##
## @exception		A string (catches all exceptions)
##======================================================================================================================================

def GetInstallBrandMD5FileHash():
    try:
        HashList=[]        
        InsCache=GetDatafromPathExpansionMap(r'INSTALLCACHEDIR')
        fPath=os.path.join(InsCache,'09','01','InsBrand.loc')
        Hash=hashlib.md5(open(fPath).read()).hexdigest()
        HashList.append(fPath)
        HashList.append(Hash)

        return HashList
    except Exception as e:
        return str(e)

##=========================================================================================================================================
## @brief           GetNTPProductBrandMD5FileHash() is used to get the MD5 File Hash Value of 
##                  notepad.loc file present inside Branding folder of Norton Test Product                    
##
## @param           NONE
##
## @returns         A List which has the path of LOC file and Hash Value of the notepad.loc file present inside Branding folder of
##                  Norton Test Product
##
## @exception		A string (catches all exceptions)
##==========================================================================================================================================

def GetNTPProductBrandMD5FileHash():
    try:  
        
        HashList=[]

        path1=GetDatafromPathExpansionMap(r'BRANDINGDIR')                     
        if Is32Bit():       
            path2=GetRegistryKeyData("HKLM",r"SOFTWARE\Norton\{11111111-1111-1111-1111-111111111111}",r"PRODUCTVERSION")           
        else:
            path2=GetRegistryKeyData("HKLM",r"SOFTWARE\Wow6432Node\Norton\{11111111-1111-1111-1111-111111111111}",r"PRODUCTVERSION")
        path3=os.path.join(path1,path2[1])
        path4=os.path.join(path3,'09','01','notepad.loc')

        if os.path.exists(path4):
            HashList.append(path4)
            Hash=hashlib.md5(open(path4).read()).hexdigest()
            HashList.append(Hash)       
        
        return HashList
    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           This function returns the entire path of "ProgramFiles" Folder                      
##
## @param           NONE
##
## @returns         A path of "ProgramFiles" Folder depending upon 32 bit or 64 bit   
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def GetCommonProgramFilesPath():
    try:
        CSIDL_PROGRAMFILES = 38
        _SHGetFolderPath = windll.shell32.SHGetFolderPathW
        _SHGetFolderPath.argtypes = [wintypes.HWND,
                    ctypes.c_int,
                    wintypes.HANDLE,
                    wintypes.DWORD, wintypes.LPCWSTR]

        path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
        result = _SHGetFolderPath(0, CSIDL_PROGRAMFILES, 0, 0, path_buf)

        if result==0:
            return path_buf.value
        else:
            return result

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief                        
##
## @param           NONE
##
## @returns         The path where Windows OS is installed. Ex., C:\ or D:\ etc
##                  The aim of this function is to avoid Hard Coding of paths.
##                  We can very well use os.path.join(driver_variable,'System32') etc.     
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def GetDefaultWindowsOSDriver():
    try:
        CSIDL_WINDRIVER = 36
        _SHGetFolderPath = windll.shell32.SHGetFolderPathW
        _SHGetFolderPath.argtypes = [wintypes.HWND,
                    ctypes.c_int,
                    wintypes.HANDLE,
                    wintypes.DWORD, wintypes.LPCWSTR]

        path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
        result = _SHGetFolderPath(0, CSIDL_WINDRIVER, 0, 0, path_buf)

        if result==0:
            temp=path_buf.value
            DFLT_DRIVER=temp.replace("Windows","")
            return DFLT_DRIVER
        else:
            return result

    except Exception as e:
        return str(e)
##=====================================================================================================
## @brief           Copies the entire "%APPDATA%\NortonInstaller\Logs\"  to  "%ATRIUMOUTPUT%\Logs\"  Folder             
##
## @param           NONE
##
## @returns         True (success case when logs are copied)
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def CopyNortonLogs():
    try:
        path1=GetCommonAppDataPath()
        path2=GetDefaultWindowsOSDriver()

        SOURCE=os.path.join(path1,'NortonInstaller','Logs')
        if not (os.path.exists(SOURCE)):
            return False
        DESTI=os.path.join(WORKING_OUTPUT_DIR,'Logs')
        shutil.copytree(SOURCE,DESTI)

        if os.path.exists(os.path.join(DESTI,'Url.txt')):
            return True
        else:
            return False

    except Exception as e:
        return str(e)

##========================================================================================================
## @brief           This function will install Product in basic mode /qr (or /qb) with or without *Switch
##                  (only display the progess page during the installation)
##                  
##              
## @param           sPath       = r"C:\working\input\setup.exe"
##                  *Switch     = "/BTP 0", "/BTPDrivers 0", or etc...
##                  Ex: InstallWithBasicMode(sPath, "/BTP 0", "/BTPDrivers 0")
##                      InstallWithBasicMode(sPath)     second parameter is null or not exist, the installation 
##                                                      will proceed with /qr
##
## @returns             0
##                      1
##                      False
##
## @exception        return str(e) = exception error
##========================================================================================================
def InstallWithBasicMode(sPath, *Switch):
    try:
        InstRetCode=1
        InstArg=[sPath,"/qr"]
        if os.path.exists(sPath) is True:
            if len(Switch) == 0:
                InstRetCode=subprocess.call(InstArg)
                logging.info("DINGUTL:"+"InstallWithBasicMode() Not Found Any Switches Parameters. Installation is run by /QR by default")  
            else:
                for s in Switch:
                    InstArg.append(s)
                InstRetCode=subprocess.call(InstArg)
                logging.info("DINGUTL:"+"InstallWithBasicMode() Installation is run with Switches") 

            logging.info("DINGUTL:"+"InstallWithBasicMode() Return InstRetCode = %s" % InstRetCode)
            logging.info("DINGUTL:"+"---END SilentInstallWithSwitch()---")
            logging.info("------------------------") 
            return InstRetCode
        else:
            logging.info("DINGUTL:"+"InstallWithBasicMode() Installer is not found. Exists")
            logging.info("DINGUTL:"+"---END InstallWithBasicMode()---")
            logging.info("------------------------")  
            return False
    except Exception as e:
        logging.error("DINGUTL:"+"InstallWithBasicMode(): Exception Error occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END InstallWithBasicMode()---")
        logging.info("------------------------")
        return str(e)

##========================================================================================================
## @brief               This function will install Product in silent mode with or without *Switch
##                 
##                  
##              
## @param               sPath       = r"C:\working\input\setup.exe"
##                      *Switch     = "/BTP 0", "/BTPDrivers 0", or etc...
##                      Ex: SilentInstallWithSwitch(sPath, "/BTP 0", "/BTPDrivers 0")
##                      SilentInstallWithSwitch(sPath)     second parameter is null or not exist, the installation 
##                      will proceed with /qn
##                  
##
## @returns             0
##                      1
##                      False
##
## @exception        return str(e) = exception error
##========================================================================================================
def SilentInstallWithSwitch(sPath, *Switch):
    try:
        InstRetCode=1
        InstArg=[sPath,"/qn"]
        logging.info("DINGUTL:"+"---START SilentInstallWithSwitch()---")
        if os.path.exists(sPath) is True:
            if len(Switch) == 0:
                InstRetCode=subprocess.call(InstArg)
                logging.info("DINGUTL:"+"SilentInstallWithSwitch() Not Found Any Switches Parameters. Installation is run by /QN by default")                                                                 
            else:
                for s in Switch:
                    InstArg.append(s)
                InstRetCode=subprocess.call(InstArg)
                logging.info("DINGUTL:"+"SilentInstallWithSwitch() Installation is run with Switches")
                         
            logging.info("DINGUTL:"+"SilentInstallWithSwitch() Return InstRetCode = %s" % InstRetCode)
            logging.info("DINGUTL:"+"---END SilentInstallWithSwitch()---")
            logging.info("------------------------") 
            return InstRetCode
        else:
            logging.info("DINGUTL:"+"SilentInstallWithSwitch() Installer is not found. Exists")
            logging.info("DINGUTL:"+"---END SilentInstallWithSwitch()---")
            logging.info("------------------------")  
            return False
    except Exception as e:
        logging.error("DINGUTL:"+"SilentInstallWithSwitch(): Exception Error occurs ****Return Value= %s" % str(e))
        logging.info("DINGUTL:"+"---END SilentInstallWithSwitch()---")
        logging.info("------------------------")
        return str(e)

##================================================================================================================================================================
## @brief           DisableNetworkAdapter()  turns the Network Adapter OFF, thus disabling browsing                    
##
## @param           NONE 
##
## @returns         An integer which is Windows Error Code (http://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description)
##
## @exception		A string (catches all exceptions)
##=================================================================================================================================================================

def DisableNetworkAdapter():
    try:
        if IsWin8() or IsWin8_1():
            cmd="netsh interface set interface name=\"Ethernet\" admin=DISABLED"
            val=subprocess.call(cmd)
            return val
        else:
            cmd="netsh interface set interface name=\"Local Area Connection\" admin=DISABLED"
            val=subprocess.call(cmd)
            return val
    except Exception as e:
        return str(e)

##================================================================================================================================================================
## @brief           EnableNetworkAdapter()  turns the Network Adapter ON, thus enabling browsing                    
##
## @param           NONE 
##
## @returns         An integer which is Windows Error Code (http://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description)
##
## @exception		A string (catches all exceptions)
##=================================================================================================================================================================

def EnableNetworkAdapter():
    try:
        if IsWin8() or IsWin8_1():
            cmd="netsh interface set interface name=\"Ethernet\" admin=ENABLED"
            val=subprocess.call(cmd)
            return val
        else:
            cmd="netsh interface set interface name=\"Local Area Connection\" admin=ENABLED"
            val=subprocess.call(cmd)
            return val

    except Exception as e:
        return str(e)

##====================================================================================================================================
## @brief           StartNTPService() starts the 'Norton Test Product' Service which has been stopped             
##
## @param           NONE
##
## @returns         An integer which is Windows Error Code 
##                  (http://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description)
##
## @exception		A string (catches all exceptions)
##=====================================================================================================================================

def StartNTPService(): 
    try :
        SERVICE="Norton Test Product"
        cmd = "net start " + "\"" + SERVICE + "\""
        val=subprocess.call(cmd,shell=True)
        return val
    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           GetFileSize(file) returns the size of the file                      
##
## @param           Full path of the file   (Ex. C:\Samplefile.txt)  
##
## @returns         Size of the file in Bytes (A Long value)    (Ex. 2496128L which is 2.49 MB)
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def GetFileSize(file):
    try :
        if os.path.exists(file):
            STATISTICS = os.stat(file)
            return STATISTICS.st_size
        else:
            return "No file exists in the path!"
    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           GetAnyWindowsPath(num) returns the path of the Windows Folder when the any of the Windows Enumeration under
##                      http://code.snapstream.com/api/bm11/SnapStream.Util.CSIDL.html is given                      
##
## @param           Any number based on the column 'Value' in the above website (Ex. 36)
##
## @returns         A path of Windows Folder (Ex. C:\Windows)
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def GetAnyWindowsPath(num):
    try:
        CSIDL_FOLDER = num
        _SHGetFolderPath = windll.shell32.SHGetFolderPathW
        _SHGetFolderPath.argtypes = [wintypes.HWND,
                    ctypes.c_int,
                    wintypes.HANDLE,
                    wintypes.DWORD, wintypes.LPCWSTR]

        path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
        result = _SHGetFolderPath(0, CSIDL_FOLDER, 0, 0, path_buf)

        if result==0:
            return path_buf.value
        else:
            return result
    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief           CreateNTPIsolateINI(folder) creates ITB Harness specific isolate.ini file 
##                      in the specifed location to use tools 
##                  
##
## @param           Full path of the folder  (Ex. C:\Working\Input\)
##
## @returns         True (success case, isolate.ini created)
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def CreateNTPIsolateINI(folder):
    try:
        if os.path.exists(folder):
            INIFILE=os.path.join(folder,'isolate.ini')
            WriteFile   = open(INIFILE , mode="w")
            WriteFile.write("\n")
            WriteFile.write(r'[isolation]' +"\n")
            WriteFile.write(r'Silo={11111111-1111-1111-1111-111111111111}' +"\n")
            WriteFile.write(r'reghive=Software\Norton' +"\n")
            WriteFile.close()
        else:
            return "The specified folder does not exist!"

        if os.path.exists(os.path.join(folder,'isolate.ini')):
            return True
        else:
            return False

    except Exception as e:
        return str(e)

##=====================================================================================================
## @brief            CreateProductIsolateINI(folder) creates Product specific isolate.ini file 
##                      in the specifed location to use tools 
##                  
## @param           Full path of the folder  (Ex. C:\Working\Input\)
##
## @returns         True (success case, isolate.ini created)
##
## @exception		A string (catches all exceptions)
##======================================================================================================

def CreateProductIsolateINI(folder):
    try:
        if os.path.exists(folder):
            INIFILE=os.path.join(folder,'isolate.ini')
            WriteFile   = open(INIFILE , mode="w")
            WriteFile.write("\n")
            WriteFile.write(r'[isolation]' +"\n")
            WriteFile.write(r'Silo={0C55C096-0F1D-4F28-AAA2-85EF591126E7}' +"\n")
            WriteFile.write(r'reghive=Software\Norton' +"\n")
            WriteFile.close()
        else:
            return "The specified folder does not exist!"

        if os.path.exists(os.path.join(folder,'isolate.ini')):
            return True
        else:
            return False

    except Exception as e:
        return str(e)

##==================================================================================================================================================
## @brief           SearchRecurNortonLogsforCount(SearchStr) returns the "count" of occurance of string inside 
##                          NortonInstall.log files by doing recursive search inside APPDATA\NortonInstaller\Logs\ folder                      
##
## @param           A string to search  [Ex.,  StringLiteral = r'DING::CLayoutCustomizer::VerifyTrust(457) : invalid signature'  ]
##
## @returns         An unsigned integer which is count [Ex., 3 
##                  (When Side Loaded with .flavor which is having no Sign, then inside NortonInstall.log, we have this string 3 times) ]
##
## @exception		A string (catches all exceptions)
##===================================================================================================================================================

def SearchRecurNortonLogsforCount(SearchStr):
    try:
        LogPath=os.path.join(GetCommonAppDataPath(),'NortonInstaller','Logs')       
        Search=SearchStr
        if not isinstance(Search,str):
            return "No String specified"
        
        sum=0
        for folder, dirs , files in os.walk(LogPath):
            for each_file in files:
                str_file=str(each_file)
                if str_file.startswith('NortonInstall') and str_file.endswith('.log'):
                    FileU=os.path.join(folder,each_file)                    
                    shutil.copyfile(FileU,os.path.join(folder,'PyU.txt'))
                    UniToAnsi(os.path.join(folder,'PyU.txt'),os.path.join(folder,'PyA.txt'))
                    with open(os.path.join(folder,'PyA.txt')) as fp:
                        a=0
                        for eachline in fp.readlines():
                            if Search in eachline:
                                a=a+1
                        sum=sum+a 
                    os.remove(os.path.join(folder,'PyU.txt'))
                    os.remove(os.path.join(folder,'PyA.txt'))
        return sum

    except Exception as e:
        return str(e)

##=================================================================================================================================================
## @brief            SearchRecurforCount(FolderPath,SearchStr) returns the "count" of occurance of string inside 
##                         given folder by doing recursive search                     
##
## @param           arg1 : The Folder to search for    [Ex., Folder = r'C:\Working\Input\']
##                  arg2 : The string to search for    [Ex.,  StringLiteral = r'DING::CLayoutCustomizer::VerifyTrust(457) : invalid signature']
##
##
## @returns         An unsigned integer which is count [Ex., 3 
##                  (When Side Loaded with .flavor which is having no Sign, then inside NortonInstall.log, we have this string 3 times) ]
##
## @exception		A string (catches all exceptions)
##==================================================================================================================================================

def SearchRecurforCount(FolderPath,SearchStr):
    try:
                
        FolderPath=os.path.join(FolderPath)      
        if not os.path.exists(FolderPath):
            return "Invalid Folder Path"

        Search=SearchStr
        if not isinstance(Search,str):
            return "No String specified"
        
        sum=0
        for folder, dirs , files in os.walk(FolderPath):
            for each_file in files:
                str_file=str(each_file)
                #if str_file.startswith('NortonInstall') and str_file.endswith('.log'):
                FileU=os.path.join(folder,each_file)                    
                shutil.copyfile(FileU,os.path.join(folder,'PyU.txt'))
                UniToAnsi(os.path.join(folder,'PyU.txt'),os.path.join(folder,'PyA.txt'))
                with open(os.path.join(folder,'PyA.txt')) as fp:
                    a=0
                    for eachline in fp.readlines():
                        if Search in eachline:
                            a=a+1
                    #a = fp.read().count(Search)
                    sum=sum+a
                os.remove(os.path.join(folder,'PyU.txt'))
                os.remove(os.path.join(folder,'PyA.txt'))
        return sum

    except Exception as e:
        return str(e)

##===========================================================================================================================================
## @brief           SearchRecurRebootlessLogsforCount(SearchStr) returns the "count" of occurance of string inside 
##                          RebootlessPatch.log files by doing recursive search inside APPDATA\NortonInstaller\Logs\ folder                      
##
## @param           The string to search [ Ex.,  StringLiteral = r'DING::CLayoutCustomizer::VerifyTrust(457) : invalid signature' ]
##
## @returns         An unsigned integer which is count [Ex., 3 
##                  (When Side Loaded with .flavor which is having no Sign, then inside RebootlessPatch.log, we have this string 3 times) ]       
##
## @exception		A string (catches all exceptions)
##============================================================================================================================================

def SearchRecurRebootlessLogsforCount(SearchStr):
    try:
        LogPath=os.path.join(GetCommonAppDataPath(),'NortonInstaller','Logs')       
        Search=SearchStr
        if not isinstance(Search,str):
            return "No String specified"
        
        sum=0

        for folder, dirs , files in os.walk(LogPath):
            for each_file in files:
                str_file=str(each_file)
                if str_file.startswith('RebootlessPatch') and str_file.endswith('.log'):
                    FileU=os.path.join(folder,each_file)                    
                    shutil.copyfile(FileU,os.path.join(folder,'PyU.txt'))
                    UniToAnsi(os.path.join(folder,'PyU.txt'),os.path.join(folder,'PyA.txt'))
                    with open(os.path.join(folder,'PyA.txt')) as fp:
                        a=0
                        for eachline in fp.readlines():
                            if Search in eachline:
                                a=a+1
                        sum=sum+a 
                    os.remove(os.path.join(folder,'PyU.txt'))
                    os.remove(os.path.join(folder,'PyA.txt'))
        return sum
        
    except Exception as e:
        return str(e)

##=====================================================================================================================================================
## @brief           SearchRecurPatchLogsforCount(SearchStr) returns the "count" of occurance of string inside 
##                          Patch.log files by doing recursive search inside APPDATA\NortonInstaller\Logs\ folder                    
##
## @param           The string to search. Ex.,  StringLiteral = r'DING::CLayoutCustomizer::VerifyTrust(457) : invalid signature' 
##
## @returns          An unsigned integer which is count [Ex., 3 
##                  (When Side Loaded with .flavor which is having no Sign, then inside Patch.log, we have this string 3 times) ]
##
## @exception		A string (catches all exceptions)
##======================================================================================================================================================

def SearchRecurPatchLogsforCount(SearchStr):
    try:
        LogPath=os.path.join(GetCommonAppDataPath(),'NortonInstaller','Logs')       
        Search=SearchStr
        if not isinstance(Search,str):
            return "No String specified"
        
        sum=0
        for folder, dirs , files in os.walk(LogPath):
            for each_file in files:
                str_file=str(each_file)
                if str_file.startswith('Patch') and str_file.endswith('.log'):
                    FileU=os.path.join(folder,each_file)                    
                    shutil.copyfile(FileU,os.path.join(folder,'PyU.txt'))
                    UniToAnsi(os.path.join(folder,'PyU.txt'),os.path.join(folder,'PyA.txt'))
                    with open(os.path.join(folder,'PyA.txt')) as fp:
                        a=0
                        for eachline in fp.readlines():
                            if Search in eachline:
                                a=a+1
                        sum=sum+a
                    os.remove(os.path.join(folder,'PyU.txt'))
                    os.remove(os.path.join(folder,'PyA.txt'))
        return sum
        
    except Exception as e:
        return str(e)

##=====================================================================================================================================================
## @brief           SearchRecurFlavorLogsforCount(SearchStr) returns the "count" of occurance of string inside 
##                          Patch.log files by doing recursive search inside APPDATA\NortonInstaller\Logs\ folder                    
##
## @param           The string to search. Ex.,  StringLiteral = r'DING::CLayoutCustomizer::VerifyTrust(457) : invalid signature' 
##
## @returns          An unsigned integer which is count [Ex., 3 
##                  (When Side Loaded with .flavor which is having no Sign, then inside Flavorizing.log, we have this string 3 times) ]
##
## @exception		A string (catches all exceptions)
##======================================================================================================================================================

def SearchRecurFlavorLogsforCount(SearchStr):
    try:
        LogPath=os.path.join(GetCommonAppDataPath(),'NortonInstaller','Logs')       
        Search=SearchStr
        if not isinstance(Search,str):
            return "No String specified"
        
        sum=0
        for folder, dirs , files in os.walk(LogPath):
            for each_file in files:
                str_file=str(each_file)
                if str_file.startswith('Flavorizing') and str_file.endswith('.log'):
                    FileU=os.path.join(folder,each_file)                    
                    shutil.copyfile(FileU,os.path.join(folder,'PyU.txt'))
                    UniToAnsi(os.path.join(folder,'PyU.txt'),os.path.join(folder,'PyA.txt'))
                    with open(os.path.join(folder,'PyA.txt')) as fp:
                        a=0
                        for eachline in fp.readlines():
                            if Search in eachline:
                                a=a+1
                        sum=sum+a
                    os.remove(os.path.join(folder,'PyU.txt'))
                    os.remove(os.path.join(folder,'PyA.txt'))
        return sum
        
    except Exception as e:
        return str(e)
