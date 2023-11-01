from instruments import Guitar, Flute, EletricGuitar, Distortion, InstrumentKind


gianini = Guitar("Gianini m2", kind=InstrumentKind.keys)

print(gianini.play())
print(gianini.colors)


yamaha = Flute("Yamaha Magic Flute")
print(yamaha.play())
print(yamaha.colors)


lespaul = EletricGuitar("lespaul m1")
print(lespaul.play(distortion=Distortion.wave))
print(lespaul.play(distortion=Distortion.whisper))