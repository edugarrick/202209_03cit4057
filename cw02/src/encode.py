import WavSteg as en

WAVE_FILE = "cw02/doc/music.wav"
SECRET_BMP = "cw02/doc/secret.bmp"
OUTPUT_WAVE_FILE = "cw02/doc/musichidden.wav"

def main():
    en.hide_data(
        WAVE_FILE,
        SECRET_BMP,
        OUTPUT_WAVE_FILE,
        1 )

if __name__ == "__main__":
    main()