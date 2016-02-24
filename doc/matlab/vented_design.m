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
plotyy(cascab,Qt,cascab,wbws)