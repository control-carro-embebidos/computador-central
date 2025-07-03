from pop_corn.upy_html.canvas_upy_html import Canvas_upy_html


import network
import socket
import ure
import json
import time





# import socketpool
# import wifi
import os  # Assuming a filesystem is available
import network
import socket
#import ure
#import json
#import time



class Context_upy_html:
    def __init__(self,name_net="Ejemplo",psw_net="12345678",ap=False):
        self.name_net=name_net
        self.psw_net=psw_net
        self.ap=ap
        self.after_list=[]
        self.gadgets=[
      {
        "type": "checkboxRow",
        "count": 3
      },
      {
        "type": "canvas",
        "canvasWidth": 200,
        "canvasHeight": 100
      }
    ]

        self.json2send=[
            {
                "gadget_index":0,
                "checkBox_index":1,
                "chackBox_value":True
            },
            {
                "gadget_index":1,
                "canvas_fillStyle": "blue",
                "canvas_shape": "ellipse",
                "canvas_elli_x": 50,
                "canvas_elli_y": 50,
                "canvas_elli_rw": 25,
                "canvas_elli_rh": 25,
                "canvas_elli_angini_deg": 0,
                "canvas_elli_angfin_deg": 360,
            }
        ]
        
        
        self.html="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multiple Canvases and Checkboxes</title>
</head>
<body>

  <script>
  
class CheckboxRow {
    constructor( numCheckboxes) {
        this.numCheckboxes = numCheckboxes;
        this.checkboxes = [];
        this.row = document.createElement('div');
        this.createCheckboxesWithLabels();
    }

    // Create the checkboxes with labels and append them to the container
    createCheckboxesWithLabels() {
        const row = this.row; // Wrapper for the checkboxes
        row.style.display = 'flex';
        row.style.flexDirection = 'row';
        row.style.alignItems = 'center';
        row.style.gap = '10px';

        for (let i = 0; i < this.numCheckboxes; i++) {
            const container = document.createElement('div');
            container.style.display = 'flex';
            container.style.flexDirection = 'column';
            container.style.alignItems = 'center';

            // Create labels
            const increasingLabel = document.createElement('span');
            increasingLabel.textContent = 'index'+ i; // Increasing index
            increasingLabel.style.fontSize = '12px';

            const decreasingLabel = document.createElement('span');
            decreasingLabel.textContent = 'bit'+(this.numCheckboxes - 1 - i); // Decreasing index
            decreasingLabel.style.fontSize = '12px';

            // Create checkbox
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.dataset.index = i;

            // Append labels and checkbox to the container
            container.appendChild(increasingLabel);
            container.appendChild(decreasingLabel);
            container.appendChild(checkbox);

            // Append the container to the row
            row.appendChild(container);

            this.checkboxes.push(checkbox);
        }

    }
    
    get_obj(){
    return this.row
    }

    // Update a single bit (checkbox) at the specified index
    updateIndex(index, value) {
        if (index >= 0 && index < this.numCheckboxes) {
            this.checkboxes[index].checked = Boolean(value);
        } else {
            throw new Error(`Index out of bounds: ${index}`);
        }
    }

    // Read the state of a single bit (checkbox) at the specified index
    readBit(index) {
        if (index >= 0 && index < this.numCheckboxes) {
            return this.checkboxes[index].checked;
        } else {
            throw new Error(`Index out of bounds: ${index}`);
        }
    } 
}
  
  
  //jsonData_here

       function sendJson(){//jsonData) {

            //fetch(`/api?${queryString}`)
            fetch('/api')
                .then(response => response.json())  // Expecting a JSON response
                .then(data => {
                    //console.log('receivedJson',data);                                       
                    for (element of data) {
                        //console.log('elem ',element);
                        update_gadgets(element);
                    }
                 })
                .catch(error => console.error('sendJson Error:', error));
        }

       function update_gadgets(element){
           const gadget=gadgets[element["gadget_index"]]
           const gcn=gadget.constructor.name
           //console.log('update gadget construtcor:',gcn)
           if (gcn=="CheckboxRow"){
               //console.log('CheckBox')
               gadget.updateIndex(element["checkBox_index"],element["chackBox_value"])
           }
           if (gcn=="CanvasRenderingContext2D"){
               //console.log('CanvasRenderingContext2D')
               if (element["canvas_shape"]=="ellipse"){
                    gadget.beginPath();
                    gadget.ellipse(element.canvas_elli_x, element.canvas_elli_y, element.canvas_elli_rw, element.canvas_elli_rh, 0, element.canvas_elli_angini_deg*Math.PI /180, element.canvas_elli_angfin_deg*Math.PI /180) 
                    gadget.fill();
                    gadget.stroke();
               }
               if (element["canvas_shape"]=="reset"){
                    gadget.reset();
               }
           }
       }
       
       
// Iterate over the JSON data
    let gadgets=[]
    jsonData.forEach(item => {
      if (item.type === "canvas") {
        const rowContainer = document.createElement('div');
        const canvas = document.createElement('canvas');
        canvas.width = item.canvasWidth;
        canvas.height = item.canvasHeight;
        rowContainer.appendChild(canvas);
        document.body.appendChild(rowContainer);

        const ctx = canvas.getContext('2d');
        
        // Optional: You can draw something on the canvas if needed
        ctx.fillStyle = "lightgray";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        gadgets.push(ctx);
        ctx.fillStyle = "black";
      }

      if (item.type === "checkboxRow") {
        const checkboxRow = new CheckboxRow( item.count);
        gadgets.push(checkboxRow);

        document.body.appendChild(checkboxRow.get_obj());
      }
    });
    
    const intervalID = setInterval(sendJson, 300);

  </script>
</body>
</html>

"""


    def _api(self, request_str):

        #print('api_in')        
        response_json = json.dumps(self.json2send)
        self.json2send=[]
        #print(response_json)
        response_str=('HTTP/1.1 200 OK\r\n'
                + 'Content-Type: application/json\r\n'
                + 'Connection: close\r\n\r\n'
                + response_json)
        #print('api_out',response_str)
        return (response_str )

# Colocar comandos, unos para canvas y otros para checkbox, así como leer el estado del checkbox y recibir el mouse del canvas
#En un canvas se puede mover el mouse, y colocar un flag para mostarlo  o no.
#El mouse se puede mover internamente en el canvas o externamente

# Start the server
    def _start_server(self,name,psw,ap=True):
        if ap:
            # wifi.radio.start_ap("RPi-Pico", "12345678")
            # print("wifi.radio ap:", wifi.radio.ipv4_address_ap)
            wlan=network.WLAN(network.AP_IF)
            wlan.active(True)
            #wlan.config(essid="RPi-Pico", password="12345678")
            wlan.config(essid=name, password=psw)
            if wlan.active():            
                print("Current SSID",wlan.config('essid'))
                print("IP Address:", wlan.ifconfig()[0])
            else:
                print("AP inactive:", wlan.status())

        else:    
            # wifi.radio.connect("Ejemplo","12345678")
            # print("wifi.radio:", wifi.radio.ipv4_address)
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            #wlan.connect("Ejemplo","12345678")
            wlan.connect(name,psw)
            for _ in range(10):
                if wlan.isconnected():
                    break
                print('.',end='')
                time.sleep(1)
            if wlan.isconnected():
                print("IP Address:", wlan.ifconfig())
            else:
                print("Falied:", wlan.status())
                # The status() method provides connection states:
                            # 
                # Handle connection error
                # Error meanings
                # 0  Link Down
                # 1  Link Join
                # 2  Link NoIp
                # 3  Link Up
                # -1 Link Fail
                # -2 Link NoNet
                # -3 Link BadAuth        


    #     pool = socketpool.SocketPool(wifi.radio)
    #     s = pool.socket()
    #     s.bind(('', 80))
    #     s.listen(5)
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        server_socket = socket.socket()
        server_socket.bind(addr)
        server_socket.listen(1)
        
        print('Server listening on', addr)


        return server_socket

    # Get the correct content type based on file extension

    # Serve files or handle API requests
    def _handle_request(self,client):
        #buffer = bytearray(1024)  # Create a mutable buffer
        #bytes_received, address = client.recvfrom(buffer)  # Receive data into the buffer and get the sender's address
        request, address = client.recvfrom(1024)#buffer)  # Receive data into the buffer and get the sender's address
        #request = buffer[:bytes_received]
        request_str = request.decode('utf-8')
        #print('request_str',request_str)
        # Extract the requested file from the request

        # Check if the request is for the API endpoint
        if request.startswith('GET /api'):
            # Call the api() method from api.py
            #print('/api')
            client.send(self._api( request_str))
            client.close()
            return

        
        #print('NO /api')
        # Get the content type for the requested file
        content = self.html.replace("//jsonData_here","jsonData="+str(self.gadgets))

        # Send headers
        client.send('HTTP/1.1 200 OK\r\n')
        client.send(f'Content-Type: text/html\r\n')
        client.send('Connection: close\r\n\r\n')

        # Send the file content in chunks
        print('len(content)=',len(content))
        client.send(content)
        #print(len(all_file),len(chunk),chunk)
        #time.sleep_ms(100)
        client.close()
        return

    def add_gadget(self,gadget_dic):
        self.gadgets.append(gadget_dic)
        return len(self.gadgets)-1

    def add_shape(self,shape):
        #print('add_shape',shape)
        self.json2send.append(shape)




#################################################    
    def canvas(self,scene,**props):
        return Canvas_upy_html(scene,context=self,**props)
 
    def after_ms(self,t_ms,callback):
        self.after_list.append((time.ticks_add(time.ticks_ms(), t_ms),callback))
        
#     def in_bits(self,num_bits,**props):
#         return In_upy_html(num_bits,**props)
#         
#     def out_bits(self,num_bits,**props):
#         return Out_upy_html(num_bits,**props)

#     def mainloop(self,**props):
#         server.mainloop(name="RPi-Pico", psw="12345678",ap=True)

    def mainloop(self):
        s = self._start_server(name=self.name_net, psw=self.psw_net, ap=self.ap)
        while True:
            conn, addr = s.accept()
            #print(f'Got a connection from {addr}')
            self._handle_request(conn)
            
            current_time = time.ticks_ms()
            to_remove = []
            for timer in self.after_list:
                ticks_ms_,callback=timer
                if time.ticks_diff(ticks_ms_, current_time)<=0:
                    callback()
                    to_remove.append(timer)
                    
            for timer in to_remove:
                self.after_list.remove(timer)            
        
        
if __name__ == "__main__":
    ctx=Context_upy_html(name_net="Ejemplo", psw_net="12345678",ap=False)
    ctx.mainloop()
        