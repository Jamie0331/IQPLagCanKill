/// @description Insert description here
// You can write your code in this editor
draw_self();
draw_set_font(font0);
draw_set_color(c_white)
draw_text(320,6,"Current Score: " +string(player_health));
draw_sprite_ext(spr_square,0,x,y,image_xscale,image_yscale,image_angle,c_red,1);

draw_text(220,6,string(global.player_name))