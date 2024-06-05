default_initial_settings = {
    "name": "Hellbot Magna 2 500 dual",
    "manufacturer": "Hellbot",
    "start_gcode": "M104 T0 S{data['nozzle_temp']}\nM104 T1 S{data['nozzle_temp']}\nM109 T0 S{data['nozzle_temp']}\nM109 T1 S{data['nozzle_temp']}\nG21\nG90 \nG28 X0 Y0 \nG28 Z0 \nG1 Z15.0 F300 \nT0 \nG92 E0 \nG1 F700 E-80 \nT1 \nG92 E0 \nG1 F1000 X1 Y1 Z0.3 \nG1 F600 X200 E60 \nG1 F1000 Y3 \nG1 F600 X1 E120 \nT1 \nG92 E0 \nG28 X0 Y0 \nG1 F700 E-80 \nT0 \nG92 E0",
    "end_gcode": "M104 T0 S0\nM104 T1 S0\nM140 S0\nG92 E1\nG1 E-1 F300\nG28 X0 Y0\nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 500,
    "build_volume_y": 500,
    "build_volume_z": 500,
}
