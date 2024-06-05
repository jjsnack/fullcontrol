default_initial_settings = {
    "name": "Volumic SH65",
    "manufacturer": "Volumic",
    "start_gcode": "M117 Demarrage\nM106 S0\nM140 S{data['bed_temp']}\nM104 T0 S{data['nozzle_temp']}\nG28\nG90\nM82\nG92 E0\nG1 Z3 F600\nM109 T0 S{data['nozzle_temp']}\nM300 P350\nM117 Purge\nG1 Z0.15 F600\nG1 E10 F400\nG92 E0\nM117 Impression",
    "end_gcode": "M107\nG91\nT0\nG1 E-1\nM104 T0 S0\nG90\nG0 X1 Y190 F5000\nG92 E0\nM140 S0\nM84\nM300",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 650,
    "build_volume_y": 300,
    "build_volume_z": 300,
}
