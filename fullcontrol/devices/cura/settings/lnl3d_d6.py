default_initial_settings = {
    "name": "LNL3D D6",
    "manufacturer": "LNL3D",
    "start_gcode": "G21              ;metric values\nG90              ;absolute positioning\nM82              ;set extruder to absolute mode\nM107             ;start with the fan off\nG28              ;move to min endstops\nG92 E0           ;reset extruder\nG1 E15 F1500     ;move extruder 15mm\nG1 Z15.0 F3000   ;move the header up 15mm\nM117 printing... ;LCD message",
    "end_gcode": "M104 T0 S0                   ;left extruder heater off\nM104 T1 S0                   ;right extruder heater off\nM140 S0                      ;heated bed heater off (if you have it)\nG91                          ;relative positioning\nG1 E-1 F300                  ;retract the filament a bit before lifting the nozzle, to release some of the pressure\nG1 Z+0.5 E-5 X-20 Y-20 F9000 ;move Z up a bit and retract filament even more\nG28 X0 Y0                    ;move X/Y to min endstops, so the head is out of the way\nM84                          ;steppers off\nG90                          ;absolute positioning",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 80.0,
    "dia_feed": 1.75,
    "build_volume_x": 600,
    "build_volume_y": 600,
    "build_volume_z": 600,
}
