default_initial_settings = {
    "name": "ELEGOO NEPTUNE 3 Pro",
    "manufacturer": "ELEGOO",
    "start_gcode": ";ELEGOO NEPTUNE 3 Pro\nM220 S100 ;Set the feed speed to 100%\nM221 S100 ;Set the flow rate to 100%\nG90\nG28 ;home\n;M420 S1 Z10;Uncomment to enable progressive compensation height of 10mm\nG92 E0 ;Reset Extruder\nG1 Z0.45 F300\nG1 X1.5 Y20 F5000.0 ;Move to start position\nG1 Y120.0 F600.0 E15 ;Draw the first line\nG1 X0.5 F1000.0 ;Move to side a little\nG1 Y20 F600 E30 ;Draw the second line\nG92 E0 ;Reset Extruder",
    "end_gcode": "G91 ;Relative positionning\nG1 E-2 F2700 ;Retract a bit\nG1 E-8 X5 Y5 Z3 F3000 ;Retract\nG90 ;Absolute positionning\nG1 X0 Y{data['build_volume_y']} ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\nM84 X Y E ;Disable all steppers but Z",
    "bed_temp": 70,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 150,
    "dia_feed": 1.75,
    "build_volume_x": 235,
    "build_volume_y": 235,
    "build_volume_z": 280,
}
