# TC2 - Trabajo Práctico Nº 2: Caracterización de Filtro Activo (Sección 2.1.5)

Aplicación web interactiva y ultrarrápida diseñada específicamente para la toma de datos de laboratorio, cálculo automático de tolerancias/errores, trazado de curvas y exportación para el informe de la **Sección 2.1.5** del TP2 de **Teoría de Circuitos II (UTN FRC)**.

---

## 🚀 Cómo ejecutar la aplicación

Podés iniciarla con Python (abre el navegador automáticamente):

```bash
python3 run_app.py
```

O también podés abrir directamente en tu navegador el archivo:
```bash
app/index.html
```

> **Nota:** La aplicación es **100% offline y autónoma** (las librerías están incluidas localmente en `app/lib/`), por lo que podés usarla en el laboratorio sin conexión a internet ni WiFi.

---

## ⚡ Características principales

### 1. Pensada para mediciones de tensión sobre resistencias y puntos de prueba
Tal como se trabaja en el banco de laboratorio, **no hace falta abrir el circuito para intercalar un amperímetro**:
- **Entrada ($I_{in}$):** Se ingresa la caída de tensión medida sobre la resistencia de shunt de entrada ($V_{Rshunt,in}$), y la app calcula $I_{in} = \frac{V_{Rshunt,in}}{R_{shunt,in}}$.
- **Etapa 1 ($V_{E1}$):** Medición de tensión en la salida del restador (pin 8 de U1C) respecto a GND.
- **Etapa 2 ($V_{filtro}$):** Medición de tensión en la salida del Sallen-Key (pin 14 de U1D) respecto a GND.
- **Etapa 3 ($I_{out}$ hacia PLC):** Permite elegir cómo se midió la salida:
  1. *Caída sobre $R_{carga}$ ($V_{Rcarga}$):* $I_{out} = \frac{V_{Rcarga}}{R_{carga}}$ (Recomendado).
  2. *Tensión en colector de Q1 ($V_C$ a GND):* $V_{Rcarga} = V_{CC} - V_C \implies I_{out} = \frac{V_{Rcarga}}{R_{carga}}$.
  3. *Tensión en emisor de Q1 ($V_E$ sobre $R_{shunt,out}$):* $I_E = \frac{V_E}{R_{shunt,out}} \implies I_{out} = \alpha \cdot I_E$.
  4. *Medición directa con miliamperímetro* ($I_{out}$ en mA).

### 2. Calibración real de componentes
Permite ingresar los valores reales medidos con multímetro de:
- $R_{shunt,in}$ (nominal 250 $\Omega$)
- $R_{shunt,out}$ (nominal 250 $\Omega$)
- $R_{carga}$ (nominal 250 $\Omega$)
- $V_{CC}$ de fuente (nominal 24.0 V)
- $\beta$ estimado del transistor BC337 / 2N2222 (para evaluar el error teórico por corriente de base $\alpha = \frac{\beta}{\beta+1}$)

### 3. Caracterización Estática (Linealidad 4 a 20 mA)
- Puntos estándar de inyección: 4 mA, 8 mA, 12 mA, 16 mA y 20 mA (con posibilidad de agregar o quitar filas).
- Cálculo en tiempo real de errores relativos porcentuales de cada etapa.
- Regresión lineal por mínimos cuadrados ($I_{out} = m \cdot I_{in} + b$) y coeficiente $R^2$.
- Gráfico interactivo de la curva de transferencia $I_{out}$ vs $I_{in}$ superpuesto a la recta ideal.
- Gráfico de barras de distribución de errores por etapa.

### 4. Caracterización Dinámica (Bode 1 Hz a 100 Hz)
- Barrido de frecuencias con inyección senoidal + offset DC.
- Entrada de $V_{in}$ y $V_{out}$ (en $V_{pp}$ medidos con osciloscopio) y $\Delta t$ opcional para fase.
- Cálculo automático de ganancia $A_v$, magnitud en dB y comparación contra la curva teórica de Butterworth de 2º orden ($f_c = 10\text{ Hz}$):
  $$|H(jf)|_{\text{dB}} = -10 \log_{10}\left(1 + \left(\frac{f}{10}\right)^4\right)$$
- **Frecuencia de corte real a -3 dB:** Interpolación log-lineal automática del punto exacto donde la ganancia cruza $-3.01\text{ dB}$.
- **Atenuación exacta a 50 Hz:** Verificación del rechazo al ruido de red de 50 Hz (ideal $-27.97\text{ dB}$, atenuación $\sim 25\times$).
- **Pendiente asintótica (Roll-off):** Cálculo de la caída en dB/década en la banda de rechazo (ideal $-40\text{ dB/déc}$).
- Diagrama de Bode interactivo en escala logarítmica con curva teórica continua, marcadores experimentales y líneas guía.

### 5. Guardado, Carga y Exportación
- **Auto-guardado en LocalStorage:** Cualquier dato ingresado queda guardado automáticamente en el navegador; si recargás la página o cerrás la pestaña, nada se pierde.
- **Guardar / Cargar Sesión JSON:** Backup completo descargable en formato `.json` para archivar o compartir entre compañeros de grupo.
- **Exportación CSV:** Descarga directa de archivos `.csv` para procesar en Excel, Google Sheets, Python o MATLAB.
- **Generador de Tablas LaTeX:** Código fuente listo con formato `\begin{table}` y `tabular` para pegar en Overleaf.
- **Resumen Markdown:** Conclusiones y valores clave listos para el informe.
- **Exportación de Gráficos:** Botones para descargar las imágenes PNG en alta definición.
- **Botón "Cargar Demo":** Carga datos coherentes de simulación para verificar visualmente todo el funcionamiento.
