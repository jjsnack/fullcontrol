default_initial_settings = {
    "name": "Farm 2",
    "manufacturer": "Farm3D LLC",
    "start_gcode": "G28 ;Home\nG1 Y0 Z3.0 F4000 ;Move the platform\nG92 E0\nG1 F1000 Z0.2\nG1 X190 F1000 E50 Z0.2\nG92 E0",
    "end_gcode": "M104 S0\nM140 S0\nG92 E1\nG1 E-1 F300\nG28\nM84\nM81",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 203,
    "build_volume_y": 199,
    "build_volume_z": 197,
}
