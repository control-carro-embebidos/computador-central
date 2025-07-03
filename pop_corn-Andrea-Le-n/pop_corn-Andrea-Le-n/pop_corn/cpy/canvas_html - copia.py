import wifi
import socketpool
import time

# Connect to the Wi-Fi network
wifi.radio.connect("Ejemplo", "12345678")
print("wifi.rado",wifi.radio.hostname, wifi.radio.ipv4_address)

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Create a TCP/IP socket
server_socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM)

# Bind the socket to the port
server_socket.bind(("0.0.0.0", 80))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening on port 80")

# Set the socket to non-blocking mode
server_socket.setblocking(False)

html_response = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuadrícula de Grises</title>
    <style>
        body {
            display: grid;
            grid-template-columns: repeat(40, 1fr);
            grid-template-rows: repeat(30, 1fr);
            margin: 0;
            height: 100vh;
            width: 100vw;
        }
        div {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <script>


        const grayValues = "data_image" ;
        for (let i = 0; i < 40 * 30; i++) {
            let div = document.createElement('div');
            let grayValue =grayValues.charCodeAt(i) ;
             grayValue= ((grayValue==47)?92:grayValue)-48;
            div.style.backgroundColor = `rgb(${grayValue}, ${grayValue}, ${grayValue})`;
            document.body.appendChild(div);
        }
    </script>
</body>
</html>
'''
data_image="".join([ r''.join([chr(i+j+48 if i+j+48 !=92 else 47) for i in range(40)]) for j in range(30)])



clients = []

while True:
    try:
        # Accept a new connection
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        client_socket.setblocking(False)  # Set client socket to non-blocking
        clients.append(client_socket)
    except OSError:
        print('# No new connections, move on')
        pass

    # Check existing clients for requests
    for client_socket in clients:
        try:
            data = bytearray(1024)  # Create a mutable buffer
            bytes_received, address = client_socket.recvfrom_into(data)  # Receive data into the buffer and get the sender's address
            #data = client_socket.recv(1024)
            if data:
                print(f"Received data: {data}")
                client_socket.send(html_response.replace('data_image',data_image).encode('utf-8'))  # Send the HTML response
                client_socket.close()
                clients.remove(client_socket)
            else:
                print("Client disconnected")
                clients.remove(client_socket)
                client_socket.close()
        except OSError:
            # No data received, move on
            pass

    # Add a small delay to avoid high CPU usage
    time.sleep(1)
