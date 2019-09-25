import rosbag

for topic, msg, t in rosbag.Bag('umdentisch.bag2').read_messages():
	if topic == '/tf_static':
		print msg.transforms
