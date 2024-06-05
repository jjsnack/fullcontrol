default_initial_settings = {
    "name": "Kosher Duplication",
    "manufacturer": "Sri Vignan Technologies",
    "start_gcode": "M605 S0\nT0\nM605 S2 R0 X266\nG28 X\nG28 Y\nG1 X-30 F9000\nG1 Y20 F9000\nG21\nG90\nM82\nM107\nM104 S{data['nozzle_temp']};\nM105\nM109 S{data['nozzle_temp']};\nG92 E0\nG1 E16 F210\nG92 E0\nM605 S2 X100\nG28 X\nG28 Z\n",
    "end_gcode": "G91\nG1 Z+0.5 E-16 Y+10 F9000\nG90\nM107\nM104 S0\nM140 S0\nM117\nM605 S0\nG28 X0 Y0\nM605 S1\nG28 X\nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 200,
    "dia_feed": 1.75,
    "build_volume_x": 100,
    "build_volume_y": 220,
    "build_volume_z": 300,
}
