default_initial_settings = {
    "name": "BQ Hephestos 2",
    "manufacturer": "BQ",
    "start_gcode": "; -- START GCODE --\nM104 S{data['nozzle_temp']}\nG28 ; Zero-ing position\nG29 ; Auto bed-leveling\nG0 X4 Y297 Z15 F4000 ; Fast move to BQ's start position\nG90 ; Set to Absolute Positioning\nG92 E0 ; Reset extruder 0\nG1 F1800 ; Set default feedrate\nM109 S{data['nozzle_temp']} ; Makes sure the temperature is correct before printing\n; -- end of START GCODE --",
    "end_gcode": "; -- END GCODE --\nM801        ; Marlin G-CODE to fire end print procedure\n; -- end of END GCODE --",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 210,
    "build_volume_y": 297,
    "build_volume_z": 220,
}
