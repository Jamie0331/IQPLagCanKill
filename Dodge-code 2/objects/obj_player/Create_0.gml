/// @description Insert description here
// You can write your code in this editor
 x = room_width / 2;
 y = room_height * 0.85;
 
 max_health = 1000;
 player_health= max_health;
 size = 10;
 xsp = 0;
 dis = 0;
 
 image_xscale = size;
 image_yscale = size;
 
 for (i=0;i<=10;i++)
 {
	 var ran_x = random(room_width);
	 var ran_y = random(room_height*0.5);
	 var ran_rot = random_range(14,20);
	 
	 var ran_r = random(255);
	 var ran_g = random(255);
	 var ran_b = random(255);
	 var col = make_color_rgb(ran_r,ran_g,ran_b);
	 
	 var obj = instance_create_depth(ran_x,ran_y,0,obj_falling);
	 obj.rot = ran_rot;
	 obj.col = col;
 }