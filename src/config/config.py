from typing import List, Dict

import yaml


class Config:
    writers: Dict[str, Dict]

    @classmethod
    def from_yaml(cls, yaml_path: str):
        for k, v in yaml.safe_load(open(yaml_path)).items():
            setattr(cls, k, v)
