# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)  # ADDED LINE FROM TEXT - server listen for TCP connection requests from the client -() MAX QUEUED REQUESTS
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
#    connectionSocket, addr = #Fill in start     #Fill in end
    connectionSocket, addr = serverSocket.accept()   # ADDED 
    try:

      try:
#        message = #Fill in start    #Fill in end  
        message = connectionSocket.recv(1024).decode()  # ADDED for receiving request into message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start     #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())  # ADDED SUCCESS FROM PPT, ENCODE FOR TRANSMISSION

        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start

        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()  # ADDED CLOSE
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
