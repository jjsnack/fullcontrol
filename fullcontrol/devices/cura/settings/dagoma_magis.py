default_initial_settings = {
    "name": "Dagoma Magis",
    "manufacturer": "Dagoma",
    "start_gcode": ";Gcode by Cura\nG90\nG28\nM107\nM109 R100\nG29\nM109 S{data['nozzle_temp']} U-55 X55 V-85 Y-85 W0.26 Z0.26\nM82\nG92 E0\nG1 F200 E6\nG92 E0\nG1 F200 E-3.5\nG0 Z0.15\nG0 X10\nG0 Z3\nG1 F6000\n",
    "end_gcode": "\nM104 S0\nM106 S255\nM140 S0\nG91\nG1 E-1 F300\nG1 Z+3 E-2 F9000\nG90\nG28\n",
    "bed_temp": 60,
    "nozzle_temp": 205,
    "material_flow_percent": 100,
    "print_speed": 40,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 195.55,
    "build_volume_y": 195.55,
    "build_volume_z": 205,
}
