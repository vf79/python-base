# Abstração e Herança com dataclass
# Enum no Python
# Dataclass com valor default com erro
# Super

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List

# Enumeração/Enumerador
class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"


class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...


@dataclass
class DataInstrumentMixin: # deve ser usado junto com outra classe
    name: str
    kind: InstrumentKind
    sound: str
    colors: List[str] = field(default_factory=list)


class Instrument(DataInstrumentMixin, ABCInstrument):
    ...



@dataclass
class Guitar(Instrument):
    n_strings: int = 6
    sound: str = 'Ding Ding Ding'
    kind: InstrumentKind = InstrumentKind.string
    colors: List[str] = field(default_factory=lambda: ["green", "black"])

    def play(self):
        return self.sound


@dataclass
class EletricGuitar(Guitar):
    sound: str = "Wah Wah Wah"

    def play(self, distortion: Distortion=Distortion.wave):
        return_from_base_class = super().play()
        if distortion == "wave":
            return "~~~".join(return_from_base_class.split())
        elif distortion == "whisper":
            return "...".join(return_from_base_class.split())
        return return_from_base_class



@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind
    colors: List[str] = field(default_factory=lambda: ["beige", "white"])

    def play(self):
        return self.sound
