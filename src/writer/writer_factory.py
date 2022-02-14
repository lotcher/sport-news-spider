from typing import List

from .es_writer import ESWriter
from .writer import Writer
from .kafka_writer import KafkaWriter
from .file_writer import FileWriter
from src.config import Config


class WriterFactory:
    @classmethod
    def generate(cls) -> List[Writer]:
        writers = {
            'kafka': lambda config: KafkaWriter(**config),
            'file': lambda config: FileWriter(**config),
            'es': lambda config: ESWriter(**config),
        }
        return [writers[name](writer_config or {}) for name, writer_config in Config.writers.items()]
