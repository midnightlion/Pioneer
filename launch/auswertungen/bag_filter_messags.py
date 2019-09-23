import rosbag

with rosbag.Bag('umdentischschnell2.bag', 'w') as outbag:
    for topic, msg, t in rosbag.Bag('umdentischschnell.bag').read_messages():
	if not (topic == "/tf" and msg.transforms[0].child_frame_id == 'imu'):
		outbag.write(topic, msg, msg.header.stamp if msg._has_header else t)
