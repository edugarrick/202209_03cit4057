import WavSteg as en

WAVE_FILE = "cw02/doc/music.wav"
SECRET_BMP = "cw02/doc/secret.bmp"
OUTPUT_WAVE_FILE = "cw02/doc/musichidden.wav"
RECOVERD_BMP = "cw02/doc/recover.bmp"

def main():
    en.recover_data(
        OUTPUT_WAVE_FILE,
        RECOVERD_BMP,
        1,
        460000 )

if __name__ == "__main__":
    main()