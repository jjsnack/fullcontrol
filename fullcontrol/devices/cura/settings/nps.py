default_initial_settings = {
    "name": "nps",
    "manufacturer": "Naxe",
    "start_gcode": "G28 X Y\nG1 Y10\nM104 S{data['nozzle_temp']}\nM190 S{data['bed_temp']}\nG28\nG4 S5\nG34\nG29 E0\nG21\nG90\nM83\nG1 X6 Y20 F7200\nG1 Z0.2\nM109 S{data['nozzle_temp']}\nG1 X10 Y20 Z0.2 F5000.0\nG1 X10 Y200.0 Z0.2 F900.0 E10\nG92 E0.0\nM82\nM117 Printing\n",
    "end_gcode": "M104 S0\nM140 S0\nG92 E1\nG1 E-1 F300\nG28 X0 Y0\nM84\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 300,
    "build_volume_y": 300,
    "build_volume_z": 300,
}
