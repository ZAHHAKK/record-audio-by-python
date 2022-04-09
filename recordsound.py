import ctypes
ctypes.windll.winmm.mciSendStringW("open new Type waveaudio Alias recsound", "", 0, 0)
ctypes.windll.winmm.mciSendStringW("record recsound", "", 0, 0)
input()
ctypes.windll.winmm.mciSendStringW("save recsound C:\\record.wav", "", 0, 0)
ctypes.windll.winmm.mciSendStringW("close recsound ", "", 0, 0)
