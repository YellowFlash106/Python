try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print('File Not Found')
finally: 
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete") 