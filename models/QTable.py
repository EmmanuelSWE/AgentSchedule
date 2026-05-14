# q table clss 
# author Emmanuel Ashimwe

from typing import Dict
from dataclasses import dataclass,field

@dataclass
class Qtable:
    qValues: Dict[str, int ] = field(default_factory = dict)