clear all
close all

Re=7;
Le=0;
%Le=1e-4;
Ces=1e-3;
Les=1e-3;
Res=30;

omega=[20*2*pi:1:20000*2*pi];
blank=ones(1,length(omega));
Ze=(1./(blank.*Res)+1./(i.*omega.*Les)+i.*omega.*Ces).^-1;
transfer1=omega.*Ze./(Re.*blank+i.*omega.*Le+Ze);

Re=7;
%Le=1e-3;
Le=1e-3;
Ces=1e-3;
Les=1e-3;
Res=30;
%Les=2*Res^2*Ces

Ze=(1./(blank.*Res)+1./(i.*omega.*Les)+i.*omega.*Ces).^-1;
transfer2=omega.*Ze./(Re.*blank+i.*omega.*Le+Ze);
loglog(omega./2/pi,abs(transfer1).^2,omega./2/pi,abs(transfer2).^2)

xlabel('Frequency (Hz)')
ylabel('Power Transfer Function')
grid on

Re=7;
%Le=1e-3;
Le=1e-4;
Ces=1e-3;
Les=1e-3;
Res=20;
%Les=2*Res^2*Ces

Ze=(1./(blank.*Res)+1./(i.*omega.*Les)+i.*omega.*Ces).^-1;

figure
impedance=Re.*blank+i.*omega.*Le+Ze;
semilogx(omega./2/pi,abs(impedance).^2)

xlabel('Frequency (Hz)')
ylabel('Impedance (Ohms)')
grid on

figure
Re=7;
Le=1e-4;
%Le=0;
Ces=1e-3;
Les=1e-3;
Res=30;
Les=2*((Res*Re)/(Re+Res))^2*Ces

Ze=(1./(blank.*Res)+1./(i.*omega.*Les)+i.*omega.*Ces).^-1;
transfer3=omega.*Ze./(Re.*blank+i.*omega.*Le+Ze);
loglog(omega./2/pi,abs(transfer3).^2,omega./2/pi,abs(transfer2).^2)
xlabel('Frequency (Hz)')
ylabel('Power Transfer Function')
grid on

figure
semilogx(omega./2/pi,angle(transfer3),omega./2/pi,angle(transfer2).^2)
xlabel('Frequency (Hz)')
ylabel('Phase (rad)')
grid on

figure

Q=[sqrt(2)^3,sqrt(2)^2,sqrt(2)^1,sqrt(2)^0,sqrt(2)^-1,sqrt(2)^-2];
omega=[.1:.01:100];

for k=[1:length(Q)]
    transfer4(:,k)=i*omega.^2./(-omega.^2+1/Q(k).*i*omega+1);
end
loglog(omega./2/pi,abs(transfer4).^2)
xlabel('Frequency (Hz)')
ylabel('Normalized Transfer Function')
grid on
legend('show')
legend('Q=2.83','Q=2.00','Q=1.41','Q=1.00','Q=0.71','Q=0.50')
figure
semilogx(omega./2/pi,angle(transfer4))
xlabel('Frequency (Hz)')
ylabel('Phase (rad)')
grid on