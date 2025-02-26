import Files
import Files.downloading as downloading
import Files.uploading as uploading

def test_download_speed():
    return downloading.tester_download()

def test_upload_speed() : 
    return uploading.tester_upload()



