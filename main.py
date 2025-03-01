import Files.downloading as downloading
import Files.uploading as uploading

a = int(input("What you want to test about your network\n1. Dowloading Speed\n2.Uploading Speed\n"))

if(a==1) : downloading.tester_download()

elif(a==2) : uploading.tester_upload()

else : print("give a proper input")