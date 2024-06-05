default_initial_settings = {
    "name": "Zav Max",
    "manufacturer": "Zav Co., Ltd.",
    "start_gcode": ";---- Starting Script Start ----\nG90                     ;absolute positioning\nM82                     ;set extruder to absolute mode\nM107                   ;start with the fan off\nG28 Z0                ;move Z to min endstops\nG28 X0 Y0           ;move X/Y to min endstops\nG92 E0                ;zero the extruded length\nG1  F5000           ;set speed\nG1 Y40                ;move to start position Y\nM117 Printing...\n;---- Starting Script End ----\n",
    "end_gcode": ";---- Ending Script Start ----\nM104 S0                                        ;extruder heater off\nM140 S0                                        ;heated bed heater off (if you have it)\nG91                                               ;relative positioning\nG1 E-4 F300                                  ;retract the filament a bit before lifting the nozzle to release some of the pressure\nG1 Z+0.5 E-5 X-20 Y-20 F5000    ;move Z up a bit and retract filament even more\nG28 Z0                                          ;move bed down\nG28 X0 Y0                                     ;move X/Y to min endstops so the head is out of the way\nM84                                              ;steppers off\nG90                                              ;absolute positioning\nM107                                            ;switch off cooling fan\nM355 S0 P0                                  ;switch off case light\n;---- Ending Script End ----\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 80,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 200,
    "build_volume_y": 200,
    "build_volume_z": 240,
}
