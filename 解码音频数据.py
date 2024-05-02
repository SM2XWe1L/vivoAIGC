# -*- coding: utf-8 -*-
import wave
import io


class ShortTTS(object):
    vivoHelper = "vivoHelper"
    yunye = "yunye"
    wanqing = "wanqing"
    xiaofu = "xiaofu"
    yige_child = "yige_child"
    yige = "yige"
    yiyi = "yiyi"
    xiaoming = "xiaoming"


class LongTTS(object):
    x2_vivoHelper = "vivoHelper"
    x2_yige = "x2_yige"
    x2_yige_news = "x2_yige_news"
    x2_yunye = "x2_yunye"
    x2_yunye_news = "x2_yunye_news"
    x2_M02 = "x2_M02"
    x2_M05 = "x2_M05"
    x2_M10 = "x2_M10"
    x2_F163 = "x2_F163"
    x2_F25 = "x2_F25"
    x2_F22 = "x2_F22"
    x2_F82 = "x2_F82"


'''
input:
    pcmdata: pcm audio data
output:
    wav file-like object
'''


def pcm2wav(pcmdata: bytes, channels=1, bits=16, sample_rate=24000):
    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))
    io_fd = io.BytesIO()
    wavfile = wave.open(io_fd, 'wb')
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcmdata)
    wavfile.close()
    io_fd.seek(0)
    return io_fd


if __name__ == '__main__':
    from tts_examples import TTS, AueType

    for k, v in ShortTTS.__dict__.items():
        if k.find('__') != -1:
            continue
        print(k, v)
        input_params = {
            # 修改为你的app_id 和 app_key
            'app_id': 'your_app_id',
            'app_key': 'your_app_key',
            'engineid': 'short_audio_synthesis_jovi'
        }
        tts = TTS(**input_params)
        tts.open()
        # pcm
        pcm_buffer = tts.gen_radio(aue=AueType.PCM, vcn=k, text='你好呀')
        wav_io = pcm2wav(pcm_buffer)
        with open(f'{k}_pcm.wav', 'wb') as fd:
            fd.write(wav_io.read())
        break

    for k, v in LongTTS.__dict__.items():
        if k.find('__') != -1:
            continue
        print(k, v)
        input_params = {
            # 修改为你的app_id 和 app_key
            'app_id': 'your_app_id',
            'app_key': 'your_app_key',
            'engineid': 'long_audio_synthesis_screen'
        }
        tts = TTS(**input_params)
        tts.open()
        # pcm
        pcm_buffer = tts.gen_radio(aue=AueType.PCM, vcn=k, text='你好呀')
        wav_io = pcm2wav(pcm_buffer)
        with open(f'{k}_pcm.wav', 'wb') as fd:
            fd.write(wav_io.read())
        break