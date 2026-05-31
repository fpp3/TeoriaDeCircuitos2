pkg load control;
s = tf('s');
H =  (18.2967*10^9)/((s + 166500.1665)*(s + 109890.1099));
bodas(H);
