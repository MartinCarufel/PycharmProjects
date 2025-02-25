import music_tag

all_metadata = ["album","albumartist","artist","artwork","comment","compilation",
                "composer","discnumber","genre","lyrics","totaldiscs","totaltracks",
                "tracknumber","tracktitle","year","isrc","#bitrate","#codec","#length",
                "#channels","#bitspersample","#samplerate"]

f = music_tag.load_file("01 Maudite promesse.m4a")

for tag in all_metadata:
    try:
        print(f"{tag}: {f[tag]}")
    except:
        pass


