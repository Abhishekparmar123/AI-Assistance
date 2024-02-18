import os


songs_dir = r"C:\Users\abhis\Music\new musuc"
songs = os.listdir(songs_dir)
os.startfile(os.path.join(songs_dir, songs[0]))
