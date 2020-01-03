																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																		/// @description Insert description here
// You can write your code in this editor


var left = mouse_check_button(mb_left)|keyboard_check(vk_left);
var right = mouse_check_button(mb_right)|keyboard_check(vk_right);
var rate = 6;
var xsp_max = 10;

//textFile = file_text_open_write(working_directory+"output-"+global.player_name+".txt");
if (obj_timer.showTime>180 && obj_timer.showTime<=200){
	if (left)
	{
		xsp = 0;
		alarm[0] = 1;
		//xsp += (-xsp_max - xsp) / rate;
	
	}


	if (right)
	{	
		xsp = 0;
		alarm[1] = 1;
		//xsp += (xsp_max - xsp) / rate;
	
	}
}

if (obj_timer.showTime<=180 && obj_timer.showTime>150){
	if (left)
	{
		xsp = 0;
		alarm[0] = 6;
		//xsp += (-xsp_max - xsp) / rate;
	
	}


	if (right)
	{	
		xsp = 0;
		alarm[1] = 6;
		//xsp += (xsp_max - xsp) / rate;
	
	}
}
if (obj_timer.showTime<=150 &&obj_timer.showTime>120){
	if (left)
	{
		xsp = 0;
		alarm[0] = 12;
		//xsp += (-xsp_max - xsp) / rate;
	
	}


	if (right)
	{	
		xsp = 0;
		alarm[1] = 12;
		//xsp += (xsp_max - xsp) / rate;
	
	}
}

if (obj_timer.showTime<=120&&obj_timer.showTime>90){
	if (left)
	{
		xsp = 0;
		alarm[0] = 18;
		//xsp += (-xsp_max - xsp) / rate;
	
	}


	if (right)
	{	
		xsp = 0;
		alarm[1] = 18;
		//xsp += (xsp_max - xsp) / rate;
	
	}
}
if (obj_timer.showTime<=90&&obj_timer.showTime>60){
	if (left)
	{
		xsp = 0;
		alarm[0] = 24;
		//xsp += (-xsp_max - xsp) / rate;
	
	}


	if (right)
	{	
		xsp = 0;
		alarm[1] = 24;
		//xsp += (xsp_max - xsp) / rate;
	
	}
}

if (obj_timer.showTime<=60&&obj_timer.showTime>0){
	if (left)
	{
		xsp = 0;
		alarm[0] = 30;
		//xsp += (-xsp_max - xsp) / rate;
	
	}


	if (right)
	{	
		xsp = 0;
		alarm[1] = 30;
		//xsp += (xsp_max - xsp) / rate;
	
	}
}


if (left && right || !left && !right)
{
	xsp += -xsp/rate;	
}

direction = xsp * -20;
image_angle = direction;
x +=xsp*2;
   
if (place_meeting(x,y,obj_falling)){
	player_health --;
	audio_play_sound(s_1, 0, 0);
	show_debug_message(string(current_year) + "/" + string (current_month) + "/" + string(current_day) +". "+string(current_hour) + ":" + string(current_minute) + ":" + string(current_second)+" hit:" + string(obj_timer.myTime)+ "||" + "Score:"+string(player_health)); 
}
