default_initial_settings = {
    "name": "3DTech Semi-Professional",
    "manufacturer": "3DTech",
    "start_gcode": "G28 ; home all axes\nG29 ;\nG1 Z5 F3000 ; lift\nG1 X5 Y25 F5000 ; move to prime\nG1 Z0.2 F3000 ; get ready to prime\nG92 E0 ; reset extrusion distance\nG1 Y100 E20 F600 ; prime nozzle\nG1 Y140 F5000 ; quick wipe",
    "end_gcode": "M104 S0\nM140 S0 ; Retract the filament\nG92 E1\nG1 E-1 F300\nG28 X0 Y0\nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 250,
    "build_volume_y": 250,
    "build_volume_z": 300,
}
