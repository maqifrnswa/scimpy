clear all
close all

linestyle={'-','--','-.','-','--','-.','-','--','-.','-','--','-.'};

index=1;
for k=.2:.2:1
    fact=.125.*k.^4+.75.*k.^2+0.125;
    A4=1;%.125.*k.^4+.75.*k.^2+0.125;%in Thiele, they divide by numerator
    A0=1;
    A1=2.6131.*k./(fact.^(1/4));
    A2=(2.4143.*k.^2+1)./(fact.^(1/2));
    A3=(.9239.*k.^3+1.6892.*k)./(fact.^(3/4));
    
    Qt(index)=1./sqrt(A1.*A3);
    index=index+1;
    wbws=A1./A3;

    omega=.4:.01:10; %actually omega/omega_s. Need to convert to omega/omega_c = omega/omega_s/sqrt(h)
    loglog(omega,abs(A4.*(omega./sqrt(wbws)).^4./(A4.*(omega./sqrt(wbws)).^4.-i.*A3.*(omega./sqrt(wbws)).^3-A2.*(omega./sqrt(wbws)).^2+i.*A1.*(omega./sqrt(wbws))+A0)).^2,linestyle{index-1}, 'LineWidth',2)
    hold on
end

for Qt_qb3=0.35:-.05:0.15;
    A4=1;
    A2=sqrt(2.*(1./Qt_qb3.^2-1));
    A3=sqrt(2.*A2);
    A1=(2+A2.^2)./(2.*A3);
    Qt(index)=Qt_qb3;
    index=index+1;
    wbws=A1./A3;
    omega=.4:.01:10; %actually omega/omega_s. Need to convert to omega/omega_c = omega/omega_s/sqrt(h)
    loglog(omega,abs(A4.*(omega./sqrt(wbws)).^4./(A4.*(omega./sqrt(wbws)).^4.-i.*A3.*(omega./sqrt(wbws)).^3-A2.*(omega./sqrt(wbws)).^2+i.*A1.*(omega./sqrt(wbws))+A0)).^2,linestyle{index-1}, 'LineWidth',2)
    hold on
end

xlim([.4 10])
ylim([1e-2 10])
legend(num2str(Qt'),'Location','southeast')
xlabel('\omega/\omega_s')
ylabel('Power Transfer Function')
grid on
print('chebyfilters','-depsc')