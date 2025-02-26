import speedtest

st = speedtest.Speedtest()
def tester_download() :
    speed = st.download()/(1024*1024)
    print(f"your network's downloading speed is : {speed} Mbps")
    return

if(__name__=="__main__") : tester_download() 