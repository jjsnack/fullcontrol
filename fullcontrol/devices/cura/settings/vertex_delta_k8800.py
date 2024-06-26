default_initial_settings = {
    "name": "Vertex Delta K8800",
    "manufacturer": "Velleman N.V.",
    "start_gcode": "; Vertex Delta Start Gcode\nM0 Is my nozzle clean?\nM400\nG28 ; Home extruder\nM106 S128 ; Start fan\nM104 T0 R130 ; Set cold nozzle\nM109 T0 R130 ; Wait for cold nozzle\nM117 Leveling bed...\nG29 ; Level Bed\nG1 X0 Y100 Z1 F2000\nG92 Z0.9 ; Set Z position (SET Z OFFSET HERE -> 1 - OFFSET)\nM107 ; Stop fan\nG90 ; Absolute positioning\nM82 ; Extruder in absolute mode\nM104 T0 S{data['nozzle_temp']}\nG92 E0 ; Reset extruder position\nM109 T0 S{data['nozzle_temp']}\nM117 Priming nozzle...\nM83\nG1 E20 F100 ; purge/prime nozzle\nM82\nG92 E0 ; Reset extruder position\nG4 S3 ; Wait 3 seconds\nG1 Z5 F2000\nM117 Vertex Delta printing",
    "end_gcode": "; Vertex Delta end code\nM107 ; Turn off fan\nG91 ; Relative positioning\nT0\nG1 E-1 F1500; Reduce filament pressure\nM104 T0 S0\nG90 ; Absolute positioning\nG92 E0 ; Reset extruder position\nM300 S4000 P500\nM300 S3000 P500\nM300 S2000 P800\nG28\nM84 ; Turn steppers off",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 35,
    "travel_speed": 190,
    "dia_feed": 2.85,
    "build_volume_x": 200,
    "build_volume_y": 200,
    "build_volume_z": 225,
}
