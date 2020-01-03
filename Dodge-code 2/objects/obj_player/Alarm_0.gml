/// @description Insert description here
// You can write your code in this editor
var xsp_max = 15;
var rate = 3;
xsp += (-xsp_max - xsp) / rate;
show_debug_message(string(current_year) + "/" + string (current_month) + "/" + string(current_day) +". "+string(current_hour) + ":" + string(current_minute) + ":" + string(current_second)+" click: "+string(obj_timer.myTime));