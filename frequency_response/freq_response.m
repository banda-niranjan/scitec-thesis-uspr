%Frequency response of the transducer

data = readtable("freq_response.xlsx");

x_freq = data.freq/1e3;
y1_impedance = data.impedance;
y2_phase = data.phase_angle;

yyaxis left;
loglog(x_freq, y1_impedance);
ylabel("Impedance in Ohm (Ω)");
xlabel("Frequencies in KHz");

yyaxis right;
ylabel("Phase in degree");
ylim([-70 70]);
