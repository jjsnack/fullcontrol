default_initial_settings = {
    "name": "Cubicon Single",
    "manufacturer": "Cubicon",
    "start_gcode": "M911 3DP-110F\nM201 X400 Y400\nM202 X400 Y400\nG28 ; Home\nG1 Z15.0 F6000 ;move the platform down 15mm\n;Prime the extruder\nG92 E0\nG1 F200 E3\nG92 E0",
    "end_gcode": "M104 S0\nM140 S0\nM904\nM117 Print completed! \nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 240,
    "build_volume_y": 190,
    "build_volume_z": 200,
}
