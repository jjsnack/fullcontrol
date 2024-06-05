default_initial_settings = {
    "name": "MBot3D Grid 4",
    "manufacturer": "Magicfirm",
    "start_gcode": ";---------- START GCODE ----------\nG21 ; set units to millimeters\nG28 ; home all axes\nG29 ;Autolevel bed\nG1 Z10 F400\nG1 X145 Z10 F2400\nG92 E0\nG1 X145 Z0.5 F400\nG1 X120 Z0.5 E20 F360\nG92 E0.0\n;----------END START GCODE ----------\n",
    "end_gcode": "M104 S0 ; turn off extruder\nM140 S0 ; turn off heatbed\nM107 ; turn off fan\nG1 Z190 F900\nG28 X Y  ;home X Y axes\nM84 ; disable motors",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 235,
    "build_volume_y": 210,
    "build_volume_z": 190,
}
