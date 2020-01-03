/// @description Insert description here
// You can write your code in this editor

var offset = 10;

direction += rot;
y += rot / 2;
image_angle = direction;

if(y > room_height + offset)
{
	var ran_r = random(255);
	var ran_g = random(255);
	var ran_b = random(255);
	 
	col = make_color_rgb(ran_r,ran_g,ran_b);
	rot = random_range(5,20);
	
	x = random(room_width);
	y = -offset;
}