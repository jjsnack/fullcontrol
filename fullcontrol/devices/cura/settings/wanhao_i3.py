default_initial_settings = {
    "name": "Wanhao Duplicator i3",
    "manufacturer": "Wanhao",
    "start_gcode": "G21 ;metric values\n G90 ;absolute positioning\n M82 ;set extruder to absolute mode\n M107 ;start with the fan off\n G28 X0 Y0 ;move X/Y to min endstops\n G28 Z0 ;move Z to min endstops\n G1 Z15.0 F{data['travel_speed']} ;move the platform down 15mm\n G92 E0 ;zero the extruded length\n G1 F200 E6 ;extrude 6 mm of feed stock\n G92 E0 ;zero the extruded length again\n G1 F{data['travel_speed']} \n ;Put printing message on LCD screen\n M117 Printing...",
    "end_gcode": "M104 S0 ;extruder heater off \n G91 ;relative positioning\n G1 E-1 F300  ;retract the filament a bit before lifting the nozzle, to release some of the pressure\n G1 Z+0.5 E-5 X-20 Y-20 F{data['travel_speed']} ;move Z up a bit and retract filament even more\n G28 X0 Y0 ;move X/Y to min endstops, so the head is out of the way\n M84 ;steppers off\n G90 ;absolute positioning",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 200,
    "build_volume_y": 200,
    "build_volume_z": 180,
}
