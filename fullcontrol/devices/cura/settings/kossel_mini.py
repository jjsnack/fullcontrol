default_initial_settings = {
    "name": "Kossel Mini",
    "manufacturer": "Johann",
    "start_gcode": "G21 ;metric values\nG90 ;absolute positioning\nM82 ;set extruder to absolute mode\nM107 ;start with the fan off\nG28 ;Home all axes (max endstops)\nG1 Z15.0 F9000 ;move the platform down 15mm\nG92 E0 ;zero the extruded length\nG1 F200 E3 ;extrude 3mm of feed stock\nG92 E0 ;zero the extruded length again\nG1 F9000\n;Put printing message on LCD screen\nM117 Printing...",
    "end_gcode": "M104 S0 ;extruder heater off\nM140 S0 ;heated bed heater off (if you have it)\nG91 ;relative positioning\nG1 E-1 F300  ;retract the filament a bit before lifting the nozzle, to release some of the pressure\nG28 ;Home all axes (max endstops)\nM84 ;steppers off\nG90 ;absolute positioning",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 170,
    "build_volume_y": 170,
    "build_volume_z": 200,
}
