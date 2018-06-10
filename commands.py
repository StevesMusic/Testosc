CH_FADER_VOLUME = "/ch/{}/mix/fader ,f"

def change_fader_volume(client, channel, value):
    client.send_message(CH_FADER_VOLUME.format(channel), value)
    return "success!"