from Clip import Clip
from ArtClip import ArtClip
from Player import Player


def main():
	c1 = Clip('singel1', 1900)
	c2 = ArtClip('gangam', 2012, 3)
	c3 = ArtClip('moon', 2001, 4)
	c4 = Clip('shalom alichem', 1702)
	c6 = ArtClip('yeled shel haba', 2012, 5)
	c7 = ArtClip('halev shely', 2201, 2)
	clips = [c1, c2, c3, c4, c6, c7]
	
	c5 = Player(clips)
	
	print(c1)
	print(c2)
	
	c1.play()
	print(c1.is_played)
	
	c1.stop()
	print(c1.is_played)
	
	print(c3.is_valid_for_euro())
	print(c7.is_valid_for_euro())
	
	
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	c5.__next__()
	print()
	print(c1.is_played)
	print(c2.is_played)
	print(c3.is_played)
	print(c4.is_played)
	print(c6.is_played)
	print(c7.is_played)
	print(c5.current)
	
	print()
	print(c5.clips)
	c5.shuffle()
	print(c5.clips)
	
	
	
	
if __name__=='__main__':
	main()
