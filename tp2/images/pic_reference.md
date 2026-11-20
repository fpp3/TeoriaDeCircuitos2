# Acondicionador de señal (lazo 4-20mA)
lazo_osc_2hz.png: entrada vs salida (2hz)
lazo_osc_50hz.png: entrada vs salida (50hz)
lazo_fft_mag.png: FFT magnitud (-3db)
lazo_fft_fc.png: FFT (fc=12.6hz)

# HPF (Chebyshev MFB 4to orden)
hpf_fft_mag.png: FFT magnitud (-3db)
hpf_fft_freq.png: FFT (fc)
hpf_osc_11khz.png: entrada vs salida (11khz)
hpf_osc_25khz.png: entrada vs salida (25khz, 6 veces de ganancia)

# LPF (Butterworth Sallen-Key 4to orden)
lpf_fft_mag.png: FFT amplitud (0.5db)
lpf_fft_freq.png: FFT frecuencia (fc)
lpf_mag.png: entrada vs salida (10kHz, ganancia en banda de paso)

# Pictures
pcb_lazo_4-20ma.jpg: Placa completa acondicionador lazo 4-20mA
pcb_hpf_mfb.jpg: Placa filtro pasa-altos MFB 4to orden
pcb_lpf_sk.jpg: Placa filtro pasa-bajos Sallen-Key 4to orden

# Diagramas esquemáticos de circuitos (KiCad vector PDF)
sch_ampli_instrumentacion.pdf: Diagrama circuital completo del acondicionador de campo con valores
sch_lpf_sk.pdf: Diagrama circuital del filtro pasa-bajos Sallen-Key 4to orden con valores
sch_hpf_mfb.pdf: Diagrama circuital del filtro pasa-altos MFB 4to orden con valores
sch_bpf_sk.pdf: Diagrama circuital del filtro pasa-banda Sallen-Key 2do orden con valores

# Gráficos vectoriales de simulación AC (Bode magnitud y fase)
sim_bode_amp_ins.pdf: Diagrama de Bode AC del acondicionador de campo (fc=10Hz, rechazo 50Hz)
sim_bode_lpf.pdf: Diagrama de Bode AC del filtro pasa-bajos Sallen-Key 4to orden (fc=19kHz, Av=+19.08dB)
sim_bode_hpf.pdf: Diagrama de Bode AC del filtro pasa-altos MFB 4to orden (fc=11kHz, Chebyshev 3dB)
sim_bode_bpf.pdf: Diagrama de Bode AC del filtro pasa-banda Sallen-Key 2do orden (f0=25kHz, BW=2kHz)
