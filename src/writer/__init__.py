from bools.log import Logger

from .writer import Writer

try:
    from .kafka_writer import KafkaWriter
except Exception as e:
    Logger.error(e)

from .file_writer import FileWriter
