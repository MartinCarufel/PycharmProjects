import music_tag


def methode_1():
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


def methode_2():
    from tinytag import TinyTag
    f = TinyTag.get("01 Maudite promesse.m4a")
    tag_list = {"album":f.album, "album_artist":f.albumartist, "artist":f.artist, "comment":f.comment, "composer":f.composer,
                "disc":f.disc, "total_disk":f.disc_total, "genre":f.genre, "track_total":f.track_total, "track":f.track,
                "title":f.title, "yeear":f.year, "bitrate":f.bitrate, "duration":f.duration, "channel":f.channels,
                "samplerate":f.samplerate}
    for tag, val in tag_list.items():
        print(f"{tag} : {val}")

methode_2()

