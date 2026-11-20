#!/usr/bin/env python3
import csv
import os
import re

DATA_DIR = 'sources/data'
SIM_OUT_DIR = 'sources/sim_out'

def generate():
    os.makedirs(DATA_DIR, exist_ok=True)

    # 1. amp_ins
    with open(os.path.join(SIM_OUT_DIR, 'ampli-instrumentacion-ac.csv'), 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        rows = []
        for r in reader:
            if r and r[0].strip():
                freq = float(r[0].replace(',', '.'))
                gain = float(r[2].replace(',', '.'))
                rows.append((freq, gain))
    with open(os.path.join(DATA_DIR, 'data_bode_amp_ins.txt'), 'w', encoding='utf-8') as f:
        f.write('freq gain_db\n')
        for freq, gain in rows:
            f.write(f'{freq:.6g} {gain:.6g}\n')

    # 2. hpf
    with open(os.path.join(SIM_OUT_DIR, 'filter-HP-MFB-ac.csv'), 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        rows = []
        for r in reader:
            if r and r[0].strip():
                freq = float(r[0].replace(',', '.'))
                gain = float(r[2].replace(',', '.'))
                rows.append((freq, gain))
    with open(os.path.join(DATA_DIR, 'data_bode_hpf.txt'), 'w', encoding='utf-8') as f:
        f.write('freq gain_db\n')
        for freq, gain in rows:
            f.write(f'{freq:.6g} {gain:.6g}\n')

    # 3. bpf
    with open(os.path.join(SIM_OUT_DIR, 'filter-BP-SK-ac.csv'), 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        rows = []
        for r in reader:
            if r and r[0].strip():
                freq = float(r[0].replace(',', '.'))
                gain = float(r[2].replace(',', '.'))
                rows.append((freq, gain))
    with open(os.path.join(DATA_DIR, 'data_bode_bpf.txt'), 'w', encoding='utf-8') as f:
        f.write('freq gain_db\n')
        for freq, gain in rows:
            f.write(f'{freq:.6g} {gain:.6g}\n')

    # 4. lpf
    with open(os.path.join(SIM_OUT_DIR, 'filter-LP-SK-ac.txt'), 'r', encoding='latin-1') as f:
        lines = f.readlines()
    rows = []
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        freq = float(parts[0])
        m = re.search(r'\(([-+0-9.eE]+)dB', parts[1])
        if m:
            gain = float(m.group(1))
            rows.append((freq, gain))
    with open(os.path.join(DATA_DIR, 'data_bode_lpf.txt'), 'w', encoding='utf-8') as f:
        f.write('freq gain_db\n')
        for freq, gain in rows:
            f.write(f'{freq:.6g} {gain:.6g}\n')

if __name__ == '__main__':
    generate()
    print('Bode data generated successfully in sources/data/')
