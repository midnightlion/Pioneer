import rosbag

for topic, msg, t in rosbag.Bag('umdentischschnell.bag').read_messages():
	if topic == '/tf_static':
		print msg.transforms
