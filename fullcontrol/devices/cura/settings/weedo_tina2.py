default_initial_settings = {
    "name": "WEEDO TINA2",
    "manufacturer": "WEEDO",
    "start_gcode": "\n;(**** start.gcode for tina2****)\nM203 Z15\nM104 S150\nG28 Z\nG28 X Y; Home extruder\nG1 X55 Y55 F1000\nG29\nM107 ; Turn off fan\nG90 ; Absolute positioning\nM82 ; Extruder in absolute mode\nM109 S{data['nozzle_temp']}\nG92 E0 ; Reset extruder position\nG1 X90 Y6 Z0.27 F2000\nG1 X20 Y6 Z0.27 E15 F1000\nG92 E0 ; Reset extruder position\nM203 Z5",
    "end_gcode": ";(**** end.gcode for tina2****)\nM203 Z15\nM104 S0\nM107\nG92 E0 (Reset after prime)\nG0 E-1 F300\nG28 Z F300\nG28 X0 Y0\nG1 Y90 F1000",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 95.0,
    "print_speed": 40.0,
    "travel_speed": 65.0,
    "dia_feed": 1.75,
    "build_volume_x": 100,
    "build_volume_y": 120,
    "build_volume_z": 100,
}
