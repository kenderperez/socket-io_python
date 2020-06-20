from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG'] = True
socket_io = SocketIO(app)

#RUTAS 

@app.route('/')
def index():
    return render_template('index.html')

#SocketIO

#Recivimos un mensaje y lo guardamos en la variable msg
@socket_io.on('message') 
def handleMessage(msg):
    #imprimimos el mensaje por pantalla
    print('Message: ' + msg)
    #enviamos el mensaje a todos los clientes conectados
    send(msg, broadcast = True)


#Iniciar Servidor
if __name__ == '__main__':
    socket_io.run(app)