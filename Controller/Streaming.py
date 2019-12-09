from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.mqtt import MQTTUtils


class Streaming(object):
    def __init__(self):
        pass

    def rabbit_mq(self):
        sc = SparkContext()
        ssc = StreamingContext(sc, 1)

        mqttStream = MQTTUtils.createStream(
            ssc,
            "tcp://localhost:1883",  # Note both port number and protocol
            "hello"  # The same routing key as used by producer
        )

        # todo:数据分析模型
        mqttStream.count().pprint()
        ssc.start()
        ssc.awaitTermination()
        ssc.stop()
