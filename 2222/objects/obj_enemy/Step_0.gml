/// @DnDAction : YoYo Games.Common.If_Variable
/// @DnDVersion : 1
/// @DnDHash : 28E8CA88
/// @DnDArgument : "var" "y"
/// @DnDArgument : "op" "2"
/// @DnDArgument : "value" "room_height"
if(y > room_height)
{
	/// @DnDAction : YoYo Games.Common.Variable
	/// @DnDVersion : 1
	/// @DnDHash : 72E2A038
	/// @DnDParent : 28E8CA88
	/// @DnDArgument : "var" "y"
	y = 0;

	/// @DnDAction : YoYo Games.Common.Variable
	/// @DnDVersion : 1
	/// @DnDHash : 51A0A658
	/// @DnDParent : 28E8CA88
	/// @DnDArgument : "expr" "random(room_width)"
	/// @DnDArgument : "var" "x"
	x = random(room_width);
}