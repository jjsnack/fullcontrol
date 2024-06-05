default_initial_settings = {
    "name": "Kemiq Q2 Gama",
    "manufacturer": "Kemiq",
    "start_gcode": "G28 ;Home\nG1 Z15.0 F6000 ;Move the platform down 15mm\nG92 E0\nG1 F200 E3\nG92 E0\nM80 ;Lights On",
    "end_gcode": "M104 S0\nM140 S0\nG92 E1\nG1 E-1 F300\nG28 X0 Y0\nM84\nM80 ;Lights Off",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 190,
    "build_volume_y": 200,
    "build_volume_z": 273,
}
