from speedtest import Speedtest

st = Speedtest()
def tester_upload() :
    speed = st.upload()/(1024*1024)
    print(f"your network's uploading speed is : {speed} Mbps")
    return

if(__name__=="__main__") : tester_upload()