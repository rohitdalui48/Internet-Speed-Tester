import director as dr

a = int(input("What you want to test about your network\n1. Dowloading Speed\n2.Uploading Speed"))

if(a==1) : print(f"Downloading Speed : {dr.test_download_speed}")

elif(a==2) : print(f"Uploading Speed : {dr.test_upload_speed}")

else : print("give a proper input")