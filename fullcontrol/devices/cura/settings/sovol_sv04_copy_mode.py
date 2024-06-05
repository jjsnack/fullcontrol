default_initial_settings = {
    "name": "Sovol SV04 Copy Mode",
    "manufacturer": "Sovol 3D",
    "start_gcode": ";SV04 start\nM140 S{data['bed_temp']};\nM104 S{data['nozzle_temp']};\nM280 P0 S160;\nG4 P100;\nG28;\nM420 S1;\nM190 S{data['bed_temp']};\nM109 S{data['nozzle_temp']};\nG92 E0;\nG1 X10.1 Y20 Z0.28 F5000.0;\nG1 X10.1 Y200.0 Z0.28 F1500.0 E15;\nG1 X10.4 Y200.0 Z0.28 F5000.0;\nG1 X10.4 Y20 Z0.28 F1500.0 E30;\nG92 E0 ;Reset Extruder\nG1 Z2.0 F3000;",
    "end_gcode": ";SV04 end\nG91 ;Relative positioning\nG1 E-2 F2700 ;Retract a bit\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X0 Y240 F3000 ;Wipe out\nG1 Z10 ;Raise Z more\nG90 ;Absolute positionning\nG1 X0 Y{data['build_volume_y']} ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\nM84 X Y E ;Disable all steppers but Z",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 50.0,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 150,
    "build_volume_y": 302,
    "build_volume_z": 402,
}
