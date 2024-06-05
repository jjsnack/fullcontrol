default_initial_settings = {
    "name": "Sovol-SV06 Plus",
    "manufacturer": "Sovol 3D",
    "start_gcode": "G28 ;Home\n\nM420 S1;\nG92 E0 ;Reset Extruder\nG1 Z2.0 F3000 ;Move Z Axis up\nG1 X10.1 Y20 Z0.28 F5000.0 ;Move to start position\nG1 X10.1 Y200.0 Z0.28 F1500.0 E15 ;Draw the first line\nG1 X10.4 Y200.0 Z0.28 F5000.0 ;Move to side a little\nG1 X10.4 Y20 Z0.28 F1500.0 E30 ;Draw the second line\nG92 E0 ;Reset Extruder\nG1 Z2.0 F3000 ;Move Z Axis up\n",
    "end_gcode": "G91 ;Relative positioning\nG1 E-2 F2700 ;Retract a bit\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X0 Y220 F3000 ;Wipe out\nG1 Z10 ;Raise Z more\nG90 ;Absolute positionning\n\nG1 X0 Y{data['build_volume_y']} ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\n\nM84 X Y E ;Disable all steppers but Z\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 150.0,
    "travel_speed": 200.0,
    "dia_feed": 1.75,
    "build_volume_x": 300,
    "build_volume_y": 300,
    "build_volume_z": 340,
}
