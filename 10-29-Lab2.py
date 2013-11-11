def colorfunc (foreground_color = 'purplish-gray', background_color = 'vomit yellow', link_color = 'programmer gray', visited_link_color = 'berry cheesecake'):
	print 'foreground_color is: ', foreground_color
	print 'background_color is: ', background_color
	print 'link_color is: ', link_color
	print 'visited_link_color is: ', visited_link_color

colorfunc(foreground_color = 'cerulean')

def colorfunc2 (**kwargs):
	print 'The keyword argument is ', kwargs

colorfunc2 (foreground_color = 'terracotta', background_color = 'saffron', link_color = 'puce', visited_link_color = 'aubergine')

print [(i, j) for i in range (4) for j in range(3) ]

print [(i, j) for i in range(4) for j in range (3) if not i%2]

[x**2 for x in range(3)]

[x+y for x in range(3) for y in range(5, 7)]

[name for name in dir(__builtin__) if 'Error' in name]
