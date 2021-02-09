while True:
    print("sound level:" + input.sound_level() +3.7)
    if input.sound_level() >13:
        light.set_all(light.rgb(0,255,255))
else: 
    light.clear()