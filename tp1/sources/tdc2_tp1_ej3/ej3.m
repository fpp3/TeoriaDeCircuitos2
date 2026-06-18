pkg load control;
s = tf('s');

num=-(s*0.5);
den=(s*0.025+1)*(s*6.25*1*10^(-3)+1);
H=num/den;

bodas(H);

