default_initial_settings = {
    "name": "Geeetech MizarM",
    "manufacturer": "Geeetech",
    "start_gcode": ";Official open-source firmware for MizarM: https://github.com/Geeetech3D/Mizar-M \n\nM104 S{data['nozzle_temp']} ; Set Hotend Temperature\nM190 S{data['bed_temp']} ; Wait for Bed Temperature\nM109 S{data['nozzle_temp']} ; Wait for Hotend Temperature\nG92 E0 ; Reset Extruder\nG28 ; Home all axes\nM107 P0 ;Off Main Fan\nM107 P1 ;Off Aux Fan\nM2012 P8 S1 F100 ; ON Light\n;M106 P0 S383 ; ON MainFan 150% if need\n;M106 P1 S255 ; ON Aux Fan 100% if need\nG1 Z5.0 F3000 ;Move Z Axis up little to prevent scratching of Heat Bed\nG1 X0.1 Y20 Z0.8 F5000 ; Move to start position\nG1 X0.1 Y200.0 Z1.2 F1500 E30 ; Draw the first line\nG92 E0 ; Reset Extruder\nG1 X0.4 Y200.0 Z1.2 F3000 ; Move to side a little\nG1 X0.4 Y20 Z1.2 F1500 E25 ; Draw the second line\nG92 E0 ; Reset Extruder\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 X5 Y20 Z0.4 F3000.0 ; Scrape off nozzle residue",
    "end_gcode": "G91 ;Switch to relative positioning\nG1 E-2.5 F2700 ;Retract filament\nG1 E-1.5 Z0.2 F2400 ;Retract and raise Z\nG1 X5 Y5 F3000 ;Move away\nG1 Z10 ;lift print head\nG90 ;Switch to absolute positioning\nG28 X Y ;homing XY\nM106 S0 ;off Fan\nM104 S0 ;Cooldown hotend\nM140 S0 ;Cooldown bed\nM84 X Y E ;Disable steppers",
    "bed_temp": 60,
    "nozzle_temp": 200,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 255,
    "build_volume_y": 255,
    "build_volume_z": 260,
}
