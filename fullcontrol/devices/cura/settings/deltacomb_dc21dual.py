default_initial_settings = {
    "name": "Deltacomb DC-21 Dual",
    "manufacturer": "Deltacomb 3D Printers",
    "start_gcode": ";---------------------------------------\n;Deltacomb start script\n;---------------------------------------\nG21 ;metric values\nG90 ;absolute positioning\nM107 ;start with the fan off\nG28 ;Home all axes (max endstops)\nM420 S1; Bed Level Enable\nG92 E0 ;zero the extruded length\nG1 Z15.0 F9000 ;move to the platform down 15mm\nG1 F9000\n\n;Put printing message on LCD screen\nM117 In stampa...\nM140 S{data['bed_temp']} ;set the target bed temperature\n;---------------------------------------",
    "end_gcode": ";---------------------------------------\n;Deltacomb end script\n;---------------------------------------\nG91 ;relative positioning\nG1 F15000 X8.0 E-4.5 ;Wipe filament+material retraction\nG1 F15000 E4.0 Z1 ;Retraction compensation\nG28 ;Home all axes (max endstops)\nM84 ;steppers off\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 80,
    "travel_speed": 170,
    "dia_feed": 2.85,
    "build_volume_x": 190,
    "build_volume_y": 190,
    "build_volume_z": 400,
}
