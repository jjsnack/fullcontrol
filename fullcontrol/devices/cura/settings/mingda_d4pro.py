default_initial_settings = {
    "name": "Mingda D4 Pro",
    "manufacturer": "Mingda",
    "start_gcode": "G28 ; home all axes\n G29; ABL\n M117 Purge extruder\n G92 E0 ; reset extruder\n G1 Z1.0 F3000 ; move z up little to prevent scratching of surface\n G1 X2 Y20 Z0.3 F5000.0 ; move to start-line position\n G1 X2 Y200.0 Z0.3 F1500.0 E15 ; draw 1st line\n G1 X2 Y200.0 Z0.4 F5000.0 ; move to side a little\n G1 X2 Y20 Z0.4 F1500.0 E30 ; draw 2nd line\n G92 E0 ; reset extruder\n G1 Z1.0 F3000 ; move z up little to prevent scratching of surface",
    "end_gcode": " G91; relative positioning\n G1 Z1.0 F3000 ; move z up little to prevent scratching of print\n G90; absolute positioning\n G1 X0 Y0 F1000 ; prepare for part removal\n M104 S0; turn off extruder\n M140 S0 ; turn off bed\n M84 ; disable motors\n M106 S0 ; turn off fan",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60.0,
    "travel_speed": 90.0,
    "dia_feed": 1.75,
    "build_volume_x": 420,
    "build_volume_y": 420,
    "build_volume_z": 400,
}
