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
%Le=1e-4;
Ces=1e-3;
%Les=1e-3;
Res=30;
Les=2*Res^2*Ces

Ze=(1./(blank.*Res)+1./(i.*omega.*Les)+i.*omega.*Ces).^-1;
transfer2=omega.*Ze./(Re.*blank+i.*omega.*Le+Ze);
loglog(omega./2/pi,abs(transfer1).^2,omega./2/pi,abs(transfer2).^2)

xlabel('Frequency (Hz)')
ylabel('Power Transfer Function')
grid on