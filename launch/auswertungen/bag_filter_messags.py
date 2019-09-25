import rosbag

files = ["umdentischzickzack.bag", "raum207zweieingaenge.bag", "umdentischrueckwaerts.bag", "umdentisch.bag", "umdentischschnell.bag"]

print files

for i in range(len(files)):
	with rosbag.Bag(files[i] + '2', 'w') as outbag:
		for topic, msg, t in rosbag.Bag(files[i]).read_messages():
			if topic == "/tf_static":
				del msg.transforms[6]
			if not (topic == "/tf" and msg.transforms[0].child_frame_id == 'imu'):
				outbag.write(topic, msg, t)

