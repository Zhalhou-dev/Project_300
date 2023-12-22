from mqtt import paho
import time
import flask
broker = 'broker.emqx.io'
port = 1883
client_id = 'pir'
username = 'motion'
password = ''

app = Flask(__name__)
def on_connect (client,rc,flags,userdata):
	client.subscribe('topicName/pir')

def on_message(client,userdata,msg):
	detection=global;
	detection=msg.payload.decode('utf8')
@app.route('/',methods=["GET"])
def check_distance():
	client = mqtt_client.Client(client_id)
	client.on_connect()
	client.on_message()
	client.connect(broker,port)
loop_start()

for i in range(0,10):
	time.sleep(5)
	print(detection)
	return render_template("1.html",int(detection));
loop_stop()

if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)

