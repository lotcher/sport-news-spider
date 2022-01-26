from typing import List, Dict

import yaml


class Config:
    writers: Dict[str, Dict]

    @classmethod
    def init(cls, configs):
        for k, v in configs.items():
            setattr(cls, k, v)

    @classmethod
    def from_yaml(cls, yaml_path: str):
        for k, v in yaml.safe_load(open(yaml_path)).items():
            setattr(cls, k, v)
