clear all
close all

k=.3:.01:1;

fact=.125.*k.^4+.75.*k.^2+0.125;
A0=1;
A4=1;
A1=2.6131.*k./(fact.^(1/4));
A2=(2.4143.*k.^2+1)./(fact.^(1/2));
A3=(.9239.*k.^3+1.6892.*k)./(fact.^(3/4));

%need to keep track of w_c s everywhere!
Qt=1./sqrt(A1.*A3);
wbws=A1./A3;
cascab=(A1.*A2.*A3-A1.^2-A3.^2)./(A3.^2);

%plot(k,Qt,k,wbws,k,cascab);
%plotyy(cascab,Qt,cascab,wbws)
hold on


Qt_qb3=0.38:-.01:0.15;
A2=sqrt(2.*(1./Qt_qb3.^2-1));
A3=sqrt(2.*A2);
A1=(2+A2.^2)./(2.*A3);

wbws_qb3=A1./A3;
cascab_qb3=(A1.*A2.*A3-A1.^2-A3.^2)./(A3.^2);

figure
Qt_total=[Qt,Qt_qb3]
wbws_total=[wbws,wbws_qb3]
cascab_total=[cascab,cascab_qb3]

plotyy(cascab_total,Qt_total,cascab_total,wbws_total, 'semilogx')
grid on