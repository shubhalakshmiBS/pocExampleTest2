
def compare_and_fetch_diff(file_path):
    prev_blob = ""
    prev_content = prev_blob.data_stream.read().decode("utf-8")
 
    current_blob = ""
    current_content = current_blob.data_stream.read().decode("utf-8")
 
    diff = ""