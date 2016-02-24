clear all
close all

for k=.2:.2:1
    fact=.125.*k.^4+.75.*k.^2+0.125;
    A0=1;%in Thiele, they divide by numerator
    A4=1;
    A3=2.6131.*k./(fact.^(1/4));
    A2=(2.4143.*k.^2+1)./(fact.^(1/2));
    A1=(.9239.*k.^3+1.6892.*k)./(fact.^(3/4));
    omega=.1:.01:20;
    loglog(omega,abs(omega.^4./(A0.*omega.^4.-i.*A1.*omega.^3-A2.*omega.^2+i.*A3.*omega+A4)))
    hold on
end
