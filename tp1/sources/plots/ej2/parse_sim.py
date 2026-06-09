import re

input_path = "bode_simulado.txt .txt"
output_path = "bode_simulado.csv"

# Read input file
with open(input_path, 'r', encoding='latin-1') as f:
    lines = f.readlines()

csv_lines = ["frequency,magnitude,phase\n"]

for line in lines:
    line = line.strip()
    if not line or line.startswith("Freq."):
        continue
    
    # Split by whitespace
    parts = line.split()
    if len(parts) < 2:
        continue
    
    freq = parts[0]
    data = "".join(parts[1:]) # e.g. (-1.735dB,-1.14e-05°)
    
    # Strip parentheses
    data = data.replace('(', '').replace(')', '')
    data_parts = data.split(',')
    if len(data_parts) != 2:
        continue
        
    mag_str, phase_str = data_parts
    
    # Remove 'dB' and degree symbol or any non-numeric suffixes
    mag = mag_str.replace('dB', '').strip()
    # Remove degree symbol (which might be represented differently in latin-1)
    phase = re.sub(r'[^0-9eE\.\+\-]', '', phase_str).strip()
    
    csv_lines.append(f"{freq},{mag},{phase}\n")

# Downsample to ~500 points to keep LaTeX fast and avoid memory limits
total_points = len(csv_lines) - 1
step = max(1, total_points // 500)

downsampled = [csv_lines[0]]
for i in range(1, len(csv_lines), step):
    downsampled.append(csv_lines[i])

# Ensure the last point is included
if step > 1 and (len(csv_lines) - 1) % step != 0:
    downsampled.append(csv_lines[-1])

with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(downsampled)

print(f"Processed {total_points} points. Wrote {len(downsampled)-1} points to {output_path}")
