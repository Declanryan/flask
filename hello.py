 

from flask import Flask, jsonify 
import socket 
import multiprocessing 
import os 
 
 
app = Flask(__name__) 
 
 
@app.route('/status') 
def system_info(): 
    data = {} 
    data['hostname'] = socket.gethostname() 
    data['ip_address'] = socket.gethostbyname(socket.gethostname()) 
    data['cpus'] =str(multiprocessing.cpu_count())
    data['memory'] =str(round(get_mem(), 2))
    return jsonify(data) 
 
 
def get_mem(): 
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') 
    mem_gib = mem_bytes/(1024.**3) 
    return mem_gib 
     
    
if __name__ == '__main__': 
    app.run()

